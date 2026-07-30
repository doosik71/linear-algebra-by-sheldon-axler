#!/usr/bin/env python3
r"""Normalize Markdown files so LaTeX math renders correctly on GitHub.

GitHub's Markdown renderer treats `$$...$$` as plain paragraph text, not as
an opaque fence like ``` code blocks. That means:

  * A `$$` block must be separated from surrounding prose by a blank line
    on both sides, or GitHub's parser won't recognize where the block
    starts/ends relative to the paragraph around it.
  * Every line *inside* a `$$` block is still subject to normal CommonMark
    block-level parsing. A line that happens to look like a Setext heading
    underline (bare `-`/`=` run), a thematic break (`---`, `***`, `___`),
    an ATX heading (`# ...`), a blockquote (`> ...`), a list marker
    (`- `, `1. `), or a fence (``` / ~~~) will split the math block into
    separate HTML elements and break rendering -- even though it was never
    intended as such by the author.

GitHub's math rendering also has a second, more subtle problem: even once a
`$$`/`$...$` span is correctly recognized as math, its *contents* still go
through normal CommonMark inline parsing before being handed to the math
renderer. CommonMark's backslash-escape rule removes the backslash from any
`\` immediately followed by ASCII punctuation (that's how `\*` becomes a
literal `*` in ordinary prose). Inside math this is disastrous: LaTeX
commands like `\{`, `\}`, `\|`, `\,`, `\#`, or a matrix/aligned row
separator `\\` are *themselves* backslash+punctuation, so their backslash
gets silently stripped before the math renderer ever sees it -- e.g.
`\{1,\ldots,n\}` (should show curly braces) renders as `{1,\ldots,n}` (no
braces at all, since bare `{`/`}` are invisible LaTeX grouping characters),
and `\|v\|` (norm) silently downgrades to `|v|` (absolute value). This was
verified against the actual github.com page render (not just the API), so
it is a real, pervasive problem, not a quirk of any particular preview tool.

This script fixes both classes of problems, across one or more Markdown
files in place.

Fixes applied:
  1. Insert a blank line before an opening `$$` delimiter if missing.
  2. Insert a blank line after a closing `$$` delimiter if missing.
  3. Neutralize lines inside a `$$` block that CommonMark would otherwise
     interpret as a block-level construct, by indenting them 4+ spaces
     beyond the block's own baseline indentation. 4 spaces is enough to
     defeat every one of those triggers (they all require <=3 spaces of
     indentation) while remaining a harmless "lazy continuation" line of
     the same paragraph, so the visible math content is unchanged.
  4. Strip leading/trailing space padding immediately inside inline
     `$...$` math delimiters (`$ a=b $` -> `$a=b$`).
  5. Replace a bare `|` inside inline `$...$` math with `\\vert` when that
     line is a Markdown table row (so it doesn't collide with table
     column syntax).
  6. Inside any math span (block or inline), replace backslash-escaped
     punctuation that has a letter-spelled LaTeX synonym with that synonym,
     since a `\` before a *letter* is never touched by CommonMark's escape
     rule: `\{`->`\lbrace`, `\}`->`\rbrace`, `\|`->`\Vert`, `\,`->`\thinspace`,
     `\;`->`\thickspace`, `\!`->`\negthinspace`, `\:`->`\medspace`.
  7. Inside any math span, replace an isolated `\\` (matrix/aligned row
     separator, confirmed common in this corpus) with `\cr`. `\cr` is a
     backslash+letters synonym KaTeX documents as an accepted row
     separator (https://katex.org/docs/supported.html), so like rule 6
     it's immune to the escape-stripping problem outright -- no doubling
     needed. This is preferred over doubling `\\` to `\\\\`: that trick
     only "worked" by exploiting GitHub's specific escape-stripping bug,
     and would render as *two* line breaks (an extra blank row) in any
     other renderer that reads the raw source directly (KaTeX/MathJax in
     an editor preview, Obsidian, Jupyter, etc.) where no stripping
     happens. `\cr` is correct and portable everywhere, GitHub included.
     Note: KaTeX explicitly does NOT accept `\newline` as an array/matrix
     row separator (only for a generic display-math line break), so it's
     not a safe substitute for this corpus's `\\` usage, which is always
     inside `aligned`/`pmatrix`/etc. Skipped when immediately followed by
     one of the punctuation marks handled by rule 8, so the two rules
     don't collide on the rare case of a separator glued directly to
     another escape with no space between them.
  8. Inside any math span, double a single backslash before punctuation
     with no letter-spelled synonym (`#`, `%`, `&`, `_`, `^`, `~`, `$`) so
     it survives CommonMark's escape stripping intact.

Usage:
  python fix-md-for-github.py FILE.md [FILE2.md ...]
  python fix-md-for-github.py --check FILE.md ...   # report only, no writes
  python fix-md-for-github.py "*.md"                 # glob patterns are expanded

Exit status: 0 if no fixes were needed (or --check found nothing), 1 if
--check found issues that would be fixed by a normal run.
"""

import argparse
import glob
import re
import sys

DD_RE = re.compile(r'^\s*\$\$\s*$')

# Patterns that can interrupt or transform an ongoing CommonMark paragraph.
# All of them require <=3 leading spaces to trigger, so indenting a line to
# baseline+4 unconditionally defeats every one of them.
DANGEROUS_PATTERNS = [
    ('setext-dash', re.compile(r'^\s{0,3}-+\s*$')),
    ('setext-equals', re.compile(r'^\s{0,3}=+\s*$')),
    ('thematic-break', re.compile(r'^\s{0,3}([*_])(\s*\1){2,}\s*$')),
    ('atx-heading', re.compile(r'^\s{0,3}#{1,6}(\s|$)')),
    ('blockquote', re.compile(r'^\s{0,3}>')),
    ('bullet-list', re.compile(r'^\s{0,3}[-+*]\s')),
    ('ordered-list', re.compile(r'^\s{0,3}\d{1,9}[.)]\s')),
    ('fence', re.compile(r'^\s{0,3}(```|~~~)')),
    ('html-start', re.compile(r'^\s{0,3}<[a-zA-Z!/]')),
]

INLINE_MATH_RE = re.compile(r'\$([^$\n]*)\$')
TABLE_ROW_RE = re.compile(r'^\s*\|.*\|\s*$')

# Rule 6: backslash-escaped punctuation with a letter-spelled LaTeX synonym.
# A `\` before a *letter* is never touched by CommonMark's escape rule, so
# these survive unconditionally once substituted. Note: LaTeX/KaTeX reads a
# "control word" (backslash + letters) as greedily as possible, so if the
# substituted word is immediately followed by another letter (e.g. the `a`
# in `\{a+bi` -> `\lbracea+bi`), it would merge into one broken command
# token -- a trailing space must be inserted to terminate the word cleanly.
LETTER_SYNONYMS = {
    '{': 'lbrace', '}': 'rbrace', '|': 'Vert',
    ',': 'thinspace', ';': 'thickspace', '!': 'negthinspace', ':': 'medspace',
}
LETTER_SYNONYM_RE = re.compile(r'\\([' + re.escape(''.join(LETTER_SYNONYMS)) + r'])')

# Rule 8: punctuation with no letter-spelled synonym; must survive by
# doubling the backslash instead.
NO_SYNONYM_PUNCT = '#%&_^~$'
ROW_SEP_RE = re.compile(r'(?<!\\)\\\\(?!\\)(.?)')
NO_SYNONYM_RE = re.compile(r'(\\+)([' + re.escape(NO_SYNONYM_PUNCT) + r'])')


def fix_math_escapes(s, stats):
    """Rules 6-8: make backslash-escaped punctuation survive CommonMark's
    inline escape stripping, so the LaTeX reaching the math renderer is
    unchanged from what the author intended."""
    def repl_letter(m):
        ch = m.group(1)
        word = LETTER_SYNONYMS[ch]
        key = 'escape-' + word
        stats[key] = stats.get(key, 0) + 1
        nxt = m.string[m.end():m.end() + 1]
        sep = ' ' if nxt.isalpha() else ''
        return '\\' + word + sep

    s = LETTER_SYNONYM_RE.sub(repl_letter, s)

    def repl_row_sep(m):
        nxt = m.group(1)
        if nxt and nxt in NO_SYNONYM_PUNCT:
            return m.group(0)  # let rule 8 handle this one instead
        stats['row-separator'] = stats.get('row-separator', 0) + 1
        sep = ' ' if nxt.isalpha() else ''
        return '\\cr' + sep + nxt

    s = ROW_SEP_RE.sub(repl_row_sep, s)

    def repl_no_synonym(m):
        bs, ch = m.group(1), m.group(2)
        if len(bs) % 2 == 1:
            key = 'escape-' + ch
            stats[key] = stats.get(key, 0) + 1
            return bs + '\\' + ch
        return m.group(0)

    s = NO_SYNONYM_RE.sub(repl_no_synonym, s)
    return s


def read_text(fname):
    raw = open(fname, 'rb').read()
    has_bom = raw.startswith(b'\xef\xbb\xbf')
    if has_bom:
        raw = raw[3:]
    text = raw.decode('utf-8')
    uses_crlf = text.count('\r\n') > 0
    return text, has_bom, uses_crlf


def write_text(fname, text, has_bom, uses_crlf):
    nl = '\r\n' if uses_crlf else '\n'
    out = text.replace('\r\n', '\n').replace('\n', nl)
    data = out.encode('utf-8')
    if has_bom:
        data = b'\xef\xbb\xbf' + data
    with open(fname, 'wb') as fh:
        fh.write(data)


def fix_dangerous_lines(lines, stats):
    """Rule 3: neutralize CommonMark-interrupting lines inside $$ blocks."""
    out = []
    in_block = False
    base_indent = ''
    for line in lines:
        stripped = line.rstrip('\r\n')
        if DD_RE.fullmatch(stripped):
            if not in_block:
                base_indent = stripped[:len(stripped) - len(stripped.lstrip())]
                in_block = True
            else:
                in_block = False
            out.append(line)
            continue
        if in_block:
            for name, pat in DANGEROUS_PATTERNS:
                if pat.match(stripped):
                    content = stripped.lstrip()
                    new_line = base_indent + '    ' + content
                    out.append(new_line)
                    stats[name] = stats.get(name, 0) + 1
                    break
            else:
                out.append(line)
        else:
            out.append(line)
    return out


def fix_blank_lines_around_blocks(lines, stats):
    """Rules 1 & 2: blank line before opening $$ and after closing $$."""
    out = []
    in_block = False
    n = len(lines)
    for i, line in enumerate(lines):
        stripped = line.rstrip('\r\n')
        if DD_RE.fullmatch(stripped):
            if not in_block:
                prev_nonempty = out and out[-1].strip() != ''
                if prev_nonempty:
                    out.append('')
                    stats['blank-before'] = stats.get('blank-before', 0) + 1
                in_block = True
                out.append(line)
            else:
                in_block = False
                out.append(line)
                nxt = lines[i + 1].rstrip('\r\n') if i + 1 < n else None
                if nxt is not None and nxt.strip() != '':
                    out.append('')
                    stats['blank-after'] = stats.get('blank-after', 0) + 1
        else:
            out.append(line)
    return out


def fix_inline_math_padding(lines, stats):
    """Rule 4: no space just inside inline $...$ delimiters (outside $$ blocks)."""
    out = []
    in_block = False
    for line in lines:
        stripped = line.rstrip('\r\n')
        if DD_RE.fullmatch(stripped):
            in_block = not in_block
            out.append(line)
            continue
        if in_block:
            out.append(line)
            continue

        def repl(m):
            content = m.group(1)
            trimmed = content.strip()
            if trimmed and trimmed != content:
                stats['inline-padding'] = stats.get('inline-padding', 0) + 1
                return '$' + trimmed + '$'
            return m.group(0)

        out.append(INLINE_MATH_RE.sub(repl, line) if line.strip() else line)
    return out


def fix_math_escapes_in_lines(lines, stats):
    """Apply fix_math_escapes to $$-block content lines and to each inline
    $...$ span in ordinary prose lines."""
    out = []
    in_block = False
    for line in lines:
        stripped = line.rstrip('\r\n')
        if DD_RE.fullmatch(stripped):
            in_block = not in_block
            out.append(line)
            continue
        if in_block:
            out.append(fix_math_escapes(line, stats))
            continue

        def repl(m):
            return '$' + fix_math_escapes(m.group(1), stats) + '$'

        out.append(INLINE_MATH_RE.sub(repl, line) if '$' in line else line)
    return out


def fix_table_pipes_in_math(lines, stats):
    """Rule 5: bare | inside inline $...$ math on a table row -> \\vert."""
    out = []
    in_block = False
    for line in lines:
        stripped = line.rstrip('\r\n')
        if DD_RE.fullmatch(stripped):
            in_block = not in_block
            out.append(line)
            continue
        if in_block or not TABLE_ROW_RE.match(stripped):
            out.append(line)
            continue

        def repl(m):
            content = m.group(1)
            if '|' in content:
                stats['table-pipe'] = stats.get('table-pipe', 0) + content.count('|')
                content = content.replace('|', r'\vert')
                return '$' + content + '$'
            return m.group(0)

        out.append(INLINE_MATH_RE.sub(repl, line))
    return out


def process(text):
    stats = {}
    lines = text.split('\n')
    lines = fix_math_escapes_in_lines(lines, stats)
    lines = fix_dangerous_lines(lines, stats)
    lines = fix_blank_lines_around_blocks(lines, stats)
    lines = fix_inline_math_padding(lines, stats)
    lines = fix_table_pipes_in_math(lines, stats)
    return '\n'.join(lines), stats


def expand_args(args):
    files = []
    for a in args:
        matches = glob.glob(a)
        files.extend(matches if matches else [a])
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='+', help='Markdown file(s) or glob pattern(s)')
    parser.add_argument('--check', action='store_true', help='Report only, do not write changes')
    args = parser.parse_args()

    files = expand_args(args.files)
    any_issues = False
    for fname in files:
        text, has_bom, uses_crlf = read_text(fname)
        new_text, stats = process(text)
        total = sum(stats.values())
        if total == 0:
            print(f"{fname}: OK")
            continue
        any_issues = True
        detail = ', '.join(f"{k}={v}" for k, v in stats.items())
        if args.check:
            print(f"{fname}: {total} issue(s) would be fixed ({detail})")
        else:
            write_text(fname, new_text, has_bom, uses_crlf)
            print(f"{fname}: fixed {total} issue(s) ({detail})")

    sys.exit(1 if (args.check and any_issues) else 0)


if __name__ == '__main__':
    main()
