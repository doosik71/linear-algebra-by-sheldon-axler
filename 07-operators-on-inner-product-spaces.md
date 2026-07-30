# 7장 내적공간 위의 연산자

내적공간과 관련된 가장 깊은 결과들은 이제 다룰 주제, 즉 내적공간 위의 선형사상과 연산자에 관한 것이다. 앞으로 보겠지만 수반의 성질을 이용하면 좋은 정리들을 증명할 수 있다.

매우 중요한 스펙트럼 정리는 실 내적공간 위의 자기수반 연산자와 복소 내적공간 위의 정규 연산자를 완전히 기술해 준다. 그 뒤 우리는 스펙트럼 정리를 사용해 양의 연산자와 유니터리 연산자를 이해하고, 이는 유니터리 행렬과 행렬분해로 이어진다. 스펙트럼 정리는 또한 널리 쓰이는 특이값분해로 이어지고, 특이값분해는 극분해로 이어진다.

이 책의 나머지 부분에서 가장 중요한 결과들은 유한차원에서만 성립한다. 따라서 이제부터는 $V$와 $W$가 유한차원이라고 가정한다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.
- $V$와 $W$는 $\mathbb{F}$ 위의 비영 유한차원 내적공간이다.

그림: 리비우의 시장 광장. 리비우는 국제 경계의 변화 때문에 여러 이름으로 불렸고 여러 나라에 속했던 도시이다. 1772년부터 1918년까지 이 도시는 오스트리아에 속했고 렘베르크라고 불렸다. 제1차 세계대전과 제2차 세계대전 사이에는 폴란드에 속했고 르부프라고 불렸다. 이 시기에 르부프의 수학자들, 특히 스테판 바나흐(1892-1945)와 그의 동료들은 해석학의 도구로 무한차원 벡터공간을 연구하는 현대 함수해석학의 기본 결과들을 발전시켰다. 제2차 세계대전 이후 리비우는 우크라이나에 속해 왔고, 우크라이나는 1991년 독립국이 되기 전까지 소련의 일부였다.

## 7A 자기수반 연산자와 정규 연산자

### 수반

**7.1 정의: 수반, $T^*$**

$T\in\mathcal{L}(V,W)$라고 하자. $T$의 **수반**은 모든 $v\in V$와 모든 $w\in W$에 대해

$$
\langle Tv,w\rangle=\langle v,T^*w\rangle
$$

를 만족하는 함수 $T^*:W\to V$이다.

선형대수에서 수반이라는 말은 다른 뜻으로 쓰이기도 한다. 다른 곳에서 그 뜻을 만나더라도, 여기서의 수반과는 관련이 없다는 점에 주의하라.

위 정의가 의미가 있는 이유를 보자. $T\in\mathcal{L}(V,W)$이고 $w\in W$를 고정하자. $v\in V$를 $\langle Tv,w\rangle$로 보내는 $V$ 위의 선형함수

$$
v\mapsto \langle Tv,w\rangle
$$

를 생각한다. 리스 표현정리(6.42)에 의해, 이 선형함수는 어떤 유일한 벡터와의 내적으로 표현된다. 그 유일한 벡터를 $T^*w$라고 부른다. 다시 말해 $T^*w$는 모든 $v\in V$에 대해

$$
\langle Tv,w\rangle=\langle v,T^*w\rangle
$$

를 만족하는 $V$의 유일한 벡터이다.

위 등식에서 왼쪽의 내적은 $W$에서의 내적이고, 오른쪽의 내적은 $V$에서의 내적이다. 그러나 두 내적 모두 같은 기호 $\langle\cdot,\cdot\rangle$로 나타낸다.

**7.2 예: $\mathbb{R}^3$에서 $\mathbb{R}^2$로 가는 선형사상의 수반**

$T:\mathbb{R}^3\to\mathbb{R}^2$를

$$
T(x_1,x_2,x_3)=(x_2+3x_3,2x_1)
$$

로 정의하자. $(x_1,x_2,x_3)\in\mathbb{R}^3$이고 $(y_1,y_2)\in\mathbb{R}^2$이면

$$
\begin{aligned}
\langle T(x_1,x_2,x_3),(y_1,y_2)\rangle
&=\langle (x_2+3x_3,2x_1),(y_1,y_2)\rangle\cr
&=x_2y_1+3x_3y_1+2x_1y_2\cr
&=\langle (x_1,x_2,x_3),(2y_2,y_1,3y_1)\rangle.
\end{aligned}
$$

따라서

$$
T^*(y_1,y_2)=(2y_2,y_1,3y_1).
$$

**7.3 예: 치역의 차원이 최대 $1$인 선형사상의 수반**

$u\in V$와 $x\in W$를 고정하자. $T\in\mathcal{L}(V,W)$를 각 $v\in V$에 대해

$$
Tv=\langle v,u\rangle x
$$

로 정의한다. $v\in V$와 $w\in W$이면

$$
\begin{aligned}
\langle Tv,w\rangle
&=\langle \langle v,u\rangle x,w\rangle\cr
&=\langle v,u\rangle\langle x,w\rangle\cr
&=\langle v,\langle w,x\rangle u\rangle.
\end{aligned}
$$

따라서

$$
T^*w=\langle w,x\rangle u.
$$

위 두 예와 아래 증명은 $T^*$를 계산할 때 흔히 쓰는 방법을 보여 준다. 먼저 $\langle Tv,w\rangle$의 식으로 시작한 뒤, 첫 번째 자리에 $v$만 남도록 식을 변형한다. 그러면 두 번째 자리에 남는 벡터가 $T^*w$이다.

**7.4 선형사상의 수반은 선형사상이다**

$T\in\mathcal{L}(V,W)$이면 $T^*\in\mathcal{L}(W,V)$이다.

**증명**

$v\in V$이고 $w_1,w_2\in W$이면

$$
\begin{aligned}
\langle Tv,w_1+w_2\rangle
&=\langle Tv,w_1\rangle+\langle Tv,w_2\rangle\cr
&=\langle v,T^*w_1\rangle+\langle v,T^*w_2\rangle\cr
&=\langle v,T^*w_1+T^*w_2\rangle.
\end{aligned}
$$

따라서 $T^*(w_1+w_2)=T^*w_1+T^*w_2$이다. 또한 $\lambda\in\mathbb{F}$이고 $w\in W$이면

$$
\begin{aligned}
\langle Tv,\lambda w\rangle
&=\overline{\lambda}\langle Tv,w\rangle\cr
&=\overline{\lambda}\langle v,T^*w\rangle\cr
&=\langle v,\lambda T^*w\rangle.
\end{aligned}
$$

따라서 $T^*(\lambda w)=\lambda T^*w$이다. 그러므로 $T^*$는 선형사상이다.

**7.5 수반의 성질**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) 모든 $S\in\mathcal{L}(V,W)$에 대해

$$
(S+T)^*=S^*+T^*.
$$

(b) 모든 $\lambda\in\mathbb{F}$에 대해

$$
(\lambda T)^*=\overline{\lambda}T^*.
$$

(c)

$$
(T^*)^*=T.
$$

(d) $U$가 $\mathbb{F}$ 위의 유한차원 내적공간이고 $S\in\mathcal{L}(W,U)$이면

$$
(ST)^*=T^*S^*.
$$

(e) $I$가 $V$ 위의 항등연산자이면

$$
I^*=I.
$$

(f) $T$가 가역이면 $T^*$도 가역이고

$$
(T^*)^{-1}=(T^{-1})^*.
$$

**증명**

$v\in V$와 $w\in W$를 잡는다. (a)는

$$
\langle (S+T)v,w\rangle
=\langle Sv,w\rangle+\langle Tv,w\rangle
=\langle v,S^*w+T^*w\rangle
$$

에서 따른다. (b)는

$$
\langle (\lambda T)v,w\rangle
=\lambda\langle Tv,w\rangle
=\lambda\langle v,T^*w\rangle
=\langle v,\overline{\lambda}T^*w\rangle
$$

에서 따른다. (c)는

$$
\langle T^*w,v\rangle
=\overline{\langle v,T^*w\rangle}
=\overline{\langle Tv,w\rangle}
=\langle w,Tv\rangle
$$

에서 따른다. (d)는 $u\in U$에 대해

$$
\langle (ST)v,u\rangle
=\langle S(Tv),u\rangle
=\langle Tv,S^*u\rangle
=\langle v,T^*(S^*u)\rangle
$$

에서 따른다. (e)는 $\langle Iu,v\rangle=\langle u,v\rangle$에서 따른다. (f)는 $T^{-1}T=I$와 $TT^{-1}=I$의 양변에 수반을 취하고 (d), (e)를 적용하면 된다.

$\mathbb{F}=\mathbb{R}$이면 위 결과의 (a), (b)에 의해 $T\mapsto T^*$는 $\mathcal{L}(V,W)$에서 $\mathcal{L}(W,V)$로 가는 선형사상이다. 그러나 $\mathbb{F}=\mathbb{C}$이면 (b)에 켤레복소수가 나타나므로 일반적으로 선형사상이 아니다.

**7.6 $T^*$의 영공간과 치역**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a)

$$
\text{null}T^*=(\text{range}T)^\perp.
$$

(b)

$$
\text{range}T^*=(\text{null}T)^\perp.
$$

(c)

$$
\text{null}T=(\text{range}T^*)^\perp.
$$

(d)

$$
\text{range}T=(\text{null}T^*)^\perp.
$$

**증명**

$w\in W$이면

$$
\begin{aligned}
w\in\text{null}T^*
&\Longleftrightarrow T^*w=0\cr
&\Longleftrightarrow \langle v,T^*w\rangle=0\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow \langle Tv,w\rangle=0\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow w\in(\text{range}T)^\perp.
\end{aligned}
$$

따라서 (a)가 성립한다. (a)의 양변에 직교여공간을 취하고 6.52를 사용하면 (d)가 나온다. (a)에서 $T$를 $T^*$로 바꾸고 7.5(c)를 사용하면 (c)가 나온다. 마지막으로 (d)에서 $T$를 $T^*$로 바꾸면 (b)가 나온다.

**7.7 정의: 켤레전치, $A^*$**

$m\times n$ 행렬 $A$의 **켤레전치**는 행과 열을 서로 바꾼 뒤 각 성분의 켤레복소수를 취하여 얻는 $n\times m$ 행렬 $A^*$이다. 즉 $j\in\lbrace1,\ldots,n\rbrace$이고 $k\in\lbrace1,\ldots,m\rbrace$이면

$$
(A^*)_{j,k}=\overline{A_{k,j}}.
$$

**7.8 예: $2\times 3$ 행렬의 켤레전치**

행렬의 모든 성분이 실수이면 $A^*=A^{\mathrm{t}}$이다. 여기서 $A^{\mathrm{t}}$는 행과 열을 바꿔 얻는 전치행렬이다.

다음 $2\times 3$ 행렬

$$
\begin{pmatrix}
2 & 3+4i & 7\cr
6 & 5 & 8i
\end{pmatrix}
$$

의 켤레전치는

$$
\begin{pmatrix}
2 & 6\cr
3-4i & 5\cr
7 & -8i
\end{pmatrix}
$$

이다.

수반은 기저 선택에 의존하지 않는다. 그래서 우리는 행렬의 전치나 켤레전치보다 선형사상의 수반을 강조하는 경우가 많다. 다음 결과는 $T$의 행렬로부터 $T^*$의 행렬을 계산하는 방법을 보여 준다. 주의할 점은, 정규직교기저가 아닌 기저에 대해서는 $T^*$의 행렬이 $T$의 행렬의 켤레전치와 반드시 같지 않다는 것이다.

**7.9 $T^*$의 행렬은 $T$의 행렬의 켤레전치이다**

$T\in\mathcal{L}(V,W)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $f_1,\ldots,f_m$이 $W$의 정규직교기저이면

$$
\mathcal{M}(T^*,(f_1,\ldots,f_m),(e_1,\ldots,e_n))
$$

은

$$
\mathcal{M}(T,(e_1,\ldots,e_n),(f_1,\ldots,f_m))
$$

의 켤레전치이다. 간단히 쓰면

$$
\mathcal{M}(T^*)=(\mathcal{M}(T))^*.
$$

**증명**

$T e_k$를 $f_1,\ldots,f_m$의 선형결합으로 쓰면

$$
T e_k=\langle T e_k,f_1\rangle f_1+\cdots+\langle T e_k,f_m\rangle f_m.
$$

따라서 $\mathcal{M}(T)$의 $j$행 $k$열 성분은 $\langle T e_k,f_j\rangle$이다. 같은 말을 $T^*$에 적용하면 $\mathcal{M}(T^*)$의 $j$행 $k$열 성분은

$$
\langle T^*f_k,e_j\rangle
=\langle f_k,T e_j\rangle
=\overline{\langle T e_j,f_k\rangle}
$$

이다. 이는 $\mathcal{M}(T)$의 $k$행 $j$열 성분의 켤레복소수이므로 원하는 결론이 따른다.

리스 표현정리(6.58)는 $V$와 쌍대공간 $V'$의 동일시를 제공한다. 이 동일시 아래에서 $U\subset V$의 직교여공간 $U^\perp$는 $U$의 소멸자 $U^0$에 대응한다. 또한 내적공간에서는 직교여공간과 수반을 다루는 것이 소멸자와 쌍대사상보다 더 쉽기 때문에, 보통 소멸자와 쌍대사상을 직접 사용할 필요가 없다. 연습문제 32번에서는 $V$와 $V'$, $W$와 $W'$를 표준적으로 동일시하면 수반사상 $T^*:W\to V$가 쌍대사상 $T':W'\to V'$에 대응함을 확인한다.

### 자기수반 연산자

이제 내적공간 위의 연산자에 집중한다. 즉 $V$에서 $V$로 가는 선형사상을 다룬다.

**7.10 정의: 자기수반**

연산자 $T\in\mathcal{L}(V)$가

$$
T=T^*
$$

를 만족하면 $T$를 **자기수반**이라고 한다.

$e_1,\ldots,e_n$이 $V$의 정규직교기저이면 7.9에 의해 $T$가 자기수반인 것은

$$
\mathcal{M}(T,(e_1,\ldots,e_n))=\mathcal{M}(T,(e_1,\ldots,e_n))^*
$$

인 것과 동치이다.

**7.11 예: 행렬로 자기수반성 판정하기**

$c\in\mathbb{F}$이고 $T$가 표준기저에 대한 행렬

$$
\mathcal{M}(T)=
\begin{pmatrix}
2 & c\cr
3 & 7
\end{pmatrix}
$$

을 가지는 $\mathbb{F}^2$ 위의 연산자라고 하자. 그러면

$$
\mathcal{M}(T^*)=
\begin{pmatrix}
2 & 3\cr
\overline{c} & 7
\end{pmatrix}.
$$

따라서 $\mathcal{M}(T)=\mathcal{M}(T^*)$인 것은 $c=3$인 것과 동치이다. 그러므로 $T$는 $c=3$일 때 그리고 그때에만 자기수반이다.

$\mathcal{L}(V)$에서 수반은 $\mathbb{C}$에서 켤레복소수와 비슷한 역할을 한다. 복소수 $z$가 실수인 것은 $z=\overline z$인 것과 동치이다. 따라서 자기수반 연산자 $T=T^*$는 실수에 대응되는 개념이라고 생각할 수 있다.

$T\in\mathcal{L}(V)$가 자기수반인 것은 모든 $v,w\in V$에 대해

$$
\langle Tv,w\rangle=\langle v,Tw\rangle
$$

가 성립하는 것과 동치이다.

**7.12 자기수반 연산자의 고윳값**

자기수반 연산자의 모든 고윳값은 실수이다.

**증명**

$T$가 $V$ 위의 자기수반 연산자라고 하자. $\lambda$가 $T$의 고윳값이고 $v\ne 0$인 벡터가 $Tv=\lambda v$를 만족한다고 하자. 그러면

$$
\lambda\Vert v\Vert^2
=\langle \lambda v,v\rangle
=\langle Tv,v\rangle
=\langle v,Tv\rangle
=\langle v,\lambda v\rangle
=\overline{\lambda}\Vert v\Vert^2.
$$

따라서 $\lambda=\overline{\lambda}$이고, $\lambda$는 실수이다.

**7.13 모든 $v$에 대해 $Tv$가 $v$에 직교하면 $T=0$이다, 복소수의 경우**

$V$가 복소 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 그러면

$$
\langle Tv,v\rangle=0\quad\text{모든 }v\in V\text{에 대해}
$$

인 것과 $T=0$인 것은 동치이다.

**증명**

$u,w\in V$이면 오른쪽을 전개하여 확인할 수 있는 다음 등식이 성립한다.

$$
\begin{aligned}
\langle Tu,w\rangle
&=\frac14\Big(\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle\cr
&\quad+i\langle T(u+iw),u+iw\rangle-i\langle T(u-iw),u-iw\rangle\Big).
\end{aligned}
$$

오른쪽의 각 항은 적절한 $v\in V$에 대해 $\langle Tv,v\rangle$ 꼴이다. 이제 모든 $v\in V$에 대해 $\langle Tv,v\rangle=0$이라고 하자. 그러면 위 등식에 의해 모든 $u,w\in V$에 대해 $\langle Tu,w\rangle=0$이다. 특히 $w=Tu$로 두면 $Tu=0$이다. 따라서 $T=0$이다.

실수 내적공간에서는 이 결과가 거짓이다. 예를 들어 $\mathbb{R}^2$에서 원점 중심의 $90^\circ$ 반시계방향 회전 $T(x,y)=(-y,x)$는 모든 $v$에 대해 $Tv$가 $v$에 직교하지만 $T\ne 0$이다.

**7.14 모든 $v$에 대해 $\langle Tv,v\rangle$가 실수인 것과 자기수반성, 복소수의 경우**

$V$가 복소 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 그러면

$$
T\text{가 자기수반}
\Longleftrightarrow
\langle Tv,v\rangle\in\mathbb{R}\quad\text{모든 }v\in V\text{에 대해}.
$$

**증명**

$v\in V$이면

$$
\langle T^*v,v\rangle
=\overline{\langle v,T^*v\rangle}
=\overline{\langle Tv,v\rangle}.
\tag{7.15}
$$

따라서

$$
\begin{aligned}
T\text{가 자기수반}
&\Longleftrightarrow T-T^*=0\cr
&\Longleftrightarrow \langle (T-T^*)v,v\rangle=0\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow \langle Tv,v\rangle-\overline{\langle Tv,v\rangle}=0\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow \langle Tv,v\rangle\in\mathbb{R}\quad\text{모든 }v\in V\text{에 대해}.
\end{aligned}
$$

두 번째 동치는 7.13을 $T-T^*$에 적용한 것이고, 세 번째 동치는 (7.15)에서 따른다.

**7.16 자기수반이고 모든 $v$에 대해 $\langle Tv,v\rangle=0$이면 $T=0$**

$T$가 $V$ 위의 자기수반 연산자라고 하자. 그러면

$$
\langle Tv,v\rangle=0\quad\text{모든 }v\in V\text{에 대해}
$$

인 것과 $T=0$인 것은 동치이다.

**증명**

$V$가 복소 내적공간인 경우에는 7.13에서 이미 증명했다. 따라서 $V$가 실 내적공간이라고 하자. $u,w\in V$이면

$$
\langle Tu,w\rangle
=\frac{\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle}{4}.
\tag{7.17}
$$

이는 오른쪽을 전개하고, $T$가 자기수반이며 실 내적공간에서는 $\langle Tw,u\rangle=\langle Tu,w\rangle$임을 사용하면 확인된다. 모든 $v\in V$에 대해 $\langle Tv,v\rangle=0$이면 (7.17)의 오른쪽 항들이 모두 $0$이므로 모든 $u,w\in V$에 대해 $\langle Tu,w\rangle=0$이다. 다시 $w=Tu$로 두면 $Tu=0$이므로 $T=0$이다.

### 정규 연산자

**7.18 정의: 정규**

- 내적공간 위의 연산자가 자기 자신의 수반과 교환하면 그 연산자를 **정규**라고 한다.
- 즉 $T\in\mathcal{L}(V)$가 정규라는 것은

$$
TT^*=T^*T
$$

라는 뜻이다.

모든 자기수반 연산자는 정규이다. 실제로 $T$가 자기수반이면 $T^*=T$이므로 $T$는 $T^*$와 교환한다.

**7.19 예: 정규이지만 자기수반이 아닌 연산자**

$T$를 표준기저에 대한 행렬이

$$
\begin{pmatrix}
2 & -3\cr
3 & 2
\end{pmatrix}
$$

인 $\mathbb{F}^2$ 위의 연산자라고 하자. 즉

$$
T(w,z)=(2w-3z,3w+2z).
$$

이 연산자는 자기수반이 아니다. 행렬의 $2$행 $1$열 성분은 $3$이지만 $1$행 $2$열 성분의 켤레복소수는 $-3$이기 때문이다.

한편

$$
\begin{pmatrix} 2 & -3\cr 3 & 2 \end{pmatrix}
\begin{pmatrix} 2 & 3\cr -3 & 2 \end{pmatrix} =
\begin{pmatrix} 13 & 0\cr 0 & 13 \end{pmatrix}
$$

이고

$$
\begin{pmatrix} 2 & 3\cr -3 & 2 \end{pmatrix}
\begin{pmatrix} 2 & -3\cr 3 & 2 \end{pmatrix} =
\begin{pmatrix} 13 & 0\cr 0 & 13 \end{pmatrix}.
$$

따라서 $TT^*=T^*T$이고 $T$는 정규이다.

**7.20 $T$가 정규인 것과 $Tv$, $T^*v$의 노름이 같은 것**

$T\in\mathcal{L}(V)$라고 하자. 그러면

$$
T\text{가 정규}
\Longleftrightarrow
\Vert Tv\Vert=\Vert T^*v\Vert\quad\text{모든 }v\in V\text{에 대해}.
$$

**증명**

우리는

$$
\begin{aligned}
T\text{가 정규}
&\Longleftrightarrow T^*T-TT^*=0\cr
&\Longleftrightarrow \langle (T^*T-TT^*)v,v\rangle=0\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow \langle Tv,Tv\rangle=\langle T^*v,T^*v\rangle\quad\text{모든 }v\in V\text{에 대해}\cr
&\Longleftrightarrow \Vert Tv\Vert=\Vert T^*v\Vert\quad\text{모든 }v\in V\text{에 대해}
\end{aligned}
$$

를 얻는다. 두 번째 동치는 $T^*T-TT^*$가 자기수반이라는 사실과 7.16에서 따른다.

**7.21 정규 연산자의 치역, 영공간, 고유벡터**

$T\in\mathcal{L}(V)$가 정규라고 하자. 그러면 다음이 성립한다.

(a)

$$
\text{null}T=\text{null}T^*.
$$

(b)

$$
\text{range}T=\text{range}T^*.
$$

(c)

$$
V=\text{null}T\oplus\text{range}T.
$$

(d) 모든 $\lambda\in\mathbb{F}$에 대해 $T-\lambda I$는 정규이다.

(e) $v\in V$와 $\lambda\in\mathbb{F}$에 대해

$$
Tv=\lambda v
\Longleftrightarrow
T^*v=\overline{\lambda}v.
$$

**증명**

(a) $v\in V$이면 7.20에 의해

$$
v\in\text{null}T
\Longleftrightarrow
\Vert Tv\Vert=0
\Longleftrightarrow
\Vert T^*v\Vert=0
\Longleftrightarrow
v\in\text{null}T^*.
$$

(b)는

$$
\text{range}T
=(\text{null}T^*)^\perp
=(\text{null}T)^\perp
=\text{range}T^*
$$

에서 따른다. 여기서 첫 번째 등식은 7.6(d), 두 번째 등식은 (a), 세 번째 등식은 7.6(b)를 사용했다.

(c)는

$$
V=\text{null}T\oplus(\text{null}T)^\perp
=\text{null}T\oplus\text{range}T^*
=\text{null}T\oplus\text{range}T
$$

에서 따른다.

(d) $\lambda\in\mathbb{F}$이면

$$
\begin{aligned}
(T-\lambda I)(T-\lambda I)^*
&=(T-\lambda I)(T^*-\overline{\lambda}I)\cr
&=TT^*-\overline{\lambda}T-\lambda T^*+|\lambda|^2I\cr
&=T^*T-\overline{\lambda}T-\lambda T^*+|\lambda|^2I\cr
&=(T^*-\overline{\lambda}I)(T-\lambda I)\cr
&=(T-\lambda I)^*(T-\lambda I).
\end{aligned}
$$

따라서 $T-\lambda I$는 정규이다.

(e)는 (d)와 7.20을 $T-\lambda I$에 적용하면 나온다. 실제로

$$
\Vert(T-\lambda I)v\Vert
=\Vert(T-\lambda I)^*v\Vert
=\Vert(T^*-\overline{\lambda}I)v\Vert.
$$

따라서 한쪽이 $0$인 것과 다른 쪽이 $0$인 것이 동치이다.

**7.22 정규 연산자의 서로 다른 고윳값에 대응하는 고유벡터는 직교한다**

$T\in\mathcal{L}(V)$가 정규라고 하자. 그러면 $T$의 서로 다른 고윳값에 대응하는 고유벡터들은 서로 직교한다.

**증명**

$\alpha,\beta$가 $T$의 서로 다른 고윳값이고, 대응하는 고유벡터를 각각 $u,v$라고 하자. 그러면 $Tu=\alpha u$이고 $Tv=\beta v$이다. 7.21(e)에 의해 $T^*v=\overline{\beta}v$이다. 따라서

$$
\begin{aligned}
(\alpha-\beta)\langle u,v\rangle
&=\langle \alpha u,v\rangle-\langle u,\overline{\beta}v\rangle\cr
&=\langle Tu,v\rangle-\langle u,T^*v\rangle\cr
&=0.
\end{aligned}
$$

$\alpha\ne\beta$이므로 $\langle u,v\rangle=0$이다.

**7.23 $T$가 정규인 것과 $T$의 실수부와 허수부가 교환하는 것**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$가 정규인 것과, 서로 교환하는 자기수반 연산자 $A,B$가 존재하여

$$
T=A+iB
$$

가 되는 것은 동치이다.

**증명**

먼저 $T$가 정규라고 하자. 다음과 같이 둔다.

$$
A=\frac{T+T^*}{2},\qquad
B=\frac{T-T^*}{2i}.
\tag{7.24}
$$

그러면 $A$와 $B$는 자기수반이고 $T=A+iB$이다. 간단한 계산으로

$$
AB-BA=\frac{T^*T-TT^*}{2i}
\tag{7.25}
$$

를 얻는다. $T$가 정규이므로 오른쪽은 $0$이고, 따라서 $A$와 $B$는 교환한다.

반대로 서로 교환하는 자기수반 연산자 $A,B$가 존재하여 $T=A+iB$라고 하자. 그러면 $T^*=A-iB$이다. 이 두 식을 더하고 빼면 (7.24)를 얻고, 따라서 (7.25)가 성립한다. $A$와 $B$가 교환하므로 (7.25)에 의해 $T^*T=TT^*$이다. 즉 $T$는 정규이다.

### 연습문제 7A

1. $n$이 양의 정수라고 하자. $T\in\mathcal{L}(\mathbb{F}^n)$을

   $$
   T(z_1,\ldots,z_n)=(0,z_1,\ldots,z_{n-1})
   $$

   로 정의한다. $T^*(z_1,\ldots,z_n)$의 공식을 구하여라.

2. $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

   $$
   T=0\Longleftrightarrow T^*=0\Longleftrightarrow T^*T=0\Longleftrightarrow TT^*=0.
   $$

3. $T\in\mathcal{L}(V)$이고 $\lambda\in\mathbb{F}$라고 하자. 다음을 증명하여라.

   $$
   \lambda\text{가 }T\text{의 고윳값}
   \Longleftrightarrow
   \overline{\lambda}\text{가 }T^*\text{의 고윳값}.
   $$

4. $T\in\mathcal{L}(V)$이고 $U$가 $V$의 부분공간이라고 하자. 다음을 증명하여라.

   $$
   U\text{가 }T\text{에 대해 불변}
   \Longleftrightarrow
   U^\perp\text{가 }T^*\text{에 대해 불변}.
   $$

5. $T\in\mathcal{L}(V,W)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $f_1,\ldots,f_m$이 $W$의 정규직교기저라고 하자. 다음을 증명하여라.

   $$
   \Vert Te_1\Vert^2+\cdots+\Vert Te_n\Vert^2
   =\Vert T^*f_1\Vert^2+\cdots+\Vert T^*f_m\Vert^2.
   $$

   위 등식의 왼쪽 각 항은 정규직교기저 $e_1,\ldots,e_n$에 의존하지만, 오른쪽은 이 기저에 의존하지 않는다. 따라서 왼쪽의 합은 어떤 정규직교기저를 사용하더라도 같음을 알 수 있다.

6. $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

   (a) $T$가 단사인 것과 $T^*$가 전사인 것은 동치이다.

   (b) $T$가 전사인 것과 $T^*$가 단사인 것은 동치이다.

7. $T\in\mathcal{L}(V,W)$이면 다음을 증명하여라.

   (a)

   $$
   \dim\text{null}T^*
   =\dim\text{null}T+\dim W-\dim V.
   $$

   (b)

   $$
   \dim\text{range}T^*=\dim\text{range}T.
   $$

8. $A$가 $\mathbb{F}$의 성분을 가진 $m\times n$ 행렬이라고 하자. 연습문제 7번의 (b)를 사용하여 $A$의 행랭크와 열랭크가 같음을 증명하여라.

   이 연습문제는 3.57과 3.133에서 이미 증명한 결과에 대한 또 하나의 대안적 증명을 요구한다.

9. $V$ 위의 두 자기수반 연산자의 곱이 자기수반인 것은 그 두 연산자가 교환하는 것과 동치임을 증명하여라.

10. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 자기수반인 것과 모든 $v\in V$에 대해

    $$
    \langle Tv,v\rangle=\langle T^*v,v\rangle
    $$

    가 성립하는 것은 동치임을 증명하여라.

11. $S:\mathbb{F}^2\to\mathbb{F}^2$를 $S(w,z)=(-z,w)$로 정의한다.

    (a) $S^*$의 공식을 구하여라.

    (b) $S$가 정규이지만 자기수반은 아님을 보여라.

    (c) $S$의 모든 고윳값을 구하여라.

    $\mathbb{F}=\mathbb{R}$이면 $S$는 $\mathbb{R}^2$에서 $90^\circ$ 반시계방향 회전이다.

12. 연산자 $B\in\mathcal{L}(V)$가

    $$
    B^*=-B
    $$

    를 만족하면 $B$를 **반자기수반**이라고 하자. $T\in\mathcal{L}(V)$라고 하자. $T$가 정규인 것과, 서로 교환하는 연산자 $A,B$가 존재하여 $A$는 자기수반이고 $B$는 반자기수반이며 $T=A+B$가 되는 것은 동치임을 증명하여라.

13. $\mathbb{F}=\mathbb{R}$이라고 하자. $\mathcal{A}\in\mathcal{L}(\mathcal{L}(V))$를 모든 $T\in\mathcal{L}(V)$에 대해 $\mathcal{A}T=T^*$로 정의한다.

    (a) $\mathcal{A}$의 모든 고윳값을 구하여라.

    (b) $\mathcal{A}$의 최소다항식을 구하여라.

14. $\mathcal{P}_2(\mathbb{R})$ 위에 내적

    $$
    \langle p,q\rangle=\int_0^1 pq
    $$

    를 정의한다. $T\in\mathcal{L}(\mathcal{P}_2(\mathbb{R}))$를

    $$
    T(ax^2+bx+c)=bx
    $$

    로 정의한다.

    (a) 이 내적에서 $T$가 자기수반이 아님을 보여라.

    (b) 기저 $1,x,x^2$에 대한 $T$의 행렬은

    $$
    \begin{pmatrix}
    0 & 0 & 0\cr
    0 & 1 & 0\cr
    0 & 0 & 0
    \end{pmatrix}
    $$

    이다. 이 행렬은 자신의 켤레전치와 같지만 $T$는 자기수반이 아니다. 왜 모순이 아닌지 설명하여라.

15. $T\in\mathcal{L}(V)$가 가역이라고 하자. 다음을 증명하여라.

    (a) $T$가 자기수반인 것과 $T^{-1}$이 자기수반인 것은 동치이다.

    (b) $T$가 정규인 것과 $T^{-1}$이 정규인 것은 동치이다.

16. $\mathbb{F}=\mathbb{R}$이라고 하자.

    (a) $V$ 위의 자기수반 연산자들의 집합이 $\mathcal{L}(V)$의 부분공간임을 보여라.

    (b) (a)의 부분공간의 차원을 $\dim V$로 나타내어 구하여라.

17. $\mathbb{F}=\mathbb{C}$라고 하자. $V$ 위의 자기수반 연산자들의 집합은 $\mathcal{L}(V)$의 부분공간이 아님을 보여라.

18. $\dim V\ge 2$라고 하자. $V$ 위의 정규 연산자들의 집합은 $\mathcal{L}(V)$의 부분공간이 아님을 보여라.

19. $T\in\mathcal{L}(V)$이고 모든 $v\in V$에 대해 $\Vert T^*v\Vert\le\Vert Tv\Vert$라고 하자. $T$가 정규임을 증명하여라.

    이 연습문제는 무한차원 내적공간에서는 실패하며, 이와 관련해 **하이포정규 연산자**라는 잘 발전된 이론이 생긴다.

20. $P\in\mathcal{L}(V)$가 $P^2=P$를 만족한다고 하자. 다음 조건들이 서로 동치임을 증명하여라.

    (a) $P$는 자기수반이다.

    (b) $P$는 정규이다.

    (c) 어떤 $V$의 부분공간 $U$가 존재하여 $P=P_U$이다.

21. $D:\mathcal{P}_8(\mathbb{R})\to\mathcal{P}_8(\mathbb{R})$가 $Dp=p'$로 정의되는 미분 연산자라고 하자. $D$를 정규 연산자로 만드는 $\mathcal{P}_8(\mathbb{R})$ 위의 내적은 존재하지 않음을 증명하여라.

22. $T$가 정규이지만 자기수반은 아닌 $T\in\mathcal{L}(\mathbb{R}^3)$의 예를 제시하여라.

23. $T$가 $V$ 위의 정규 연산자라고 하자. 또한 $v,w\in V$가

    $$
    \Vert v\Vert=\Vert w\Vert=2,\qquad Tv=3v,\qquad Tw=4w
    $$

    를 만족한다고 하자. $\Vert T(v+w)\Vert=10$임을 보여라.

24. $T\in\mathcal{L}(V)$이고

    $$
    a_0+a_1z+a_2z^2+\cdots+a_{m-1}z^{m-1}+z^m
    $$

    이 $T$의 최소다항식이라고 하자. $T^*$의 최소다항식은

    $$
    \overline{a_0}+\overline{a_1}z+\overline{a_2}z^2+\cdots+\overline{a_{m-1}}z^{m-1}+z^m
    $$

    임을 증명하여라. 이 연습문제는 $\mathbb{F}=\mathbb{R}$이면 $T^*$의 최소다항식이 $T$의 최소다항식과 같음을 보여 준다.

25. $T\in\mathcal{L}(V)$라고 하자. $T$가 대각화가능인 것과 $T^*$가 대각화가능인 것은 동치임을 증명하여라.

26. $u,x\in V$를 고정한다. $T\in\mathcal{L}(V)$를 모든 $v\in V$에 대해 $Tv=\langle v,u\rangle x$로 정의한다.

    (a) $V$가 실 벡터공간이면 $T$가 자기수반인 것과 리스트 $u,x$가 일차종속인 것은 동치임을 증명하여라.

    (b) $T$가 정규인 것과 리스트 $u,x$가 일차종속인 것은 동치임을 증명하여라.

27. $T\in\mathcal{L}(V)$가 정규라고 하자. 모든 양의 정수 $k$에 대해

    $$
    \text{null}T^k=\text{null}T,
    \qquad
    \text{range}T^k=\text{range}T
    $$

    임을 증명하여라.

28. $T\in\mathcal{L}(V)$가 정규라고 하자. $\lambda\in\mathbb{F}$이면 $T$의 최소다항식은 $(x-\lambda)^2$의 다항식배가 아님을 증명하여라.

29. 증명하거나 반례를 들어라. $T\in\mathcal{L}(V)$이고 $V$의 정규직교기저 $e_1,\ldots,e_n$이 존재하여 각 $k=1,\ldots,n$에 대해 $\Vert Te_k\Vert=\Vert T^*e_k\Vert$이면 $T$는 정규이다.

30. $T\in\mathcal{L}(\mathbb{F}^3)$가 정규이고 $T(1,1,1)=(2,2,2)$라고 하자. $(z_1,z_2,z_3)\in\text{null}T$이면 $z_1+z_2+z_3=0$임을 증명하여라.

31. $n$을 양의 정수로 고정한다. 실숫값 연속함수들의 내적공간 $C[-\pi,\pi]$에 내적 $\langle f,g\rangle=\int_{-\pi}^{\pi}fg$가 주어져 있다고 하자. 다음 부분공간을 생각한다.

    $$
    V=\text{span}(1,\cos x,\cos 2x,\ldots,\cos nx,\sin x,\sin 2x,\ldots,\sin nx).
    $$

    (a) $D\in\mathcal{L}(V)$를 $Df=f'$로 정의한다. $D^*=-D$임을 보여라. 따라서 $D$가 정규이지만 자기수반은 아님을 결론지어라.

    (b) $T\in\mathcal{L}(V)$를 $Tf=f''$로 정의한다. $T$가 자기수반임을 보여라.

32. $T:V\to W$가 선형사상이라고 하자. $V$와 $V'$의 표준적 동일시(6.58)와 $W$와 $W'$의 대응되는 동일시 아래에서, 수반사상 $T^*:W\to V$가 쌍대사상 $T':W'\to V'$에 대응함을 보여라. 더 정확히 말해, 모든 $w\in W$에 대해

    $$
    T'(\varphi_w)=\varphi_{T^*w}
    $$

    임을 보여라. 여기서 $\varphi_w$와 $\varphi_{T^*w}$는 6.58에서처럼 정의된다.

## 7B 스펙트럼 정리

대각행렬은 대각선 위를 제외한 모든 성분이 $0$인 정사각행렬이다. $V$ 위의 연산자가 $V$의 어떤 기저에 대해 대각행렬을 가지면 그 연산자를 대각화가능이라고 불렀다. 이는 그 연산자의 고유벡터들로 이루어진 $V$의 기저가 존재한다는 것과 동치이다(5.55).

$V$ 위에서 가장 좋은 연산자는 어떤 정규직교기저에 대해 대각행렬을 가지는 연산자이다. 이는 $T$의 고유벡터들로 이루어진 $V$의 정규직교기저가 존재한다는 말과 같다. 이 절의 목표는 스펙트럼 정리를 증명하는 것이다. 스펙트럼 정리는 $\mathbb{F}=\mathbb{R}$일 때 이런 연산자가 정확히 자기수반 연산자이고, $\mathbb{F}=\mathbb{C}$일 때 이런 연산자가 정확히 정규 연산자임을 말한다.

스펙트럼 정리는 내적공간 위의 연산자를 연구할 때 아마도 가장 유용한 도구이다. 특정 무한차원 내적공간으로의 확장은 함수해석학에서 중요한 역할을 한다.

### 실 스펙트럼 정리

실 스펙트럼 정리를 증명하려면 두 가지 준비 결과가 필요하다. 이 결과들은 실 내적공간과 복소 내적공간 모두에서 성립하지만, 복소 스펙트럼 정리의 증명에는 필요하지 않다.

완전제곱을 떠올려 보자. $b,c\in\mathbb{R}$이고 $b^2<4c$이면 모든 실수 $x$에 대해

$$
x^2+bx+c=\left(x+\frac b2\right)^2+\left(c-\frac{b^2}{4}\right)>0.
$$

따라서 $x^2+bx+c$는 $0$이 아니다. 실수 $x$를 자기수반 연산자로 바꾸면 다음 결과에 이른다.

**7.26 가역인 이차식**

$T\in\mathcal{L}(V)$가 자기수반이고 $b,c\in\mathbb{R}$가 $b^2<4c$를 만족한다고 하자. 그러면

$$
T^2+bT+cI
$$

는 가역 연산자이다.

**증명**

$v$를 $V$의 영이 아닌 벡터라고 하자. 그러면

$$
\begin{aligned}
\langle (T^2+bT+cI)v,v\rangle
&=\langle T^2v,v\rangle+b\langle Tv,v\rangle+c\langle v,v\rangle\cr
&=\langle Tv,Tv\rangle+b\langle Tv,v\rangle+c\Vert v\Vert^2\cr
&\ge \Vert Tv\Vert^2-|b|\Vert Tv\Vert\thinspace\Vert v\Vert+c\Vert v\Vert^2\cr
&=\left(\Vert Tv\Vert-\frac{|b|\Vert v\Vert}{2}\right)^2+\left(c-\frac{b^2}{4}\right)\Vert v\Vert^2\cr
&>0.
\end{aligned}
$$

세 번째 줄은 코시-슈바르츠 부등식(6.14)에서 따른다. 마지막 부등식은 $(T^2+bT+cI)v\ne 0$임을 뜻한다. 따라서 $T^2+bT+cI$는 단사이고, 유한차원에서 단사 연산자는 가역이다(3.65).

**7.27 자기수반 연산자의 최소다항식**

$T\in\mathcal{L}(V)$가 자기수반이라고 하자. 그러면 $T$의 최소다항식은 어떤 $\lambda_1,\ldots,\lambda_m\in\mathbb{R}$에 대해

$$
(z-\lambda_1)\cdots(z-\lambda_m)
$$

와 같다.

**증명**

먼저 $\mathbb{F}=\mathbb{C}$라고 하자. $T$의 최소다항식의 영점들은 $T$의 고윳값이다[5.27(a)]. 자기수반 연산자의 모든 고윳값은 실수이다(7.12). 따라서 대수학의 기본정리의 두 번째 버전(4.13)에 의해 최소다항식은 원하는 꼴이다.

이제 $\mathbb{F}=\mathbb{R}$이라고 하자. 실수체 위의 다항식 분해(4.16)에 의해 $T$의 최소다항식은 어떤 $\lambda_1,\ldots,\lambda_m\in\mathbb{R}$와 $b_1,\ldots,b_N,c_1,\ldots,c_N\in\mathbb{R}$에 대해, 각 $k$마다 $b_k^2<4c_k$를 만족하면서 다음 꼴로 쓸 수 있다.

$$
(z-\lambda_1)\cdots(z-\lambda_m)
(z^2+b_1z+c_1)\cdots(z^2+b_Nz+c_N).
\tag{7.28}
$$

여기서 $m=0$ 또는 $N=0$일 수도 있으며, 이는 해당 꼴의 인수가 없다는 뜻이다. 이 다항식을 $T$에 대입하면 $0$이 된다. 만약 $N>0$이면 7.26에 의해 마지막 이차식 $T^2+b_NT+c_NI$가 가역이므로, 양변 오른쪽에 그 역을 곱해 차수가 $2$ 낮은 소거다항식을 얻는다. 이는 최소다항식의 최소성에 모순이다. 따라서 $N=0$이어야 하고, 최소다항식은 원하는 일차식들의 곱이다.

**7.29 실 스펙트럼 정리**

$\mathbb{F}=\mathbb{R}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $T$는 자기수반이다.

(b) $T$는 $V$의 어떤 정규직교기저에 대해 대각행렬을 가진다.

(c) $V$는 $T$의 고유벡터들로 이루어진 정규직교기저를 가진다.

**증명**

먼저 $T$가 자기수반이라고 하자. 6.37과 7.27에 의해 $T$는 $V$의 어떤 정규직교기저에 대해 상삼각 행렬을 가진다. 이 정규직교기저에 대해 $T^*$의 행렬은 $T$의 행렬의 전치이다. 그런데 $T^*=T$이므로 $T$의 행렬은 자신의 전치와 같다. 상삼각 행렬이면서 자신의 전치와 같으려면 대각선 밖의 모든 성분이 $0$이어야 한다. 따라서 $T$는 이 정규직교기저에 대해 대각행렬을 가진다.

반대로 $T$가 어떤 정규직교기저에 대해 대각행렬을 가진다고 하자. 그 대각행렬은 자신의 전치와 같으므로, 같은 기저에 대해 $T^*$의 행렬과 $T$의 행렬이 같다. 따라서 $T^*=T$이다.

(b)와 (c)의 동치는 정의에서 바로 따르며, 5.55의 증명에서도 볼 수 있다.

**7.30 예: 한 연산자의 고유벡터들로 이루어진 정규직교기저**

표준기저에 대한 행렬이

$$
\begin{pmatrix}
14 & -13 & 8\cr
-13 & 14 & 8\cr
8 & 8 & -7
\end{pmatrix}
$$

인 $\mathbb{R}^3$ 위의 연산자 $T$를 생각하자. 이 실수 행렬은 자신의 전치와 같으므로 $T$는 자기수반이다. 직접 확인하면

$$
\frac{(1,-1,0)}{\sqrt2},\qquad
\frac{(1,1,1)}{\sqrt3},\qquad
\frac{(1,1,-2)}{\sqrt6}
$$

는 $T$의 고유벡터들로 이루어진 $\mathbb{R}^3$의 정규직교기저이다. 이 기저에 대한 $T$의 행렬은 대각행렬

$$
\begin{pmatrix}
27 & 0 & 0\cr
0 & 9 & 0\cr
0 & 0 & -15
\end{pmatrix}
$$

이다.

연습문제 17번에서는 하나의 연산자가 아니라 여러 연산자에 동시에 적용되는 실 스펙트럼 정리의 버전을 보게 된다.

### 복소 스펙트럼 정리

다음 결과는 복소 내적공간 위의 정규 연산자를 완전히 기술한다.

**7.31 복소 스펙트럼 정리**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $T$는 정규이다.

(b) $T$는 $V$의 어떤 정규직교기저에 대해 대각행렬을 가진다.

(c) $V$는 $T$의 고유벡터들로 이루어진 정규직교기저를 가진다.

**증명**

먼저 $T$가 정규라고 하자. 슈어 정리(6.38)에 의해, 어떤 정규직교기저 $e_1,\ldots,e_n$에 대해 $T$의 행렬은 상삼각이다. 즉

$$
\mathcal{M}(T,(e_1,\ldots,e_n)) =
\begin{pmatrix}
a_{1,1} & \cdots & a_{1,n}\cr
& \ddots & \vdots\cr
0 & & a_{n,n}
\end{pmatrix}.
\tag{7.32}
$$

이 행렬이 사실 대각행렬임을 보이자. 위 행렬에서

$$
\Vert Te_1\Vert^2=|a_{1,1}|^2
$$

이고

$$
\Vert T^*e_1\Vert^2=|a_{1,1}|^2+|a_{1,2}|^2+\cdots+|a_{1,n}|^2
$$

이다. $T$가 정규이므로 7.20에 의해 두 노름은 같다. 따라서 첫 번째 행에서 대각성분을 제외한 모든 성분은 $0$이다. 같은 논리를 $e_2,e_3,\ldots$에 차례로 적용하면 모든 비대각 성분이 $0$임을 얻는다. 따라서 $T$의 행렬은 대각행렬이다.

반대로 $T$가 어떤 정규직교기저에 대해 대각행렬을 가진다고 하자. 같은 기저에 대한 $T^*$의 행렬은 $T$의 행렬의 켤레전치이므로 역시 대각행렬이다. 두 대각행렬은 서로 교환하므로 $T$와 $T^*$도 교환한다. 따라서 $T$는 정규이다.

(b)와 (c)의 동치는 정의에서 따른다(또는 5.55를 보라).

연습문제 13번과 20번은 위 결과에서 (a)가 (b)를 함의한다는 사실의 다른 증명을 제공한다. 연습문제 14번과 15번은 실 스펙트럼 정리와 복소 스펙트럼 정리를 고유공간들의 직교직합으로 해석한다. 연습문제 16번은 여러 정규 연산자에 동시에 적용되는 복소 스펙트럼 정리이다.

**7.33 예: 한 연산자의 고유벡터들로 이루어진 정규직교기저**

$T\in\mathcal{L}(\mathbb{C}^2)$를

$$
T(w,z)=(2w-3z,3w+2z)
$$

로 정의하자. 표준기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
2 & -3\cr
3 & 2
\end{pmatrix}
$$

이다. 예 7.19에서 보았듯이 $T$는 정규 연산자이다. 직접 확인하면

$$
\frac{1}{\sqrt2}(i,1),\qquad
\frac{1}{\sqrt2}(-i,1)
$$

는 $T$의 고유벡터들로 이루어진 $\mathbb{C}^2$의 정규직교기저이고, 이 기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
2+3i & 0\cr
0 & 2-3i
\end{pmatrix}
$$

이다.

### 연습문제 7B

1. 복소 내적공간 위의 정규 연산자가 자기수반인 것은 그 모든 고윳값이 실수인 것과 동치임을 증명하여라.

2. $\mathbb{F}=\mathbb{C}$라고 하자. $T\in\mathcal{L}(V)$가 정규이고 고윳값을 하나만 가진다고 하자. $T$가 항등연산자의 스칼라배임을 증명하여라.

3. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 정규라고 하자. $T$의 고윳값들의 집합이 $\lbrace0,1\rbrace$에 포함되는 것과, 어떤 $V$의 부분공간 $U$가 존재하여 $T=P_U$가 되는 것은 동치임을 증명하여라.

4. 복소 내적공간 위의 정규 연산자가 반자기수반인 것은 그 모든 고윳값이 순허수인 것과 동치임을 증명하여라. 여기서 순허수란 실수부가 $0$인 수를 뜻한다.

5. 증명하거나 반례를 들어라. $T\in\mathcal{L}(\mathbb{C}^3)$가 대각화가능이면, 보통 내적에 대해 $T$는 정규이다.

6. $V$가 복소 내적공간이고 $T\in\mathcal{L}(V)$가 정규이며 $T^9=T^8$이라고 하자. $T$가 자기수반이고 $T^2=T$임을 증명하여라.

7. 복소 벡터공간 위의 연산자 $T$ 중 $T^9=T^8$이지만 $T^2\ne T$인 예를 제시하여라.

8. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 정규인 것과 $T$의 모든 고유벡터가 $T^*$의 고유벡터이기도 한 것은 동치임을 증명하여라.

9. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 정규인 것과 어떤 다항식 $p\in\mathcal{P}(\mathbb{C})$가 존재하여 $T^*=p(T)$가 되는 것은 동치임을 증명하여라.

10. $V$가 복소 내적공간이라고 하자. $V$ 위의 모든 정규 연산자가 제곱근을 가짐을 증명하여라.

    연산자 $S\in\mathcal{L}(V)$가 $S^2=T$를 만족하면 $S$를 $T\in\mathcal{L}(V)$의 제곱근이라고 한다. 연산자의 제곱근은 7C절과 8C절에서 더 다룬다.

11. $V$ 위의 모든 자기수반 연산자가 세제곱근을 가짐을 증명하여라.

    연산자 $S\in\mathcal{L}(V)$가 $S^3=T$를 만족하면 $S$를 $T$의 세제곱근이라고 한다.

12. $V$가 복소 벡터공간이고 $T\in\mathcal{L}(V)$가 정규라고 하자. $T$와 교환하는 모든 연산자 $S$는 $T^*$와도 교환함을 증명하여라. 이 결과는 푸글레데 정리라고 불린다.

13. 복소 스펙트럼 정리를 사용하지 말고, 두 교환 연산자에 적용되는 슈어 정리의 버전(6B절 연습문제 20번에서 $\mathcal{E}=\lbrace T,T^*\rbrace$로 둔다)을 사용하여 다음을 증명하여라. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 정규이면, $T$는 $V$의 어떤 정규직교기저에 대해 대각행렬을 가진다.

14. $\mathbb{F}=\mathbb{R}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 자기수반인 것은, 서로 다른 고윳값에 대응하는 모든 고유벡터 쌍이 직교하고

    $$
    V=E(\lambda_1,T)\oplus\cdots\oplus E(\lambda_m,T)
    $$

    가 성립하는 것과 동치임을 증명하여라. 여기서 $\lambda_1,\ldots,\lambda_m$은 $T$의 서로 다른 고윳값들이다.

15. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 정규인 것은, 서로 다른 고윳값에 대응하는 모든 고유벡터 쌍이 직교하고

    $$
    V=E(\lambda_1,T)\oplus\cdots\oplus E(\lambda_m,T)
    $$

    가 성립하는 것과 동치임을 증명하여라. 여기서 $\lambda_1,\ldots,\lambda_m$은 $T$의 서로 다른 고윳값들이다.

16. $\mathbb{F}=\mathbb{C}$이고 $\mathcal{E}\subset\mathcal{L}(V)$라고 하자. $\mathcal{E}$의 모든 원소가 어떤 하나의 정규직교기저에 대해 대각행렬을 가지는 것과, 모든 $S,T\in\mathcal{E}$가 서로 교환하는 정규 연산자인 것은 동치임을 증명하여라.

17. $\mathbb{F}=\mathbb{R}$이고 $\mathcal{E}\subset\mathcal{L}(V)$라고 하자. $\mathcal{E}$의 모든 원소가 어떤 하나의 정규직교기저에 대해 대각행렬을 가지는 것과, 모든 $S,T\in\mathcal{E}$가 서로 교환하는 자기수반 연산자인 것은 동치임을 증명하여라.

18. 실 내적공간 $V$, 연산자 $T\in\mathcal{L}(V)$, 실수 $b,c$ 중 $b^2<4c$를 만족하지만

    $$
    T^2+bT+cI
    $$

    가 가역이 아닌 예를 제시하여라. 이는 7.26에서 $T$가 자기수반이라는 가정을 제거할 수 없음을 보여 준다.

19. $T\in\mathcal{L}(V)$가 자기수반이고 $U$가 $T$에 대해 불변인 $V$의 부분공간이라고 하자.

    (a) $U^\perp$가 $T$에 대해 불변임을 증명하여라.

    (b) $T|_U\in\mathcal{L}(U)$가 자기수반임을 증명하여라.

    (c) $T|_{U^\perp}\in\mathcal{L}(U^\perp)$가 자기수반임을 증명하여라.

20. $T\in\mathcal{L}(V)$가 정규이고 $U$가 $T$에 대해 불변인 $V$의 부분공간이라고 하자.

    (a) $U^\perp$가 $T$에 대해 불변임을 증명하여라.

    (b) $U$가 $T^*$에 대해 불변임을 증명하여라.

    (c) $(T|_U)^*=(T^*)|_U$임을 증명하여라.

    (d) $T|_U\in\mathcal{L}(U)$와 $T|_{U^\perp}\in\mathcal{L}(U^\perp)$가 정규 연산자임을 증명하여라.

    이 연습문제는 복소 스펙트럼 정리의 또 다른 증명에 사용할 수 있다.

21. $T$가 유한차원 내적공간 위의 자기수반 연산자이고 $2$와 $3$이 $T$의 유일한 고윳값이라고 하자. 다음을 증명하여라.

    $$
    T^2-5T+6I=0.
    $$

22. $2$와 $3$이 유일한 고윳값이지만

    $$
    T^2-5T+6I\ne 0
    $$

    인 $T\in\mathcal{L}(\mathbb{C}^3)$의 예를 제시하여라.

23. $T\in\mathcal{L}(V)$가 자기수반이고 $\lambda\in\mathbb{F}$, $\varepsilon>0$이라고 하자. 어떤 $v\in V$가 $\Vert v\Vert=1$이고

    $$
    \Vert Tv-\lambda v\Vert<\varepsilon
    $$

    를 만족한다고 하자. 그러면 $T$가 어떤 고윳값 $\lambda'$를 가지며 $|\lambda-\lambda'|<\varepsilon$임을 증명하여라.

24. $U$가 유한차원 벡터공간이고 $T\in\mathcal{L}(U)$라고 하자.

    (a) $\mathbb{F}=\mathbb{R}$라고 하자. $T$가 대각화가능인 것과, $T$의 행렬이 자신의 전치와 같아지는 $U$의 어떤 기저가 존재하는 것은 동치임을 증명하여라.

    (b) $\mathbb{F}=\mathbb{C}$라고 하자. $T$가 대각화가능인 것과, $T$의 행렬이 자신의 켤레전치와 교환하는 $U$의 어떤 기저가 존재하는 것은 동치임을 증명하여라.

25. $T\in\mathcal{L}(V)$이고 $V$의 정규직교기저 $e_1,\ldots,e_n$이 $T$의 고유벡터들로 이루어져 있으며 대응하는 고윳값이 $\lambda_1,\ldots,\lambda_n$이라고 하자. $k\in\lbrace1,\ldots,n\rbrace$이면 유사역 $T^\dagger$가 다음을 만족함을 보여라.

    $$
    T^\dagger e_k=
    \begin{cases}
    \frac{1}{\lambda_k}e_k, & \lambda_k\ne 0,\cr
    0, & \lambda_k=0.
    \end{cases}
    $$

## 7C 양의 연산자

**7.34 정의: 양의 연산자**

연산자 $T\in\mathcal{L}(V)$가 자기수반이고 모든 $v\in V$에 대해

$$
\langle Tv,v\rangle\ge 0
$$

를 만족하면 $T$를 **양의 연산자**라고 한다.

$V$가 복소 벡터공간이면, 위 정의에서 $T$가 자기수반이어야 한다는 조건은 생략할 수 있다(7.14).

**7.35 예: 양의 연산자**

(a) 표준기저에 대한 행렬이

$$
\begin{pmatrix} 2 & -1\cr -1 & 1 \end{pmatrix}
$$

인 $T\in\mathcal{L}(\mathbb{F}^2)$를 생각하자. 그러면 $T$는 자기수반이고

$$
\begin{aligned}
\langle T(w,z),(w,z)\rangle
&=2|w|^2-2\text{Re}(w\overline z)+|z|^2\cr
&=|w-z|^2+|w|^2\ge 0.
\end{aligned}
$$

따라서 $T$는 양의 연산자이다.

(b) $U$가 $V$의 부분공간이면 직교사영 $P_U$는 양의 연산자이다.

(c) $T\in\mathcal{L}(V)$가 자기수반이고 $b,c\in\mathbb{R}$가 $b^2<4c$를 만족하면, 7.26의 증명에서 보았듯이 $T^2+bT+cI$는 양의 연산자이다.

**7.36 정의: 제곱근**

연산자 $R$가

$$
R^2=T
$$

를 만족하면 $R$를 연산자 $T$의 **제곱근**이라고 한다.

**7.37 예: 연산자의 제곱근**

$T\in\mathcal{L}(\mathbb{F}^3)$가

$$
T(z_1,z_2,z_3)=(z_3,0,0)
$$

로 정의되어 있다고 하자. $R\in\mathcal{L}(\mathbb{F}^3)$를

$$
R(z_1,z_2,z_3)=(z_2,z_3,0)
$$

로 정의하면 $R^2=T$이므로 $R$는 $T$의 제곱근이다.

양의 연산자는 비음수에 대응한다. 그래서 더 정확한 용어는 비음의 연산자일 수 있지만, 연산자 이론에서는 관습적으로 양의 연산자라고 부른다. 어떤 수학자들은 같은 뜻으로 양의 준정부호 연산자라는 말을 쓴다.

**7.38 양의 연산자의 특성화**

$T\in\mathcal{L}(V)$라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $T$는 양의 연산자이다.

(b) $T$는 자기수반이고 $T$의 모든 고윳값은 음이 아니다.

(c) $V$의 어떤 정규직교기저에 대해 $T$의 행렬은 대각선 위에 음이 아닌 수들만 있는 대각행렬이다.

(d) $T$는 양의 제곱근을 가진다.

(e) $T$는 자기수반 제곱근을 가진다.

(f) 어떤 $R\in\mathcal{L}(V)$에 대해

$$
T=R^*R.
$$

**증명**

(a)에서 (b)를 보이자. $T$가 양의 연산자이고 $\lambda$가 $T$의 고윳값이라고 하자. 대응하는 고유벡터 $v$에 대해

$$
0\le \langle Tv,v\rangle=\langle \lambda v,v\rangle=\lambda\langle v,v\rangle.
$$

따라서 $\lambda$는 음이 아닌 실수이다.

(b)에서 (c)는 스펙트럼 정리에서 따른다. 즉 $T$의 고유벡터들로 이루어진 정규직교기저 $e_1,\ldots,e_n$이 존재하며, 대응하는 고윳값 $\lambda_1,\ldots,\lambda_n$은 모두 음이 아니다. 이 기저에 대한 행렬은 대각선에 $\lambda_1,\ldots,\lambda_n$이 놓인 대각행렬이다.

(c)에서 (d)를 보이자. $e_1,\ldots,e_n$에 대한 $T$의 행렬이 대각선에 음이 아닌 수 $\lambda_1,\ldots,\lambda_n$을 가진다고 하자. $R e_k=\sqrt{\lambda_k}e_k$로 정의하면 $R$는 양의 연산자이고 $R^2=T$이다.

(d)는 곧 (e)를 함의한다. 양의 연산자는 정의상 자기수반이기 때문이다. (e)에서 (f)는 $T=R^2=R^*R$에서 따른다.

마지막으로 (f)에서 (a)를 보이자. $T=R^*R$이면

$$
T^*=(R^*R)^*=R^*R=T
$$

이므로 $T$는 자기수반이다. 또한 모든 $v\in V$에 대해

$$
\langle Tv,v\rangle
=\langle R^*Rv,v\rangle
=\langle Rv,Rv\rangle
\ge 0.
$$

따라서 $T$는 양의 연산자이다.

**7.39 각 양의 연산자는 양의 제곱근을 정확히 하나 가진다**

$V$ 위의 모든 양의 연산자는 유일한 양의 제곱근을 가진다.

**증명**

$T\in\mathcal{L}(V)$가 양의 연산자라고 하자. $v$가 $T$의 고유벡터이고 $Tv=\lambda v$라고 하자. 그러면 $\lambda\ge 0$이다.

$R$를 $T$의 양의 제곱근이라고 하자. $Rv=\sqrt{\lambda}v$임을 보이면, 스펙트럼 정리에 의해 $T$의 고유벡터들로 이루어진 기저가 존재하므로 $R$는 유일하게 결정된다.

$R$가 양의 연산자이므로 스펙트럼 정리에 의해 $R$의 고유벡터들로 이루어진 정규직교기저 $e_1,\ldots,e_n$이 존재한다. $R$의 고윳값은 음이 아니므로 어떤 음이 아닌 수 $\lambda_1,\ldots,\lambda_n$에 대해

$$
Re_k=\sqrt{\lambda_k}e_k
$$

이다. $v=a_1e_1+\cdots+a_ne_n$으로 쓰면

$$
Rv=a_1\sqrt{\lambda_1}e_1+\cdots+a_n\sqrt{\lambda_n}e_n
$$

이고

$$
\lambda v=Tv=R^2v=a_1\lambda_1e_1+\cdots+a_n\lambda_ne_n.
$$

따라서 각 $k$에 대해 $a_k(\lambda-\lambda_k)=0$이다. 그러므로

$$
v=\sum_{\lbrace k:\lambda_k=\lambda\rbrace}a_ke_k
$$

이고

$$
Rv=\sum_{\lbrace k:\lambda_k=\lambda\rbrace}a_k\sqrt{\lambda}e_k=\sqrt{\lambda}v.
$$

따라서 양의 제곱근은 유일하다. 존재는 7.38에서 이미 보였다.

**7.40 표기: $\sqrt T$**

$T$가 양의 연산자이면, $\sqrt T$는 $T$의 유일한 양의 제곱근을 뜻한다.

**7.41 예: 양의 연산자의 제곱근**

보통 유클리드 내적이 주어진 $\mathbb{R}^2$ 위의 연산자 $S,T$를

$$
S(x,y)=(x,2y),\qquad T(x,y)=(x+y,x+y)
$$

로 정의하자. 표준기저에 대해

$$
\mathcal{M}(S)=
\begin{pmatrix}
1 & 0\cr
0 & 2
\end{pmatrix},
\qquad
\mathcal{M}(T)=
\begin{pmatrix}
1 & 1\cr
1 & 1
\end{pmatrix}.
\tag{7.42}
$$

두 행렬은 모두 자신의 전치와 같으므로 $S$와 $T$는 자기수반이다. 또한

$$
\langle S(x,y),(x,y)\rangle=x^2+2y^2\ge 0
$$

이고

$$
\langle T(x,y),(x,y)\rangle=x^2+2xy+y^2=(x+y)^2\ge 0
$$

이므로 $S$와 $T$는 양의 연산자이다.

$\mathbb{R}^2$의 표준기저는 $S$의 고유벡터들로 이루어진 정규직교기저이다. 또한

$$
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),\qquad
\left(\frac1{\sqrt2},-\frac1{\sqrt2}\right)
$$

는 $T$의 고유벡터들로 이루어진 정규직교기저이고, 첫 번째 고유벡터의 고윳값은 $2$, 두 번째 고유벡터의 고윳값은 $0$이다. 따라서 $\sqrt T$는 같은 고유벡터들을 가지며 대응하는 고윳값은 $\sqrt2$와 $0$이다.

표준기저에 대해

$$
\mathcal{M}(\sqrt S)=
\begin{pmatrix}
1 & 0\cr
0 & \sqrt2
\end{pmatrix},
\qquad
\mathcal{M}(\sqrt T)=
\begin{pmatrix}
\frac1{\sqrt2} & \frac1{\sqrt2}\cr
\frac1{\sqrt2} & \frac1{\sqrt2}
\end{pmatrix}
$$

임을 확인할 수 있다.

**7.43 $T$가 양이고 $\langle Tv,v\rangle=0$이면 $Tv=0$**

$T$가 $V$ 위의 양의 연산자이고 $v\in V$가 $\langle Tv,v\rangle=0$을 만족한다고 하자. 그러면 $Tv=0$이다.

**증명**

$$
0=\langle Tv,v\rangle
=\langle \sqrt T\sqrt T v,v\rangle
=\langle \sqrt T v,\sqrt T v\rangle
=\Vert\sqrt T v\Vert^2.
$$

따라서 $\sqrt T v=0$이고, 그러므로 $Tv=\sqrt T(\sqrt T v)=0$이다.

### 연습문제 7C

1. $T\in\mathcal{L}(V)$라고 하자. $T$와 $-T$가 모두 양의 연산자이면 $T=0$임을 증명하여라.

2. 표준기저에 대한 행렬이

   $$
   \begin{pmatrix}
   2 & -1 & 0 & 0\cr
   -1 & 2 & -1 & 0\cr
   0 & -1 & 2 & -1\cr
   0 & 0 & -1 & 2
   \end{pmatrix}
   $$

   인 $T\in\mathcal{L}(\mathbb{F}^4)$가 가역인 양의 연산자임을 보여라.

3. $n$이 양의 정수이고, 표준기저에 대한 행렬의 모든 성분이 $1$인 $T\in\mathcal{L}(\mathbb{F}^n)$를 생각하자. $T$가 양의 연산자임을 보여라.

4. $n>1$인 정수라고 하자. 모든 성분이 양수이고 $A=A^*$이지만, 표준기저에 대한 행렬이 $A$인 $\mathbb{F}^n$ 위의 연산자는 양의 연산자가 아닌 $n\times n$ 행렬 $A$가 존재함을 보여라.

5. $T\in\mathcal{L}(V)$가 자기수반이라고 하자. $T$가 양의 연산자인 것과, $V$의 모든 정규직교기저 $e_1,\ldots,e_n$에 대해 $\mathcal{M}(T,(e_1,\ldots,e_n))$의 대각성분들이 모두 음이 아닌 것은 동치임을 증명하여라.

6. $V$ 위의 두 양의 연산자의 합은 양의 연산자임을 증명하여라.

7. $S\in\mathcal{L}(V)$가 가역인 양의 연산자이고 $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. $S+T$가 가역임을 증명하여라.

8. $T\in\mathcal{L}(V)$라고 하자. $T$가 양의 연산자인 것과 유사역 $T^\dagger$가 양의 연산자인 것은 동치임을 증명하여라.

9. $T\in\mathcal{L}(V)$가 양의 연산자이고 $S\in\mathcal{L}(W,V)$라고 하자. $S^*TS$가 $W$ 위의 양의 연산자임을 증명하여라.

10. $T$가 $V$ 위의 양의 연산자라고 하자. $v,w\in V$가

    $$
    Tv=w,\qquad Tw=v
    $$

    를 만족한다고 하자. $v=w$임을 증명하여라.

11. $T$가 $V$ 위의 양의 연산자이고 $U$가 $T$에 대해 불변인 $V$의 부분공간이라고 하자. $T|_U\in\mathcal{L}(U)$가 $U$ 위의 양의 연산자임을 증명하여라.

12. $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. 모든 양의 정수 $k$에 대해 $T^k$가 양의 연산자임을 증명하여라.

13. $T\in\mathcal{L}(V)$가 자기수반이고 $\alpha\in\mathbb{R}$라고 하자.

    (a) $T-\alpha I$가 양의 연산자인 것은 $\alpha$가 $T$의 모든 고윳값 이하인 것과 동치임을 증명하여라.

    (b) $\alpha I-T$가 양의 연산자인 것은 $\alpha$가 $T$의 모든 고윳값 이상인 것과 동치임을 증명하여라.

14. $T$가 $V$ 위의 양의 연산자이고 $v_1,\ldots,v_m\in V$라고 하자. 다음을 증명하여라.

    $$
    \sum_{j=1}^m\sum_{k=1}^m\langle Tv_k,v_j\rangle\ge 0.
    $$

15. $T\in\mathcal{L}(V)$가 자기수반이라고 하자. 양의 연산자 $A,B\in\mathcal{L}(V)$가 존재하여

    $$
    T=A-B,\qquad \sqrt{T^*T}=A+B,\qquad AB=BA=0
    $$

    이 됨을 증명하여라.

16. $T$가 $V$ 위의 양의 연산자라고 하자. 다음을 증명하여라.

    $$
    \text{null}\sqrt T=\text{null}T,\qquad
    \text{range}\sqrt T=\text{range}T.
    $$

17. $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. 실수 계수를 가진 다항식 $p$가 존재하여 $\sqrt T=p(T)$가 됨을 증명하여라.

18. $S$와 $T$가 $V$ 위의 양의 연산자라고 하자. $ST$가 양의 연산자인 것과 $S$와 $T$가 교환하는 것은 동치임을 증명하여라.

19. $\mathbb{F}^2$ 위의 항등연산자가 자기수반 제곱근을 무한히 많이 가짐을 보여라.

20. $T\in\mathcal{L}(V)$이고 $e_1,\ldots,e_n$이 $V$의 정규직교기저라고 하자. $T$가 양의 연산자인 것과, 어떤 $v_1,\ldots,v_n\in V$가 존재하여 모든 $j,k=1,\ldots,n$에 대해

    $$
    \langle Te_k,e_j\rangle=\langle v_k,v_j\rangle
    $$

    가 성립하는 것은 동치임을 증명하여라.

21. $n$이 양의 정수라고 하자. $n\times n$ 힐베르트 행렬은 $j$행 $k$열 성분이 $\frac1{j+k-1}$인 행렬이다. $T\in\mathcal{L}(V)$의 어떤 정규직교기저에 대한 행렬이 $n\times n$ 힐베르트 행렬이라고 하자. $T$가 가역인 양의 연산자임을 증명하여라.

    예를 들어 $4\times 4$ 힐베르트 행렬은

    $$
    \begin{pmatrix}
    1 & \frac12 & \frac13 & \frac14\cr
    \frac12 & \frac13 & \frac14 & \frac15\cr
    \frac13 & \frac14 & \frac15 & \frac16\cr
    \frac14 & \frac15 & \frac16 & \frac17
    \end{pmatrix}
    $$

    이다.

22. $T\in\mathcal{L}(V)$가 양의 연산자이고 $u\in V$가 $\Vert u\Vert=1$이며 모든 $\Vert v\Vert=1$인 $v\in V$에 대해 $\Vert Tu\Vert\ge\Vert Tv\Vert$를 만족한다고 하자. $u$가 $T$의 가장 큰 고윳값에 대응하는 고유벡터임을 보여라.

23. $T\in\mathcal{L}(V)$와 $u,v\in V$에 대해 $\langle u,v\rangle_T=\langle Tu,v\rangle$로 정의한다.

    (a) $\langle\cdot,\cdot\rangle_T$가 $V$ 위의 내적인 것은 $T$가 원래 내적에 대해 가역인 양의 연산자인 것과 동치임을 증명하여라.

    (b) $V$ 위의 모든 내적은 어떤 가역인 양의 연산자 $T\in\mathcal{L}(V)$에 대해 $\langle\cdot,\cdot\rangle_T$ 꼴임을 증명하여라.

24. $S$와 $T$가 $V$ 위의 양의 연산자라고 하자. 다음을 증명하여라.

    $$
    \text{null}(S+T)=\text{null}S\cap\text{null}T.
    $$

25. 7A절 연습문제 31(b)의 두 번째 미분 연산자를 $T$라고 하자. $-T$가 양의 연산자임을 보여라.

## 7D 등거리사상, 유니터리 연산자, 행렬분해

### 등거리사상

노름을 보존하는 선형사상은 충분히 중요하므로 이름을 붙인다.

**7.44 정의: 등거리사상**

선형사상 $S\in\mathcal{L}(V,W)$가 모든 $v\in V$에 대해

$$
\Vert Sv\Vert=\Vert v\Vert
$$

를 만족하면 $S$를 **등거리사상**이라고 한다. 즉 등거리사상은 노름을 보존하는 선형사상이다.

$S\in\mathcal{L}(V,W)$가 등거리사상이고 $Sv=0$이면

$$
\Vert v\Vert=\Vert Sv\Vert=\Vert0\Vert=0
$$

이므로 $v=0$이다. 따라서 모든 등거리사상은 단사이다.

**7.45 예: 정규직교기저를 정규직교 리스트로 보내면 등거리사상이다**

$e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $g_1,\ldots,g_n$이 $W$의 정규직교 리스트라고 하자. $S\in\mathcal{L}(V,W)$가 각 $k=1,\ldots,n$에 대해 $Se_k=g_k$를 만족한다고 하자. $v\in V$이면

$$
v=\langle v,e_1\rangle e_1+\cdots+\langle v,e_n\rangle e_n
\tag{7.46}
$$

이고

$$
\Vert v\Vert^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2.
\tag{7.47}
$$

7.46의 양변에 $S$를 적용하면

$$
Sv=\langle v,e_1\rangle g_1+\cdots+\langle v,e_n\rangle g_n.
$$

따라서

$$
\Vert Sv\Vert^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2.
\tag{7.48}
$$

7.47과 7.48을 비교하면 $\Vert Sv\Vert=\Vert v\Vert$이다. 따라서 $S$는 등거리사상이다.

**7.49 등거리사상의 특성화**

$S\in\mathcal{L}(V,W)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $f_1,\ldots,f_m$이 $W$의 정규직교기저라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $S$는 등거리사상이다.

(b)

$$
S^*S=I.
$$

(c) 모든 $u,v\in V$에 대해

$$
\langle Su,Sv\rangle=\langle u,v\rangle.
$$

(d) $Se_1,\ldots,Se_n$은 $W$의 정규직교 리스트이다.

(e) 행렬

$$
\mathcal{M}(S,(e_1,\ldots,e_n),(f_1,\ldots,f_m))
$$

의 열들은 유클리드 내적에 대해 $\mathbb{F}^m$의 정규직교 리스트를 이룬다.

**증명**

(a)가 성립한다고 하자. 그러면 모든 $v\in V$에 대해

$$
\langle (I-S^*S)v,v\rangle=\Vert v\Vert^2-\Vert Sv\Vert^2=0.
$$

$I-S^*S$는 자기수반이므로 7.16에 의해 $I-S^*S=0$이다. 따라서 (b)가 성립한다.

(b)가 성립하면

$$
\langle Su,Sv\rangle=\langle S^*Su,v\rangle=\langle u,v\rangle
$$

이므로 (c)가 성립한다. (c)를 $u=e_j$, $v=e_k$에 적용하면 $Se_1,\ldots,Se_n$이 정규직교 리스트이므로 (d)가 성립한다.

(d)가 성립한다고 하자. $A=\mathcal{M}(S,(e_1,\ldots,e_n),(f_1,\ldots,f_m))$라고 하자. $k,r\in\lbrace1,\ldots,n\rbrace$이면

$$
\sum_{j=1}^m A_{j,k}\overline{A_{j,r}} =
\left\langle \sum_{j=1}^m A_{j,k}f_j,\sum_{j=1}^m A_{j,r}f_j\right\rangle =\langle Se_k,Se_r\rangle =
\begin{cases}
1, & k=r,\cr
0, & k\ne r.
\end{cases}
\tag{7.50}
$$

왼쪽은 $A$의 $k$번째 열과 $r$번째 열의 $\mathbb{F}^m$에서의 내적이다. 따라서 (e)가 성립한다. 마지막으로 (e)가 성립하면 (7.50)에 의해 $Se_1,\ldots,Se_n$이 정규직교 리스트이고, 7.45에 의해 $S$는 등거리사상이다.

### 유니터리 연산자

이제 한 벡터공간에서 자기 자신으로 가는 선형사상, 즉 연산자만 다룬다.

**7.51 정의: 유니터리 연산자**

연산자 $S\in\mathcal{L}(V)$가 가역인 등거리사상이면 $S$를 **유니터리 연산자**라고 한다.

유한차원에서는 모든 등거리사상이 단사이고, 단사인 연산자는 가역이다. 따라서 이 장의 상황에서는 위 정의에서 "가역"이라는 말을 빼도 뜻은 달라지지 않는다. 그러나 무한차원 내적공간에서 만나는 표준 정의와 맞추기 위해 이 말을 남겨 둔다.

**7.52 예: $\mathbb{R}^2$의 회전**

$\theta\in\mathbb{R}$이고 $S$가 표준기저에 대한 행렬

$$
\begin{pmatrix}
\cos\theta & -\sin\theta\cr
\sin\theta & \cos\theta
\end{pmatrix}
$$

을 가지는 $\mathbb{F}^2$ 위의 연산자라고 하자. 이 행렬의 두 열은 $\mathbb{F}^2$의 정규직교 리스트를 이룬다. 따라서 7.49의 (a)와 (e)의 동치에 의해 $S$는 등거리사상이고, 그러므로 유니터리 연산자이다.

$\mathbb{F}=\mathbb{R}$이면 $S$는 $\mathbb{R}^2$에서 원점 중심의 $\theta$ 라디안 반시계방향 회전이다. 회전은 노름을 보존하므로 등거리사상이라는 사실을 기하적으로도 이해할 수 있다.

**7.53 유니터리 연산자의 특성화**

$S\in\mathcal{L}(V)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교기저라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $S$는 유니터리 연산자이다.

(b)

$$
S^*S=SS^*=I.
$$

(c) $S$는 가역이고

$$
S^{-1}=S^*.
$$

(d) $Se_1,\ldots,Se_n$은 $V$의 정규직교기저이다.

(e) $\mathcal{M}(S,(e_1,\ldots,e_n))$의 행들은 유클리드 내적에 대해 $\mathbb{F}^n$의 정규직교기저를 이룬다.

(f) $S^*$는 유니터리 연산자이다.

**증명**

(a)가 성립하면 7.49에 의해 $S^*S=I$이다. 오른쪽에 $S^{-1}$를 곱하면 $S^*=S^{-1}$이고, 따라서 $SS^*=I$이다. 그러므로 (b)가 성립한다.

(b)는 (c)를 바로 함의한다. (c)가 성립하면 $S^*S=I$이므로 7.49에 의해 $Se_1,\ldots,Se_n$은 정규직교 리스트이다. 길이가 $\dim V$이므로 정규직교기저이고, 따라서 (d)가 성립한다.

(d)가 성립하면 7.49에 의해 $S$는 유니터리 연산자이다. 이미 (a)가 (b)를 함의함을 보였으므로 $SS^*=I$이다. 따라서 $S^*$는 등거리사상이고, 그 행렬의 열들은 정규직교기저를 이룬다. 이는 $S$의 행들이 정규직교기저를 이룬다는 말이므로 (e)가 성립한다.

(e)가 성립하면 $S^*$의 행렬의 열들이 정규직교기저를 이루므로 7.49에 의해 $S^*$는 등거리사상이다. 따라서 유니터리 연산자이고 (f)가 성립한다. 마지막으로 (f)를 $S^*$에 적용하면 $(S^*)^*=S$가 유니터리임을 얻는다.

**7.54 유니터리 연산자의 고윳값은 절댓값이 $1$이다**

유니터리 연산자의 고윳값 $\lambda$는

$$
|\lambda|=1
$$

을 만족한다.

**증명**

$S$가 유니터리 연산자이고 $Sv=\lambda v$이며 $v\ne 0$이라고 하자. 그러면

$$
|\lambda|\thinspace\Vert v\Vert=\Vert\lambda v\Vert=\Vert Sv\Vert=\Vert v\Vert.
$$

따라서 $|\lambda|=1$이다.

**7.55 복소 내적공간 위의 유니터리 연산자의 기술**

$\mathbb{F}=\mathbb{C}$이고 $S\in\mathcal{L}(V)$라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $S$는 유니터리 연산자이다.

(b) $V$는 $S$의 고유벡터들로 이루어진 정규직교기저를 가지며, 그 대응하는 고윳값들은 모두 절댓값이 $1$이다.

**증명**

$S$가 유니터리이면 7.53에 의해 $S$는 정규이다. 복소 스펙트럼 정리(7.31)에 의해 $S$의 고유벡터들로 이루어진 정규직교기저가 존재한다. 7.54에 의해 모든 고윳값의 절댓값은 $1$이다.

반대로 $e_1,\ldots,e_n$이 $S$의 고유벡터들로 이루어진 정규직교기저이고 대응하는 고윳값 $\lambda_1,\ldots,\lambda_n$이 모두 $|\lambda_k|=1$을 만족한다고 하자. 그러면

$$
\langle Se_j,Se_k\rangle
=\langle \lambda_j e_j,\lambda_k e_k\rangle
=\lambda_j\overline{\lambda_k}\langle e_j,e_k\rangle
=\begin{cases} 0, & j\ne k,\cr 1, & j=k. \end{cases}
$$

따라서 $Se_1,\ldots,Se_n$은 정규직교기저이고, 7.53에 의해 $S$는 유니터리이다.

### QR 분해

이제 연산자에서 행렬로 잠시 관심을 옮긴다. 별다른 말이 없으면 $n\times n$ 행렬은 보통 유클리드 내적이 주어진 $\mathbb{F}^n$ 위의 연산자를 표준기저에 대해 나타낸 행렬로 생각한다.

**7.56 정의: 유니터리 행렬**

$n\times n$ 행렬의 열들이 $\mathbb{F}^n$의 정규직교 리스트를 이루면 그 행렬을 **유니터리 행렬**이라고 한다.

길이가 $n$인 정규직교 리스트는 $\mathbb{F}^n$의 정규직교기저이므로, 위 정의에서 "정규직교 리스트"를 "정규직교기저"로 바꿔도 된다. 또한 유니터리 연산자의 특성화에 의해 "열"을 "행"으로 바꿔도 된다.

**7.57 유니터리 행렬의 특성화**

$Q$가 $n\times n$ 행렬이라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $Q$는 유니터리 행렬이다.

(b) $Q$의 행들은 $\mathbb{F}^n$의 정규직교 리스트를 이룬다.

(c) 모든 $v\in\mathbb{F}^n$에 대해

$$
\Vert Qv\Vert=\Vert v\Vert.
$$

(d)

$$
Q^*Q=QQ^*=I,
$$

여기서 $I$는 대각선 위에는 $1$이 있고 그 밖에는 $0$인 $n\times n$ 행렬이다.

**7.58 QR 분해**

$A$가 열들이 일차독립인 정사각행렬이라고 하자. 그러면 유니터리 행렬 $Q$와 대각선 성분이 모두 양수인 상삼각행렬 $R$가 유일하게 존재하여

$$
A=QR
$$

가 성립한다.

**증명**

$A$의 열들을 $\mathbb{F}^n$의 벡터 $v_1,\ldots,v_n$이라고 생각하자. 이 리스트에 그램-슈미트 절차를 적용하여 각 $k=1,\ldots,n$에 대해

$$
\text{span}(v_1,\ldots,v_k)=\text{span}(e_1,\ldots,e_k)
\tag{7.59}
$$

를 만족하는 $\mathbb{F}^n$의 정규직교기저 $e_1,\ldots,e_n$을 얻는다. 행렬 $R$의 $j$행 $k$열 성분을

$$
R_{j,k}=\langle v_k,e_j\rangle
$$

로 정의한다. $j>k$이면 $e_j$는 $\text{span}(e_1,\ldots,e_k)$에 직교하므로, (7.59)에 의해 $v_k$에도 직교한다. 따라서 $R_{j,k}=0$이고 $R$는 상삼각행렬이다.

$Q$를 열들이 $e_1,\ldots,e_n$인 유니터리 행렬로 두자. $QR$의 $k$번째 열은

$$
\langle v_k,e_1\rangle e_1+\cdots+\langle v_k,e_k\rangle e_k
$$

이고, 이는 6.30(a)에 의해 $v_k$이다. 따라서 $A=QR$이다. 그램-슈미트 절차의 정의에 의해 각 $\langle v_k,e_k\rangle$은 양수이므로 $R$의 대각성분은 모두 양수이다.

유일성을 보이기 위해 $A=\widehat Q\widehat R$도 같은 조건을 만족한다고 하자. $\widehat Q$의 열을 $q_1,\ldots,q_n$이라 하면 각 $k$에 대해 $\text{span}(v_1,\ldots,v_k)=\text{span}(q_1,\ldots,q_k)$이고 $\langle v_k,q_k\rangle>0$이다. 6B절 연습문제 10번의 유일성에 의해 $q_k=e_k$이다. 따라서 $\widehat Q=Q$이고 곧 $\widehat R=R$이다.

**7.60 예: $3\times 3$ 행렬의 QR 분해**

행렬

$$
A=
\begin{pmatrix}
1 & 2 & 1\cr
0 & 1 & -4\cr
0 & 3 & 2
\end{pmatrix}
$$

의 QR 분해를 구하자. $A$의 열들을

$$
v_1=(1,0,0),\qquad
v_2=(2,1,3),\qquad
v_3=(1,-4,2)
$$

라고 하자. 그램-슈미트 절차를 적용하면

$$
e_1=(1,0,0),\qquad
e_2=\left(0,\frac1{\sqrt{10}},\frac3{\sqrt{10}}\right),\qquad
e_3=\left(0,-\frac3{\sqrt{10}},\frac1{\sqrt{10}}\right)
$$

을 얻는다. 따라서

$$
Q=
\begin{pmatrix}
1 & 0 & 0\cr
0 & \frac1{\sqrt{10}} & -\frac3{\sqrt{10}}\cr
0 & \frac3{\sqrt{10}} & \frac1{\sqrt{10}}
\end{pmatrix}
$$

이고, $R_{j,k}=\langle v_k,e_j\rangle$로부터

$$
R=
\begin{pmatrix}
1 & 2 & 1\cr
0 & \sqrt{10} & \frac{\sqrt{10}}5\cr
0 & 0 & \frac{7\sqrt{10}}5
\end{pmatrix}
$$

을 얻는다. 실제로

$$
QR=
\begin{pmatrix}
1 & 2 & 1\cr
0 & 1 & -4\cr
0 & 3 & 2
\end{pmatrix}
=A.
$$

QR 분해는 $Ax=b$ 같은 선형방정식계를 푸는 데도 사용할 수 있다. $A=QR$이면 $Ax=b$는 $QRx=b$와 동치이고, 왼쪽에 $Q^*$를 곱하면

$$
Rx=Q^*b
$$

가 된다. $R$가 대각성분이 양수인 상삼각행렬이므로, 뒤에서부터 대입하여 빠르게 풀 수 있다.

### 촐레스키 분해

**7.61 가역인 양의 연산자**

자기수반 연산자 $T\in\mathcal{L}(V)$가 가역인 양의 연산자인 것은 모든 영이 아닌 $v\in V$에 대해

$$
\langle Tv,v\rangle>0
$$

가 성립하는 것과 동치이다.

**증명**

$T$가 가역인 양의 연산자이고 $v\ne 0$이면 $Tv\ne 0$이다. 7.43에 의해 $\langle Tv,v\rangle$는 $0$일 수 없고, 양의 연산자이므로 음수도 아니다. 따라서 $\langle Tv,v\rangle>0$이다.

반대로 모든 $v\ne 0$에 대해 $\langle Tv,v\rangle>0$이면 $Tv\ne 0$이다. 따라서 $T$는 단사이고, 유한차원에서 단사 연산자는 가역이다.

**7.62 정의: 양의 정부호**

행렬 $B\in\mathbb{F}^{n,n}$이

$$
B^*=B
$$

이고 모든 영이 아닌 $x\in\mathbb{F}^n$에 대해

$$
\langle Bx,x\rangle>0
$$

을 만족하면 $B$를 **양의 정부호**라고 한다.

**7.63 촐레스키 분해**

$B$가 양의 정부호 행렬이라고 하자. 그러면 대각선 성분이 모두 양수인 상삼각행렬 $R$가 유일하게 존재하여

$$
B=R^*R
$$

이 성립한다.

**증명**

$B$가 양의 정부호이므로 7.38의 (a)와 (f)의 동치에 의해, $B$와 같은 크기의 가역 정사각행렬 $A$가 존재하여 $B=A^*A$이다.

$A=QR$를 $A$의 QR 분해라고 하자. 여기서 $Q$는 유니터리이고 $R$는 대각선 성분이 모두 양수인 상삼각행렬이다. 그러면 $A^*=R^*Q^*$이고

$$
B=A^*A=R^*Q^*QR=R^*R.
$$

앙드레-루이 촐레스키(1875-1918)는 이 분해를 발견했고, 이 결과는 사후인 1924년에 출판되었다.

유일성을 보이자. $S$도 대각선 성분이 모두 양수인 상삼각행렬이고 $B=S^*S$라고 하자. $B$가 가역이므로 $S$도 가역이다. $B=S^*S$의 양변 오른쪽에 $S^{-1}$를 곱하면 $BS^{-1}=S^*$이다. 위에서 택한 $A$에 대해

$$
\begin{aligned}
(AS^{-1})^*(AS^{-1})
&=(S^*)^{-1}A^*AS^{-1}\cr
&=(S^*)^{-1}BS^{-1}\cr
&=(S^*)^{-1}S^*\cr
&=I.
\end{aligned}
$$

따라서 $AS^{-1}$는 유니터리이다. 그러므로 $A=(AS^{-1})S$는 $A$를 유니터리 행렬과 대각선 성분이 양수인 상삼각행렬의 곱으로 나타내는 분해이다. QR 분해의 유일성에 의해 $S=R$이다.

### 연습문제 7D

1. $\dim V\ge 2$이고 $S\in\mathcal{L}(V,W)$라고 하자. $S$가 등거리사상인 것과, $V$의 길이 $2$인 모든 정규직교 리스트 $e_1,e_2$에 대해 $Se_1,Se_2$가 $W$의 정규직교 리스트인 것은 동치임을 증명하여라.

2. $T\in\mathcal{L}(V,W)$이고 $T\ne 0$이라고 하자. $T$가 등거리사상의 스칼라배인 것과 $T$가 직교성을 보존하는 것은 동치임을 증명하여라. 여기서 $T$가 직교성을 보존한다는 것은 $\langle u,v\rangle=0$이면 $\langle Tu,Tv\rangle=0$이라는 뜻이다.

3. (a) $V$ 위의 두 유니터리 연산자의 곱은 유니터리 연산자임을 보여라.

   (b) $V$ 위의 유니터리 연산자의 역은 유니터리 연산자임을 보여라.

   이 연습문제는 유니터리 연산자들의 집합이 보통의 연산자 곱을 연산으로 하는 군임을 보여 준다.

4. $\mathbb{F}=\mathbb{C}$이고 $A,B\in\mathcal{L}(V)$가 자기수반이라고 하자. $A+iB$가 유니터리인 것과 $AB=BA$이고 $A^2+B^2=I$인 것은 동치임을 보여라.

5. $S\in\mathcal{L}(V)$라고 하자. 다음 조건들이 서로 동치임을 증명하여라.

   (a) $S$는 자기수반 유니터리 연산자이다.

   (b) 어떤 $V$ 위의 직교사영 $P$에 대해 $S=2P-I$이다.

   (c) 어떤 $V$의 부분공간 $U$가 존재하여 모든 $u\in U$에 대해 $Su=u$이고 모든 $w\in U^\perp$에 대해 $Sw=-w$이다.

6. $T_1,T_2$가 모두 $\mathbb{F}^3$ 위의 정규 연산자이고 고윳값이 $2,5,7$이라고 하자. 어떤 유니터리 연산자 $S\in\mathcal{L}(\mathbb{F}^3)$가 존재하여 $T_1=S^*T_2S$가 됨을 증명하여라.

7. $T_1,T_2\in\mathcal{L}(\mathbb{F}^4)$가 자기수반이고 두 연산자의 고윳값이 모두 $2,5,7$이지만, $T_1=S^*T_2S$를 만족하는 유니터리 연산자 $S\in\mathcal{L}(\mathbb{F}^4)$는 존재하지 않는 예를 제시하여라. 왜 그런 $S$가 존재하지 않는지도 설명하여라.

8. 증명하거나 반례를 들어라. $S\in\mathcal{L}(V)$이고 어떤 정규직교기저 $e_1,\ldots,e_n$에 대해 각 $k$마다 $\Vert Se_k\Vert=1$이면 $S$는 유니터리이다.

9. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$의 모든 고윳값의 절댓값이 $1$이고 모든 $v\in V$에 대해 $\Vert Tv\Vert\le\Vert v\Vert$이면 $T$가 유니터리임을 증명하여라.

10. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 자기수반이며 모든 $v\in V$에 대해 $\Vert Tv\Vert\le\Vert v\Vert$라고 하자.

    (a) $I-T^2$가 양의 연산자임을 보여라.

    (b) $T+i\sqrt{I-T^2}$가 유니터리 연산자임을 보여라.

11. $S\in\mathcal{L}(V)$라고 하자. $S$가 유니터리 연산자인 것과

    $$
    \lbrace Sv:v\in V,\ \Vert v\Vert\le 1\rbrace=\lbrace v\in V:\Vert v\Vert\le 1\rbrace
    $$

    인 것은 동치임을 증명하여라.

12. 증명하거나 반례를 들어라. $S\in\mathcal{L}(V)$가 가역이고 모든 $v\in V$에 대해 $\Vert S^{-1}v\Vert=\Vert Sv\Vert$이면 $S$는 유니터리이다.

13. 복소수 성분을 가진 정사각행렬의 열들이 $\mathbb{C}^n$의 정규직교 리스트를 이루는 것과 행들이 $\mathbb{C}^n$의 정규직교 리스트를 이루는 것은 동치인 이유를 설명하여라.

14. $v\in V$이고 $\Vert v\Vert=1$, $b\in\mathbb{F}$이며 $\dim V\ge 2$라고 하자. $\langle Sv,v\rangle=b$를 만족하는 유니터리 연산자 $S\in\mathcal{L}(V)$가 존재하는 것과 $|b|\le 1$인 것은 동치임을 증명하여라.

15. $T$가 $V$ 위의 유니터리 연산자이고 $T-I$가 가역이라고 하자.

    (a) $(T+I)(T-I)^{-1}$가 반자기수반임을 증명하여라.

    (b) $\mathbb{F}=\mathbb{C}$이면 $i(T+I)(T-I)^{-1}$가 자기수반 연산자임을 증명하여라.

16. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 자기수반이라고 하자. $(T+iI)(T-iI)^{-1}$가 유니터리 연산자이고 $1$이 이 연산자의 고윳값이 아님을 증명하여라.

17. 7.57에 주어진 유니터리 행렬의 특성화들이 성립하는 이유를 설명하여라.

18. 정사각행렬 $A$가 자신의 전치와 같으면 $A$를 대칭행렬이라고 한다. $A$가 실수 성분을 가진 대칭행렬이면, 실수 성분을 가진 유니터리 행렬 $Q$가 존재하여 $Q^*AQ$가 대각행렬이 됨을 증명하여라.

19. $n$이 양의 정수라고 하자. 이 연습문제에서는 $\mathbb{C}^n$의 원소를 $z=(z_0,z_1,\ldots,z_{n-1})$로 쓴다. $\mathbb{C}^n$ 위의 선형함수 $\omega_0,\omega_1,\ldots,\omega_{n-1}$를

    $$
    \omega_j(z_0,z_1,\ldots,z_{n-1})
    =\frac1{\sqrt n}\sum_{m=0}^{n-1}z_m e^{-2\pi ijm/n}
    $$

    로 정의한다. 이산 푸리에 변환은

    $$
    \mathcal{F}z=(\omega_0(z),\omega_1(z),\ldots,\omega_{n-1}(z))
    $$

    로 정의되는 연산자 $\mathcal{F}:\mathbb{C}^n\to\mathbb{C}^n$이다.

    (a) $\mathcal{F}$가 $\mathbb{C}^n$ 위의 유니터리 연산자임을 보여라.

    (b) $(z_0,\ldots,z_{n-1})\in\mathbb{C}^n$이고 $z_n=z_0$로 정의하면

    $$
    \mathcal{F}^{-1}(z_0,z_1,\ldots,z_{n-1})
    =\mathcal{F}(z_n,z_{n-1},\ldots,z_1)
    $$

    임을 보여라.

    (c) $\mathcal{F}^4=I$임을 보여라.

20. $A$가 열들이 일차독립인 정사각행렬이라고 하자. 대각선 성분이 모두 양수인 하삼각행렬 $R$와 유니터리 행렬 $Q$가 유일하게 존재하여 $A=RQ$가 됨을 증명하여라.

## 7E 특이값분해

### 특이값

**7.64 $T^*T$의 성질**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) $T^*T$는 $V$ 위의 양의 연산자이다.

(b)

$$
\text{null}T^*T=\text{null}T.
$$

(c)

$$
\text{range}T^*T=\text{range}T^*.
$$

(d)

$$
\dim\text{range}T
=\dim\text{range}T^*
=\dim\text{range}T^*T.
$$

**증명**

(a) 먼저

$$
(T^*T)^*=T^*(T^*)^*=T^*T
$$

이므로 $T^*T$는 자기수반이다. 또한 $v\in V$이면

$$
\langle (T^*T)v,v\rangle
=\langle Tv,Tv\rangle
=\Vert Tv\Vert^2\ge 0.
$$

따라서 $T^*T$는 양의 연산자이다.

(b) $v\in\text{null}T^*T$이면

$$
\Vert Tv\Vert^2=\langle T^*Tv,v\rangle=0
$$

이므로 $Tv=0$이다. 반대 포함은 명백하다.

(c)는 (a), (b), 7.6에서

$$
\text{range}T^*T
=(\text{null}T^*T)^\perp
=(\text{null}T)^\perp
=\text{range}T^*
$$

로 얻는다.

(d)의 첫 등식은

$$
\dim\text{range}T
=\dim(\text{null}T^*)^\perp
=\dim W-\dim\text{null}T^*
=\dim\text{range}T^*
$$

에서 나오고, 두 번째 등식은 (c)에서 나온다.

**7.65 정의: 특이값**

$T\in\mathcal{L}(V,W)$라고 하자. $T$의 **특이값**은 $T^*T$의 고윳값들의 음이 아닌 제곱근을 큰 것부터 나열한 리스트이다. 각 값은 $T^*T$의 대응하는 고유공간의 차원만큼 반복하여 포함한다.

**7.66 예: $\mathbb{F}^4$ 위의 연산자의 특이값**

$T\in\mathcal{L}(\mathbb{F}^4)$를

$$
T(z_1,z_2,z_3,z_4)=(0,3z_1,2z_2,-3z_4)
$$

로 정의하자. 계산하면

$$
T^*T(z_1,z_2,z_3,z_4)=(9z_1,4z_2,0,9z_4)
$$

이다. 따라서 $T^*T$의 고윳값은 $9,4,0$이고

$$
\dim E(9,T^*T)=2,\qquad
\dim E(4,T^*T)=1,\qquad
\dim E(0,T^*T)=1.
$$

그러므로 $T$의 특이값은

$$
3,3,2,0
$$

이다. 이 예에서 $T$의 고윳값은 $-3$과 $0$뿐이므로, 고윳값만으로는 $T$의 정의에 나타난 수 $2$를 잡아내지 못하지만 특이값은 이를 포함한다.

**7.67 예: $\mathbb{F}^4$에서 $\mathbb{F}^3$으로 가는 선형사상의 특이값**

$T\in\mathcal{L}(\mathbb{F}^4,\mathbb{F}^3)$의 표준기저에 대한 행렬이

$$
\begin{pmatrix}
0 & 0 & 0 & -5\cr
0 & 0 & 0 & 0\cr
1 & 1 & 0 & 0
\end{pmatrix}
$$

이라고 하자. 그러면 $T^*T$의 행렬은

$$
\begin{pmatrix}
1 & 1 & 0 & 0\cr
1 & 1 & 0 & 0\cr
0 & 0 & 0 & 0\cr
0 & 0 & 0 & 25
\end{pmatrix}
$$

이고, $T^*T$의 고윳값은 $25,2,0$이며

$$
\dim E(25,T^*T)=1,\qquad
\dim E(2,T^*T)=1,\qquad
\dim E(0,T^*T)=2.
$$

따라서 $T$의 특이값은

$$
5,\sqrt2,0,0
$$

이다.

**7.68 양의 특이값의 역할**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) $T$가 단사인 것과 $0$이 $T$의 특이값이 아닌 것은 동치이다.

(b) $T$의 양의 특이값의 개수는 $\dim\text{range}T$와 같다.

(c) $T$가 전사인 것과 $T$의 양의 특이값의 개수가 $\dim W$와 같은 것은 동치이다.

**증명**

$T$가 단사인 것은 $\text{null}T=\lbrace0\rbrace$인 것과 동치이고, 7.64(b)에 의해 이는 $\text{null}T^*T=\lbrace0\rbrace$인 것과 동치이다. 이는 $0$이 $T^*T$의 고윳값이 아닌 것과 동치이며, 곧 $0$이 $T$의 특이값이 아닌 것과 동치이다.

$T^*T$에 스펙트럼 정리를 적용하면 $\dim\text{range}T^*T$는 $T^*T$의 양의 고윳값의 개수와 같다. 7.64(d)에 의해 이는 $\dim\text{range}T$와 같으므로 (b)가 성립한다. (c)는 (b)와 2.39에서 따른다.

고윳값과 특이값을 비교하면 다음과 같다.

| 고윳값의 리스트                                             | 특이값의 리스트                                          |
| ----------------------------------------------------------- | -------------------------------------------------------- |
| 벡터공간의 맥락                                             | 내적공간의 맥락                                          |
| 한 벡터공간에서 자기 자신으로 가는 선형사상에 대해서만 정의 | 한 내적공간에서 다른 내적공간으로 가는 선형사상에도 정의 |
| 임의의 실수 또는 복소수일 수 있음                           | 음이 아닌 수                                             |
| $\mathbb{F}=\mathbb{R}$이면 빈 리스트일 수 있음             | 리스트의 길이는 정의역의 차원과 같음                     |
| $0$을 포함하는 것은 연산자가 가역이 아님과 동치             | $0$을 포함하는 것은 선형사상이 단사가 아님과 동치        |
| 표준적인 순서가 없음                                        | 항상 큰 것부터 나열                                      |

**7.69 등거리사상은 모든 특이값이 $1$인 것으로 특성화된다**

$S\in\mathcal{L}(V,W)$라고 하자. 그러면

$$
S\text{가 등거리사상}
\Longleftrightarrow
S\text{의 모든 특이값이 }1.
$$

**증명**

$$
\begin{aligned}
S\text{가 등거리사상}
&\Longleftrightarrow S^*S=I\cr
&\Longleftrightarrow S^*S\text{의 모든 고윳값이 }1\cr
&\Longleftrightarrow S\text{의 모든 특이값이 }1.
\end{aligned}
$$

첫 동치는 7.49에서, 둘째 동치는 자기수반 연산자 $S^*S$에 대한 스펙트럼 정리에서 따른다.

### 선형사상과 행렬의 특이값분해

특이값분해는 자주 SVD라고 불리며, 계산 선형대수에서 매우 유용하다. 다음 결과는 $V$에서 $W$로 가는 모든 선형사상이 특이값과 두 정규직교 리스트를 통해 매우 깔끔하게 표현됨을 보여 준다.

**7.70 특이값분해**

$T\in\mathcal{L}(V,W)$이고 $T$의 양의 특이값이 $s_1,\ldots,s_m$이라고 하자. 그러면 $V$의 정규직교 리스트 $e_1,\ldots,e_m$과 $W$의 정규직교 리스트 $f_1,\ldots,f_m$이 존재하여 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
\tag{7.71}
$$

가 성립한다.

**증명**

$T$의 모든 특이값을 $s_1,\ldots,s_n$이라고 쓰자. 여기서 $n=\dim V$이다. $T^*T$는 양의 연산자이므로, 스펙트럼 정리에 의해 $V$의 정규직교기저 $e_1,\ldots,e_n$이 존재하여 각 $k=1,\ldots,n$에 대해

$$
T^*T e_k=s_k^2e_k
\tag{7.72}
$$

가 성립한다. $k=1,\ldots,m$에 대해

$$
f_k=\frac{Te_k}{s_k}
\tag{7.73}
$$

로 정의한다. 그러면 $j,k\in\lbrace1,\ldots,m\rbrace$에 대해

$$
\begin{aligned}
\langle f_j,f_k\rangle
&=\frac{1}{s_js_k}\langle Te_j,Te_k\rangle\cr
&=\frac{1}{s_js_k}\langle e_j,T^*Te_k\rangle\cr
&=\frac{s_k}{s_j}\langle e_j,e_k\rangle\cr
&=
\begin{cases}
0, & j\ne k,\cr
1, & j=k.
\end{cases}
\end{aligned}
$$

따라서 $f_1,\ldots,f_m$은 $W$의 정규직교 리스트이다. $k>m$이면 $s_k=0$이고, (7.72)에 의해 $T^*Te_k=0$이다. 7.64(b)에 의해 $Te_k=0$이다. 이제 $v\in V$이면

$$
\begin{aligned}
Tv
&=T(\langle v,e_1\rangle e_1+\cdots+\langle v,e_n\rangle e_n)\cr
&=\langle v,e_1\rangle Te_1+\cdots+\langle v,e_m\rangle Te_m\cr
&=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m.
\end{aligned}
$$

원하는 특이값분해를 얻었다.

위 특이값분해에서 $e_1,\ldots,e_m$을 $V$의 정규직교기저로, $f_1,\ldots,f_m$을 $W$의 정규직교기저로 확장하면, 그 두 기저에 대한 $T$의 행렬은 대각선에 $s_1,\ldots,s_m$이 있고 나머지는 $0$인 매우 단순한 형태가 된다. 정사각행렬이 아닌 경우에도 다음 정의를 쓰면, 모든 선형사상이 적절한 정규직교기저에 대해 대각행렬을 가진다고 말할 수 있다.

**7.74 정의: 대각행렬**

$M\times N$ 행렬 $A$가 $k=1,\ldots,\min\lbrace M,N\rbrace$에 대한 $A_{k,k}$를 제외한 모든 성분이 $0$이면 $A$를 **대각행렬**이라고 한다.

스펙트럼 정리와 특이값분해를 비교하면 다음과 같다.

| 스펙트럼 정리                                                                                 | 특이값분해                                                    |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| $\mathbb{F}=\mathbb{R}$일 때 자기수반 연산자, $\mathbb{F}=\mathbb{C}$일 때 정규 연산자만 기술 | 한 내적공간에서 다른 내적공간으로 가는 임의의 선형사상을 기술 |
| 하나의 정규직교기저를 산출                                                                    | 정의역과 공역에서 각각 하나씩, 두 정규직교 리스트를 산출      |
| $\mathbb{F}=\mathbb{R}$인지 $\mathbb{F}=\mathbb{C}$인지에 따라 증명이 다름                    | 두 경우에 같은 증명이 작동                                    |

**7.75 수반과 유사역의 특이값분해**

$T\in\mathcal{L}(V,W)$이고 $T$의 양의 특이값이 $s_1,\ldots,s_m$이라고 하자. $V$의 정규직교 리스트 $e_1,\ldots,e_m$과 $W$의 정규직교 리스트 $f_1,\ldots,f_m$이 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
\tag{7.76}
$$

를 만족한다고 하자. 그러면 모든 $w\in W$에 대해

$$
T^*w=s_1\langle w,f_1\rangle e_1+\cdots+s_m\langle w,f_m\rangle e_m
\tag{7.77}
$$

이고

$$
T^\dagger w=
\frac{\langle w,f_1\rangle}{s_1}e_1+\cdots+
\frac{\langle w,f_m\rangle}{s_m}e_m.
\tag{7.78}
$$

**증명**

$v\in V$, $w\in W$이면

$$
\begin{aligned}
\langle Tv,w\rangle
&=\left\langle s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m,w\right\rangle\cr
&=s_1\langle v,e_1\rangle\langle f_1,w\rangle+\cdots+s_m\langle v,e_m\rangle\langle f_m,w\rangle\cr
&=\left\langle v,s_1\langle w,f_1\rangle e_1+\cdots+s_m\langle w,f_m\rangle e_m\right\rangle.
\end{aligned}
$$

따라서 (7.77)이 성립한다.

(7.78)을 보이자. $w\in W$에 대해

$$
v=
\frac{\langle w,f_1\rangle}{s_1}e_1+\cdots+
\frac{\langle w,f_m\rangle}{s_m}e_m
$$

라고 두면, (7.76)에 의해

$$
Tv=\langle w,f_1\rangle f_1+\cdots+\langle w,f_m\rangle f_m
=P_{\text{range}T}w.
$$

또한 $v\in(\text{null}T)^\perp$이다. 따라서 유사역의 정의(6.68)에 의해 $v=T^\dagger w$이다.

**7.79 예: 특이값분해 찾기**

$T\in\mathcal{L}(\mathbb{F}^4,\mathbb{F}^3)$를

$$
T(x_1,x_2,x_3,x_4)=(-5x_4,0,x_1+x_2)
$$

로 정의하자. 표준기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
0 & 0 & 0 & -5\cr
0 & 0 & 0 & 0\cr
1 & 1 & 0 & 0
\end{pmatrix}
$$

이다. 예 7.67에서 보았듯이 $T^*T$의 양의 고윳값은 $25,2$이고, 따라서 $T$의 양의 특이값은 $5,\sqrt2$이다.

$E(25,T^*T)$의 정규직교기저는 $(0,0,0,1)$이고, $E(2,T^*T)$의 정규직교기저는

$$
\left(\frac1{\sqrt2},\frac1{\sqrt2},0,0\right)
$$

이다. 따라서

$$
e_1=(0,0,0,1),\qquad
e_2=\left(\frac1{\sqrt2},\frac1{\sqrt2},0,0\right)
$$

로 두고

$$
f_1=\frac{Te_1}{5}=(-1,0,0),\qquad
f_2=\frac{Te_2}{\sqrt2}=(0,0,1)
$$

로 둔다. 그러면 $e_1,e_2$는 $\mathbb{F}^4$의 정규직교 리스트이고 $f_1,f_2$는 $\mathbb{F}^3$의 정규직교 리스트이며, 모든 $v\in\mathbb{F}^4$에 대해

$$
Tv=5\langle v,e_1\rangle f_1+\sqrt2\langle v,e_2\rangle f_2
$$

이다. 이것이 $T$의 특이값분해이다.

**7.80 SVD의 행렬 버전**

$A$가 랭크가 $m\ge 1$인 $p\times n$ 행렬이라고 하자. 그러면 열들이 정규직교인 $p\times m$ 행렬 $B$, 대각선 성분이 양수인 $m\times m$ 대각행렬 $D$, 열들이 정규직교인 $n\times m$ 행렬 $C$가 존재하여

$$
A=BDC^*
$$

가 성립한다.

**증명**

$T:\mathbb{F}^n\to\mathbb{F}^p$를 표준기저에 대한 행렬이 $A$인 선형사상이라고 하자. 그러면 $\dim\text{range}T=m$이다. $T$의 특이값분해를

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
\tag{7.81}
$$

라고 하자. $B$를 열들이 $f_1,\ldots,f_m$인 $p\times m$ 행렬, $D$를 대각선 성분이 $s_1,\ldots,s_m$인 $m\times m$ 대각행렬, $C$를 열들이 $e_1,\ldots,e_m$인 $n\times m$ 행렬로 둔다.

$u_1,\ldots,u_m$을 $\mathbb{F}^m$의 표준기저라고 하자. $k=1,\ldots,m$이면

$$
(AC-BD)u_k=Ae_k-B(s_ku_k)=s_kf_k-s_kf_k=0.
$$

따라서 $AC=BD$이다. 오른쪽에 $C^*$를 곱하면

$$
ACC^*=BDC^*.
$$

$C^*e_k=u_k$이고, (7.81)에 의해 $(\text{span}(e_1,\ldots,e_m))^\perp$에서는 $A$와 $ACC^*$가 모두 $0$으로 작용한다. 따라서 $ACC^*=A$이고, 원하는 $A=BDC^*$를 얻는다.

행렬 $A$는 $pn$개의 성분을 가지지만, $B,D,C$의 성분 수의 합은 $m(p+m+n)$이다. 따라서 $p,n$이 크고 랭크 $m$이 이들보다 훨씬 작으면, $A$를 저장하는 대신 SVD의 세 행렬을 저장하면 훨씬 적은 정보를 저장해도 된다.

### 연습문제 7E

1. $T\in\mathcal{L}(V,W)$라고 하자. $T=0$인 것과 $T$의 모든 특이값이 $0$인 것은 동치임을 보여라.

2. $T\in\mathcal{L}(V,W)$이고 $s>0$이라고 하자. $s$가 $T$의 특이값인 것과, 영이 아닌 벡터 $v\in V$, $w\in W$가 존재하여

   $$
   Tv=sw,\qquad T^*w=sv
   $$

   를 만족하는 것은 동치임을 증명하여라. 두 방정식을 모두 만족하는 벡터 $v,w$는 슈미트 쌍이라고 불린다.

3. $0$이 유일한 고윳값이고 특이값이 $5,0$인 $T\in\mathcal{L}(\mathbb{C}^2)$의 예를 제시하여라.

4. $T\in\mathcal{L}(V,W)$이고 $s_1$이 $T$의 가장 큰 특이값, $s_n$이 가장 작은 특이값이라고 하자. 다음을 증명하여라.

   $$
   \lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert=1\rbrace=[s_n,s_1].
   $$

5. $T\in\mathcal{L}(\mathbb{C}^2)$가 $T(x,y)=(-4y,x)$로 정의되어 있다고 하자. $T$의 특이값을 구하여라.

6. 예 6.34의 내적이 주어진 $\mathcal{P}_2(\mathbb{R})$에서 $Dp=p'$로 정의되는 미분 연산자 $D\in\mathcal{L}(\mathcal{P}_2(\mathbb{R}))$의 특이값을 구하여라.

7. $T\in\mathcal{L}(V)$가 자기수반이거나, $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 정규라고 하자. $T$의 고윳값을 각 고유공간의 차원만큼 반복하여 $\lambda_1,\ldots,\lambda_n$이라고 하자. $T$의 특이값은 $|\lambda_1|,\ldots,|\lambda_n|$을 큰 것부터 정렬한 리스트임을 보여라.

8. $T\in\mathcal{L}(V,W)$라고 하자. $s_1\ge s_2\ge\cdots\ge s_m>0$이고, $e_1,\ldots,e_m$은 $V$의 정규직교 리스트, $f_1,\ldots,f_m$은 $W$의 정규직교 리스트이며, 모든 $v\in V$에 대해

   $$
   Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
   $$

   라고 하자.

   (a) $f_1,\ldots,f_m$은 $\text{range}T$의 정규직교기저임을 증명하여라.

   (b) $e_1,\ldots,e_m$은 $(\text{null}T)^\perp$의 정규직교기저임을 증명하여라.

   (c) $s_1,\ldots,s_m$이 $T$의 양의 특이값임을 증명하여라.

   (d) $k\in\lbrace1,\ldots,m\rbrace$이면 $e_k$는 고윳값 $s_k^2$에 대응하는 $T^*T$의 고유벡터임을 증명하여라.

   (e) 모든 $w\in W$에 대해

   $$
   TT^*w=s_1^2\langle w,f_1\rangle f_1+\cdots+s_m^2\langle w,f_m\rangle f_m
   $$

   임을 증명하여라.

9. $T\in\mathcal{L}(V,W)$라고 하자. $T$와 $T^*$는 같은 양의 특이값을 가짐을 보여라.

10. $T\in\mathcal{L}(V,W)$의 특이값이 $s_1,\ldots,s_n$이라고 하자. $T$가 가역이면 $T^{-1}$의 특이값은

    $$
    \frac1{s_n},\ldots,\frac1{s_1}
    $$

    임을 증명하여라.

11. $T\in\mathcal{L}(V,W)$이고 $v_1,\ldots,v_n$이 $V$의 정규직교기저라고 하자. $T$의 특이값을 $s_1,\ldots,s_n$이라고 하자.

    (a)

    $$
    \Vert Tv_1\Vert^2+\cdots+\Vert Tv_n\Vert^2=s_1^2+\cdots+s_n^2
    $$

    임을 증명하여라.

    (b) $W=V$이고 $T$가 양의 연산자이면

    $$
    \langle Tv_1,v_1\rangle+\cdots+\langle Tv_n,v_n\rangle=s_1+\cdots+s_n
    $$

    임을 증명하여라.

12. (a) 유한차원 벡터공간과 그 위의 연산자 $T$ 중에서 $T^2$의 특이값이 $T$의 특이값들의 제곱과 같지 않은 예를 제시하여라.

    (b) $T\in\mathcal{L}(V)$가 정규이면 $T^2$의 특이값은 $T$의 특이값들의 제곱임을 증명하여라.

13. $T_1,T_2\in\mathcal{L}(V)$라고 하자. $T_1$과 $T_2$가 같은 특이값을 가지는 것과, 유니터리 연산자 $S_1,S_2\in\mathcal{L}(V)$가 존재하여

    $$
    T_1=S_1T_2S_2
    $$

    가 되는 것은 동치임을 증명하여라.

14. $T\in\mathcal{L}(V,W)$라고 하자. $s_n$을 $T$의 가장 작은 특이값이라고 하자. 모든 $v\in V$에 대해

    $$
    s_n\Vert v\Vert\le \Vert Tv\Vert
    $$

    임을 증명하여라.

15. $T\in\mathcal{L}(V)$이고 $s_1\ge\cdots\ge s_n$이 $T$의 특이값이라고 하자. $\lambda$가 $T$의 고윳값이면

    $$
    s_1\ge |\lambda|\ge s_n
    $$

    임을 증명하여라.

16. $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

    $$
    (T^*)^\dagger=(T^\dagger)^*.
    $$

17. $T\in\mathcal{L}(V)$라고 하자. $T$가 자기수반인 것과 $T^\dagger$가 자기수반인 것은 동치임을 증명하여라.

> 행렬이 펼쳐지고  
> 특이값은 별처럼 빛나  
> 혼돈 속 질서
>
> -- ChatGPT가 쓴 특이값분해에 관한 하이쿠 --

## 7F 특이값분해의 결과들

### 선형사상의 노름

특이값분해는 $\Vert Tv\Vert$에 대한 다음 상계를 준다.

**7.82 $\Vert Tv\Vert$의 상계**

$T\in\mathcal{L}(V,W)$라고 하자. $s_1$을 $T$의 가장 큰 특이값이라고 하자. 그러면 모든 $v\in V$에 대해

$$
\Vert Tv\Vert\le s_1\Vert v\Vert.
$$

**증명**

$s_1,\ldots,s_m$을 $T$의 양의 특이값이라고 하고, $e_1,\ldots,e_m$과 $f_1,\ldots,f_m$을 $T$의 특이값분해를 주는 정규직교 리스트라고 하자. 즉 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
\tag{7.83}
$$

이다. 그러면

$$
\begin{aligned}
\Vert Tv\Vert^2
&=s_1^2|\langle v,e_1\rangle|^2+\cdots+s_m^2|\langle v,e_m\rangle|^2\cr
&\le s_1^2\left(|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_m\rangle|^2\right)\cr
&\le s_1^2\Vert v\Vert^2.
\end{aligned}
$$

마지막 부등식은 베셀 부등식(6.26)에서 따른다. 양변의 제곱근을 취하면 원하는 부등식을 얻는다.

위 결과는 $\Vert v\Vert\le 1$인 모든 $v\in V$에 대해

$$
\Vert Tv\Vert\le s_1
\tag{7.84}
$$

임을 뜻한다. 또한 (7.83)에서 $v=e_1$을 대입하면 $Te_1=s_1f_1$이고, 따라서 $\Vert Te_1\Vert=s_1$이다. 그러므로

$$
\max\lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert\le 1\rbrace=s_1.
\tag{7.85}
$$

이 등식은 다음 정의의 동기이다.

**7.86 정의: 선형사상의 노름, $\Vert\cdot\Vert$**

$T\in\mathcal{L}(V,W)$라고 하자. $T$의 **노름** $\Vert T\Vert$는

$$
\Vert T\Vert=\max\lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert\le 1\rbrace
$$

로 정의된다.

일반적으로 음이 아닌 수들의 무한집합의 최댓값은 존재하지 않을 수 있다. 그러나 위 논의는 선형사상 $T$의 노름 정의에 나타나는 최댓값이 실제로 존재하고, $T$의 가장 큰 특이값과 같음을 보여 준다.

이제 노름이라는 단어와 기호 $\Vert\cdot\Vert$가 두 가지 방식으로 쓰인다. 하나는 내적공간의 벡터 $v$에 대해 $\Vert v\Vert=\sqrt{\langle v,v\rangle}$로 정의되는 노름이고, 다른 하나는 선형사상 $T$에 대해 정의한 $\Vert T\Vert$이다. 문맥과 기호를 보면 어떤 의미인지 구분할 수 있어야 한다.

**7.87 선형사상 노름의 기본 성질**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) $\Vert T\Vert\ge 0$.

(b) $\Vert T\Vert=0$인 것과 $T=0$인 것은 동치이다.

(c) 모든 $\lambda\in\mathbb{F}$에 대해

$$
\Vert\lambda T\Vert=|\lambda|\Vert T\Vert.
$$

(d) 모든 $S\in\mathcal{L}(V,W)$에 대해

$$
\Vert S+T\Vert\le \Vert S\Vert+\Vert T\Vert.
$$

**증명**

(a)는 정의에서 바로 나온다. (b)에서 $\Vert T\Vert=0$이면 $\Vert v\Vert\le 1$인 모든 $v$에 대해 $Tv=0$이다. 임의의 영이 아닌 $u\in V$에 대해 $u/\Vert u\Vert$의 노름은 $1$이므로

$$
Tu=\Vert u\Vert T\left(\frac{u}{\Vert u\Vert}\right)=0.
$$

따라서 $T=0$이다. 반대방향은 명백하다.

(c)는

$$
\begin{aligned}
\Vert\lambda T\Vert
&=\max\lbrace\Vert\lambda Tv\Vert:v\in V,\ \Vert v\Vert\le 1\rbrace\cr
&=|\lambda|\max\lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert\le 1\rbrace\cr
&=|\lambda|\Vert T\Vert
\end{aligned}
$$

에서 따른다.

(d) $\Vert S+T\Vert=\Vert(S+T)v\Vert$이고 $\Vert v\Vert\le 1$인 $v\in V$를 택한다. 그러면

$$
\Vert S+T\Vert
=\Vert Sv+Tv\Vert
\le \Vert Sv\Vert+\Vert Tv\Vert
\le \Vert S\Vert+\Vert T\Vert.
$$

**7.88 $\Vert T\Vert$의 다른 공식들**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) $\Vert T\Vert$는 $T$의 가장 큰 특이값이다.

(b)

$$
\Vert T\Vert=\max\lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert=1\rbrace.
$$

(c) $\Vert T\Vert$는 모든 $v\in V$에 대해

$$
\Vert Tv\Vert\le c\Vert v\Vert
$$

가 성립하게 하는 가장 작은 수 $c$이다.

**증명**

(a)는 (7.85)이다. (b)는 $0<\Vert v\Vert\le 1$이면 $u=v/\Vert v\Vert$가 $\Vert u\Vert=1$을 만족하고

$$
\Vert Tu\Vert=\frac{\Vert Tv\Vert}{\Vert v\Vert}\ge \Vert Tv\Vert
$$

이므로, 최댓값을 찾을 때 노름이 $1$인 벡터만 보아도 된다는 사실에서 따른다.

(c) $v\ne 0$이면 정의에서

$$
\left\Vert T\left(\frac{v}{\Vert v\Vert}\right)\right\Vert\le \Vert T\Vert
$$

이고, 따라서

$$
\Vert Tv\Vert\le \Vert T\Vert\thinspace\Vert v\Vert.
\tag{7.89}
$$

반대로 어떤 $c$가 모든 $v\in V$에 대해 $\Vert Tv\Vert\le c\Vert v\Vert$를 만족하면, $\Vert v\Vert\le 1$인 모든 $v$에 대해 $\Vert Tv\Vert\le c$이다. 최댓값을 취하면 $\Vert T\Vert\le c$이다.

**7.90 예: 노름**

- $I$가 $V$ 위의 항등연산자이면 $\Vert I\Vert=1$이다.
- $T\in\mathcal{L}(\mathbb{F}^n)$의 표준기저에 대한 행렬의 모든 성분이 $1$이면 $\Vert T\Vert=n$이다.
- $T\in\mathcal{L}(V)$이고 $V$가 $T$의 고유벡터들로 이루어진 정규직교기저를 가지며 대응하는 고윳값이 $\lambda_1,\ldots,\lambda_n$이면, $\Vert T\Vert$는 $|\lambda_1|,\ldots,|\lambda_n|$ 중 최댓값이다.
- $T\in\mathcal{L}(\mathbb{R}^5)$의 표준기저에 대한 행렬이 $j$행 $k$열 성분 $\frac1{j^2+k}$를 가지는 $5\times 5$ 행렬이라고 하자. 표준 수학 소프트웨어는 $T$의 가장 큰 특이값이 대략 $0.8$이고 가장 작은 특이값이 대략 $10^{-6}$임을 보여 준다. 따라서 $\Vert T\Vert\approx 0.8$이고 $\Vert T^{-1}\Vert\approx 10^6$이다. 이 노름들의 정확한 공식은 구할 수 없다.

**7.91 수반의 노름**

$T\in\mathcal{L}(V,W)$라고 하자. 그러면

$$
\Vert T^*\Vert=\Vert T\Vert.
$$

**증명**

$w\in W$이면

$$
\begin{aligned}
\Vert T^*w\Vert^2
&=\langle T^*w,T^*w\rangle\cr
&=\langle TT^*w,w\rangle\cr
&\le \Vert TT^*w\Vert\thinspace\Vert w\Vert\cr
&\le \Vert T\Vert\thinspace\Vert T^*w\Vert\thinspace\Vert w\Vert.
\end{aligned}
$$

따라서 $\Vert T^*w\Vert\le \Vert T\Vert\thinspace\Vert w\Vert$이고, 7.88(c)에 의해 $\Vert T^*\Vert\le \Vert T\Vert$이다. 이제 이 부등식을 $T^*$에 적용하고 $(T^*)^*=T$를 사용하면 $\Vert T\Vert\le\Vert T^*\Vert$이다. 따라서 두 노름은 같다.

### 더 낮은 차원의 치역을 가진 선형사상으로 근사하기

다음 결과는 특이값분해의 놀라운 응용이다. 선형사상을 치역의 차원이 최대 $k$인 선형사상으로 가장 잘 근사하려면, 특이값분해에서 앞의 $k$개 항만 남기면 된다는 내용이다.

**7.92 치역 차원이 최대 $k$인 선형사상에 의한 최적 근사**

$T\in\mathcal{L}(V,W)$이고 $s_1\ge\cdots\ge s_m$이 $T$의 양의 특이값이라고 하자. $1\le k<m$이라고 하자. 그러면

$$
\min\lbrace\Vert T-S\Vert:S\in\mathcal{L}(V,W),\ \dim\text{range}S\le k\rbrace=s_{k+1}.
$$

또한

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
$$

이 $T$의 특이값분해이고 $T_k\in\mathcal{L}(V,W)$를

$$
T_kv=s_1\langle v,e_1\rangle f_1+\cdots+s_k\langle v,e_k\rangle f_k
$$

로 정의하면, $\dim\text{range}T_k=k$이고

$$
\Vert T-T_k\Vert=s_{k+1}.
$$

**증명**

$v\in V$이면

$$
\begin{aligned}
\Vert(T-T_k)v\Vert^2
&=\Vert s_{k+1}\langle v,e_{k+1}\rangle f_{k+1}+\cdots+s_m\langle v,e_m\rangle f_m\Vert^2\cr
&=s_{k+1}^2|\langle v,e_{k+1}\rangle|^2+\cdots+s_m^2|\langle v,e_m\rangle|^2\cr
&\le s_{k+1}^2\left(|\langle v,e_{k+1}\rangle|^2+\cdots+|\langle v,e_m\rangle|^2\right)\cr
&\le s_{k+1}^2\Vert v\Vert^2.
\end{aligned}
$$

따라서 $\Vert T-T_k\Vert\le s_{k+1}$이다. 또한 $(T-T_k)e_{k+1}=s_{k+1}f_{k+1}$이므로 $\Vert T-T_k\Vert=s_{k+1}$이다.

이제 $S\in\mathcal{L}(V,W)$이고 $\dim\text{range}S\le k$라고 하자. 그러면 $Se_1,\ldots,Se_{k+1}$은 길이가 $k+1$인 일차종속 리스트이다. 따라서 모두 $0$이 아닌 것은 아닌 스칼라 $a_1,\ldots,a_{k+1}$가 존재하여

$$
a_1Se_1+\cdots+a_{k+1}Se_{k+1}=0
$$

이다. 벡터 $a_1e_1+\cdots+a_{k+1}e_{k+1}$는 $0$이 아니며,

$$
\begin{aligned}
&\Vert(T-S)(a_1e_1+\cdots+a_{k+1}e_{k+1})\Vert^2\cr
&\quad=\Vert T(a_1e_1+\cdots+a_{k+1}e_{k+1})\Vert^2\cr
&\quad=\Vert s_1a_1f_1+\cdots+s_{k+1}a_{k+1}f_{k+1}\Vert^2\cr
&\quad=s_1^2|a_1|^2+\cdots+s_{k+1}^2|a_{k+1}|^2\cr
&\quad\ge s_{k+1}^2(|a_1|^2+\cdots+|a_{k+1}|^2)\cr
&\quad=s_{k+1}^2\Vert a_1e_1+\cdots+a_{k+1}e_{k+1}\Vert^2.
\end{aligned}
$$

따라서 $\Vert T-S\Vert\ge s_{k+1}$이다. 결국 $T_k$가 최적 근사이다.

### 극분해

$0$이 아닌 복소수 $z$는

$$
z=\frac{z}{|z|}|z|=\frac{z}{|z|}\sqrt{\overline z z}
$$

로 쓸 수 있다. 첫 번째 인수 $z/|z|$의 절댓값은 $1$이다. 이와 유사하게 모든 연산자는 유니터리 연산자와 양의 연산자의 곱으로 쓸 수 있다.

$T\in\mathcal{L}(V)$이면 $T^*T$는 양의 연산자이므로 $\sqrt{T^*T}$가 잘 정의된다.

**7.93 극분해**

$T\in\mathcal{L}(V)$라고 하자. 그러면 어떤 유니터리 연산자 $S\in\mathcal{L}(V)$가 존재하여

$$
T=S\sqrt{T^*T}
$$

가 성립한다.

**증명**

$s_1,\ldots,s_m$을 $T$의 양의 특이값이라고 하고, $e_1,\ldots,e_m$과 $f_1,\ldots,f_m$을 $V$의 정규직교 리스트로서 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m
\tag{7.94}
$$

를 만족한다고 하자. 이 두 리스트를 각각 $V$의 정규직교기저 $e_1,\ldots,e_n$과 $f_1,\ldots,f_n$으로 확장한다. $S\in\mathcal{L}(V)$를

$$
Sv=\langle v,e_1\rangle f_1+\cdots+\langle v,e_n\rangle f_n
$$

으로 정의한다. 그러면

$$
\Vert Sv\Vert^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2=\Vert v\Vert^2
$$

이므로 $S$는 유니터리 연산자이다.

(7.94)에 $T^*$를 적용하고 7.77을 사용하면

$$
T^*Tv=s_1^2\langle v,e_1\rangle e_1+\cdots+s_m^2\langle v,e_m\rangle e_m.
$$

따라서

$$
\sqrt{T^*T}v=s_1\langle v,e_1\rangle e_1+\cdots+s_m\langle v,e_m\rangle e_m
$$

이다. 이제

$$
\begin{aligned}
S\sqrt{T^*T}v
&=S(s_1\langle v,e_1\rangle e_1+\cdots+s_m\langle v,e_m\rangle e_m)\cr
&=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m\cr
&=Tv.
\end{aligned}
$$

따라서 $T=S\sqrt{T^*T}$이다.

### 타원체와 평행체에 연산자 적용하기

**7.95 정의: 공, $B$**

$0$을 중심으로 하고 반지름이 $1$인 $V$의 공 $B$는

$$
B=\lbrace v\in V:\Vert v\Vert<1\rbrace
$$

로 정의된다.

**7.96 정의: 타원체, $E(s_1f_1,\ldots,s_nf_n)$, 주축**

$f_1,\ldots,f_n$이 $V$의 정규직교기저이고 $s_1,\ldots,s_n$이 양수라고 하자. 주축이 $s_1f_1,\ldots,s_nf_n$인 타원체 $E(s_1f_1,\ldots,s_nf_n)$는

$$
E(s_1f_1,\ldots,s_nf_n) =
\left\lbrace
v\in V:
\frac{|\langle v,f_1\rangle|^2}{s_1^2}
+\cdots+
\frac{|\langle v,f_n\rangle|^2}{s_n^2}<1
\right\rbrace
$$

로 정의된다.

특별히 $E(f_1,\ldots,f_n)$은 파르스발 등식 6.30(b)에 의해 $V$의 공 $B$와 같다.

**7.97 예: 타원체**

- $\mathbb{R}^2$의 표준기저 $f_1,f_2$에 대해 $E(2f_1,f_2)$는 $f_1$축 방향으로 두 배 늘어난 타원이다.
- $f_1=(1/\sqrt2,1/\sqrt2)$, $f_2=(-1/\sqrt2,1/\sqrt2)$인 경우 $E(2f_1,f_2)$는 회전된 타원이다.
- $\mathbb{R}^3$의 표준기저 $f_1,f_2,f_3$에 대해 $E(4f_1,3f_2,2f_3)$는 세 주축의 길이가 각각 $4,3,2$인 타원체이다.

**7.98 표기: $T(\Omega)$**

$T$가 $V$에서 정의된 함수이고 $\Omega\subset V$이면

$$
T(\Omega)=\lbrace Tv:v\in\Omega\rbrace
$$

로 정의한다. 따라서 $T(V)=\text{range}T$이다.

**7.99 가역 연산자는 공을 타원체로 보낸다**

$T\in\mathcal{L}(V)$가 가역이라고 하자. 그러면 $T$는 $V$의 공 $B$를 $V$의 어떤 타원체 위로 보낸다.

**증명**

$T$의 특이값분해가 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_n\langle v,e_n\rangle f_n
\tag{7.100}
$$

라고 하자. 여기서 $s_1,\ldots,s_n$은 $T$의 특이값이고, $e_1,\ldots,e_n$과 $f_1,\ldots,f_n$은 모두 $V$의 정규직교기저이다. $T$가 가역이므로 특이값은 모두 양수이다. $v\in B$이면

$$
\frac{|\langle Tv,f_1\rangle|^2}{s_1^2}
+\cdots+
\frac{|\langle Tv,f_n\rangle|^2}{s_n^2}
=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2<1.
$$

따라서 $Tv\in E(s_1f_1,\ldots,s_nf_n)$이다.

반대로 $w\in E(s_1f_1,\ldots,s_nf_n)$라고 하자. 다음과 같이 둔다.

$$
v=\frac{\langle w,f_1\rangle}{s_1}e_1+\cdots+
\frac{\langle w,f_n\rangle}{s_n}e_n.
$$

그러면 $\Vert v\Vert<1$이고 (7.100)에 의해 $Tv=w$이다. 따라서

$$
T(B)=E(s_1f_1,\ldots,s_nf_n).
$$

**7.101 가역 연산자는 타원체를 타원체로 보낸다**

$T\in\mathcal{L}(V)$가 가역이고 $E$가 $V$의 타원체라고 하자. 그러면 $T(E)$는 $V$의 타원체이다.

**증명**

$E=E(s_1f_1,\ldots,s_nf_n)$이라고 하자. $S\in\mathcal{L}(V)$를

$$
S(a_1f_1+\cdots+a_nf_n)=a_1s_1f_1+\cdots+a_ns_nf_n
$$

로 정의하면 $S$는 공 $B$를 $E$ 위로 보낸다. 따라서

$$
T(E)=T(S(B))=(TS)(B).
$$

$TS$는 가역이므로 7.99에 의해 $(TS)(B)$는 타원체이다.

**7.102 정의: $P(v_1,\ldots,v_n)$, 평행체**

$v_1,\ldots,v_n$이 $V$의 기저라고 하자.

$$
P(v_1,\ldots,v_n)
=\lbrace a_1v_1+\cdots+a_nv_n:a_1,\ldots,a_n\in(0,1)\rbrace.
$$

어떤 $u\in V$에 대해 $u+P(v_1,\ldots,v_n)$ 꼴인 집합을 **평행체**라고 한다. 벡터 $v_1,\ldots,v_n$을 이 평행체의 변이라고 부른다.

**7.103 예: 평행체**

- $\mathbb{R}^2$에서 $(0.3,0.5)+P((1,0),(1,1))$는 평행사변형이다.
- $\mathbb{R}^3$의 평행체는 보통의 기울어진 상자 모양이다.

**7.104 가역 연산자는 평행체를 평행체로 보낸다**

$u\in V$이고 $v_1,\ldots,v_n$이 $V$의 기저이며 $T\in\mathcal{L}(V)$가 가역이라고 하자. 그러면

$$
T(u+P(v_1,\ldots,v_n))
=Tu+P(Tv_1,\ldots,Tv_n).
$$

**증명**

$T$가 가역이므로 $Tv_1,\ldots,Tv_n$은 $V$의 기저이다. 또한 모든 $a_1,\ldots,a_n\in(0,1)$에 대해

$$
T(u+a_1v_1+\cdots+a_nv_n)
=Tu+a_1Tv_1+\cdots+a_nTv_n.
$$

따라서 결론이 따른다.

**7.105 정의: 상자**

$V$의 **상자**는

$$
u+P(r_1e_1,\ldots,r_ne_n)
$$

꼴의 집합이다. 여기서 $u\in V$, $r_1,\ldots,r_n$은 양수이고 $e_1,\ldots,e_n$은 $V$의 정규직교기저이다.

**7.106 예: 상자**

- $e_1=(1/\sqrt2,1/\sqrt2)$, $e_2=(-1/\sqrt2,1/\sqrt2)$일 때 $(1,0)+P(\sqrt2e_1,\sqrt2e_2)$는 $\mathbb{R}^2$의 회전된 직사각형이다.
- $\mathbb{R}^3$의 표준기저 $e_1,e_2,e_3$에 대해 $P(e_1,2e_2,e_3)$는 세 변의 길이가 $1,2,1$인 상자이다.

**7.107 모든 가역 연산자는 어떤 상자들을 상자로 보낸다**

$T\in\mathcal{L}(V)$가 가역이라고 하자. $T$의 특이값분해가 모든 $v\in V$에 대해

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_n\langle v,e_n\rangle f_n
$$

라고 하자. 여기서 $s_1,\ldots,s_n$은 $T$의 특이값이고 $e_1,\ldots,e_n$, $f_1,\ldots,f_n$은 $V$의 정규직교기저이다. 그러면 모든 양수 $r_1,\ldots,r_n$과 모든 $u\in V$에 대해 $T$는 상자

$$
u+P(r_1e_1,\ldots,r_ne_n)
$$

를 상자

$$
Tu+P(r_1s_1f_1,\ldots,r_ns_nf_n)
$$

위로 보낸다.

**증명**

$a_1,\ldots,a_n\in(0,1)$이면

$$
T(u+a_1r_1e_1+\cdots+a_nr_ne_n)
=Tu+a_1r_1s_1f_1+\cdots+a_nr_ns_nf_n.
$$

따라서 결론이 따른다.

### 특이값을 통한 부피

이 소절의 목표는 연산자가 정의역의 부분집합의 부피를 어떻게 바꾸는지 이해하는 것이다. 부피 개념은 선형대수보다 해석학에 속하므로, 여기서는 직관적인 의미의 부피만 사용한다. 이 직관적 논의는 해석학의 도구를 통해 엄밀하게 만들 수 있다.

부피에 대한 직관은 실 내적공간에서 가장 자연스럽다. 따라서 이 소절에서는 자주 $\mathbb{F}=\mathbb{R}$라고 가정한다. $\dim V=n$이면 부피란 $n$차원 부피를 뜻한다. $n=2$일 때는 보통 넓이라고 부르지만, 일관성을 위해 모든 차원에서 부피라고 부른다.

**7.108 정의: 상자의 부피**

$\mathbb{F}=\mathbb{R}$라고 하자. $u\in V$이고 $r_1,\ldots,r_n$이 양수이며 $e_1,\ldots,e_n$이 $V$의 정규직교기저이면

$$
\text{volume}(u+P(r_1e_1,\ldots,r_ne_n))
=r_1\times\cdots\times r_n.
$$

이 정의는 $\mathbb{R}^2$에서 직사각형의 넓이, $\mathbb{R}^3$에서 상자의 부피에 대한 익숙한 공식과 일치한다.

**7.109 정의: 부피**

$\mathbb{F}=\mathbb{R}$이고 $\Omega\subset V$라고 하자. $\Omega$의 부피 $\text{volume}\Omega$는 $\Omega$를 근사하는 서로소 상자들의 부피의 합으로 근사되는 값이다.

여기서는 직관적 정의만 사용한다. 적절히 좋은 부분집합들에 대해서는 해석학의 방법으로 기저 선택과 무관하고 서로소 합집합에 대해 가법적인 부피가 엄밀히 정의된다.

**7.110 예: 선형사상에 의한 부피 변화**

$T\in\mathcal{L}(\mathbb{R}^2)$를

$$
Tv=2\langle v,e_1\rangle e_1+\langle v,e_2\rangle e_2
$$

로 정의하자. 여기서 $e_1,e_2$는 $\mathbb{R}^2$의 표준기저이다. 이 선형사상은 $e_1$축 방향으로 벡터를 $2$배 늘리고 $e_2$축 방향은 그대로 둔다.

따라서 $T$는 각 상자의 너비를 $2$배로 만들고 높이는 그대로 두므로 각 상자의 부피를 $2$배로 만든다. 공을 근사하는 상자들의 합도 $T$에 의해 타원체를 근사하는 상자들의 합으로 바뀌므로, 이 예에서 $T$는 공의 부피를 $2$배로 바꾼다.

**7.111 부피는 특이값들의 곱만큼 변한다**

$\mathbb{F}=\mathbb{R}$이고 $T\in\mathcal{L}(V)$가 가역이며 $\Omega\subset V$라고 하자. 그러면

$$
\text{volume}T(\Omega) =
(\text{$T$의 특이값들의 곱})(\text{volume}\Omega).
$$

**증명**

$T$의 특이값분해를

$$
Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_n\langle v,e_n\rangle f_n
$$

라고 하자. 여기서 $e_1,\ldots,e_n$과 $f_1,\ldots,f_n$은 $V$의 정규직교기저이다. $\Omega$를

$$
u+P(r_1e_1,\ldots,r_ne_n)
$$

꼴의 상자들로 근사하자. 이 상자의 부피는 $r_1\times\cdots\times r_n$이다. 7.107에 의해 $T$는 이 상자를

$$
Tu+P(r_1s_1f_1,\ldots,r_ns_nf_n)
$$

으로 보낸다. 이 새 상자의 부피는

$$
(s_1\times\cdots\times s_n)(r_1\times\cdots\times r_n)
$$

이다. 따라서 $T$는 $\Omega$를 근사하는 각 상자의 부피를 $s_1\times\cdots\times s_n$배로 바꾸고, 전체 부피도 같은 비율로 바뀐다.

나중에 행렬식에 도달하면 $T$의 특이값들의 곱이 $|\det T|$와 같음을 보게 된다(9.60과 9.61).

### 고윳값으로 결정되는 정규 연산자의 성질

이 장을 마무리하며 다음 표를 제시한다. 맥락은 유한차원 복소 내적공간이다. 표의 첫 열은 정규 연산자가 가질 수 있는 성질이고, 둘째 열은 그 성질이 성립할 필요충분조건으로서 모든 고윳값이 들어가야 하는 $\mathbb{C}$의 부분집합이다. 첫 행의 가역성만은 정규라는 가정 없이도 성립한다.

| 정규 연산자의 성질  | 고윳값들이 포함되는 집합                      |
| ------------------- | --------------------------------------------- |
| 가역                | $\mathbb{C}\setminus\lbrace0\rbrace$                    |
| 자기수반            | $\mathbb{R}$                                  |
| 반자기수반          | $\lbrace\lambda\in\mathbb{C}:\text{Re}\lambda=0\rbrace$ |
| 직교사영            | $\lbrace0,1\rbrace$                                     |
| 양의 연산자         | $[0,\infty)$                                  |
| 유니터리            | $\lbrace\lambda\in\mathbb{C}:\Vert \lambda \Vert =1\rbrace$   |
| 노름이 $1$보다 작음 | $\lbrace\lambda\in\mathbb{C}:\Vert \lambda \Vert <1\rbrace$   |

### 연습문제 7F

1. $S,T\in\mathcal{L}(V,W)$이면 다음을 증명하여라.

   $$
   \big|\Vert S\Vert-\Vert T\Vert\big|\le \Vert S-T\Vert.
   $$

   이 부등식은 역삼각부등식이라고 불린다.

2. $T\in\mathcal{L}(V)$가 자기수반이거나, $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 정규라고 하자. 다음을 증명하여라.

   $$
   \Vert T\Vert=\max\lbrace|\lambda|:\lambda\text{는 }T\text{의 고윳값}\rbrace.
   $$

3. $T\in\mathcal{L}(V,W)$이고 $v\in V$라고 하자. 다음을 증명하여라.

   $$
   \Vert Tv\Vert=\Vert T\Vert\thinspace\Vert v\Vert
   \Longleftrightarrow
   T^*Tv=\Vert T\Vert^2v.
   $$

4. $T\in\mathcal{L}(V,W)$이고 $v\in V$, $\Vert Tv\Vert=\Vert T\Vert\thinspace\Vert v\Vert$라고 하자. $u\in V$이고 $\langle u,v\rangle=0$이면 $\langle Tu,Tv\rangle=0$임을 증명하여라.

5. $U$가 유한차원 내적공간이고 $T\in\mathcal{L}(V,U)$, $S\in\mathcal{L}(U,W)$라고 하자. 다음을 증명하여라.

   $$
   \Vert ST\Vert\le \Vert S\Vert\thinspace\Vert T\Vert.
   $$

6. 증명하거나 반례를 들어라. $S,T\in\mathcal{L}(V)$이면 $\Vert ST\Vert=\Vert TS\Vert$이다.

7. $S,T\in\mathcal{L}(V,W)$에 대해 $d(S,T)=\Vert S-T\Vert$로 정의하면 $d$가 $\mathcal{L}(V,W)$ 위의 거리가 됨을 보여라.

8. (a) $T\in\mathcal{L}(V)$이고 $\Vert I-T\Vert<1$이면 $T$가 가역임을 증명하여라.

   (b) $S\in\mathcal{L}(V)$가 가역이라고 하자. $T\in\mathcal{L}(V)$이고

   $$
   \Vert S-T\Vert<\frac1{\Vert S^{-1}\Vert}
   $$

   이면 $T$가 가역임을 증명하여라.

9. $T\in\mathcal{L}(V)$라고 하자. 모든 $\varepsilon>0$에 대해 가역 연산자 $S\in\mathcal{L}(V)$가 존재하여

   $$
   0<\Vert T-S\Vert<\varepsilon
   $$

   이 됨을 증명하여라.

10. $\dim V>1$이고 $T\in\mathcal{L}(V)$가 가역이 아니라고 하자. 모든 $\varepsilon>0$에 대해 가역이 아닌 $S\in\mathcal{L}(V)$가 존재하여

    $$
    0<\Vert T-S\Vert<\varepsilon
    $$

    이 됨을 증명하여라.

11. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 모든 $\varepsilon>0$에 대해 대각화가능 연산자 $S\in\mathcal{L}(V)$가 존재하여

    $$
    0<\Vert T-S\Vert<\varepsilon
    $$

    이 됨을 증명하여라.

12. $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. 다음을 보여라.

    $$
    \Vert\sqrt T\Vert=\sqrt{\Vert T\Vert}.
    $$

13. $S,T\in\mathcal{L}(V)$가 양의 연산자라고 하자. 다음을 보여라.

    $$
    \Vert S-T\Vert\le \max\lbrace\Vert S\Vert,\Vert T\Vert\rbrace\le \Vert S+T\Vert.
    $$

14. $U$와 $W$가 $V$의 부분공간이고 $\Vert P_U-P_W\Vert<1$이라고 하자. $\dim U=\dim W$임을 증명하여라.

15. $T\in\mathcal{L}(\mathbb{F}^3)$를

    $$
    T(z_1,z_2,z_3)=(z_3,2z_1,3z_2)
    $$

    로 정의한다. $T=S\sqrt{T^*T}$가 되게 하는 유니터리 연산자 $S\in\mathcal{L}(\mathbb{F}^3)$를 명시적으로 구하여라.

16. $S\in\mathcal{L}(V)$가 가역인 양의 연산자라고 하자. 어떤 $\delta>0$가 존재하여, 자기수반 연산자 $T\in\mathcal{L}(V)$가 $\Vert S-T\Vert<\delta$를 만족하면 $T$가 양의 연산자가 됨을 증명하여라.

17. $u\in V$이고 $\varphi_u$가 $\varphi_u(v)=\langle v,u\rangle$로 정의되는 $V$ 위의 선형함수라고 하자. 다음을 증명하여라.

    $$
    \Vert\varphi_u\Vert=\Vert u\Vert.
    $$

    여기서 스칼라체 $\mathbb{F}$는 $\langle\alpha,\beta\rangle=\alpha\overline{\beta}$가 주어진 내적공간으로 생각한다.

18. $e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $T\in\mathcal{L}(V,W)$라고 하자.

    (a) 다음을 증명하여라.

    $$
    \max\lbrace\Vert Te_1\Vert,\ldots,\Vert Te_n\Vert\rbrace
    \le \Vert T\Vert
    \le
    (\Vert Te_1\Vert^2+\cdots+\Vert Te_n\Vert^2)^{1/2}.
    $$

    (b) 다음 등식이 성립하는 것은 $\dim\text{range}T\le 1$인 것과 동치임을 증명하여라.

    $$
    \Vert T\Vert=(\Vert Te_1\Vert^2+\cdots+\Vert Te_n\Vert^2)^{1/2}.
    $$

19. $T\in\mathcal{L}(V,W)$이면 다음을 증명하여라.

    $$
    \Vert T^*T\Vert=\Vert T\Vert^2.
    $$

20. $T\in\mathcal{L}(V)$가 정규라고 하자. 모든 양의 정수 $k$에 대해 다음을 증명하여라.

    $$
    \Vert T^k\Vert=\Vert T\Vert^k.
    $$

21. $\dim V>1$이고 $\dim W>1$이라고 하자. $\mathcal{L}(V,W)$ 위의 노름은 내적에서 나오는 노름이 아님을 증명하여라. 즉 모든 $T\in\mathcal{L}(V,W)$에 대해

    $$
    \max\lbrace\Vert Tv\Vert:v\in V,\ \Vert v\Vert\le 1\rbrace=\sqrt{\langle T,T\rangle}
    $$

    가 되게 하는 $\mathcal{L}(V,W)$ 위의 내적은 존재하지 않음을 증명하여라.

22. $T\in\mathcal{L}(V,W)$라고 하자. $n=\dim V$이고 $s_1\ge\cdots\ge s_n$을 $T$의 특이값이라고 하자. $1\le k\le n$이면 다음을 증명하여라.

    $$
    \min\lbrace\Vert T|_U\Vert:U\text{는 }V\text{의 부분공간이고 }\dim U=k\rbrace = s_{n-k+1}.
    $$

23. $T\in\mathcal{L}(V,W)$라고 하자. $T$가 $V$와 $W$의 노름에서 오는 거리들에 대해 균등연속임을 보여라.

24. $T\in\mathcal{L}(V)$가 가역이라고 하자. 다음을 증명하여라.

    $$
    \Vert T^{-1}\Vert=\Vert T\Vert^{-1}
    \Longleftrightarrow
    \frac{T}{\Vert T\Vert}\text{는 유니터리 연산자이다}.
    $$

25. $u,x\in V$이고 $u\ne 0$이라고 하자. $T\in\mathcal{L}(V)$를 모든 $v\in V$에 대해 $Tv=\langle v,u\rangle x$로 정의한다. 모든 $v\in V$에 대해

    $$
    \sqrt{T^*T}\thinspace v=\frac{\Vert x\Vert}{\Vert u\Vert}\langle v,u\rangle u
    $$

    임을 증명하여라.

26. $T\in\mathcal{L}(V)$라고 하자. $T$가 가역인 것과, $T=S\sqrt{T^*T}$를 만족하는 유니터리 연산자 $S\in\mathcal{L}(V)$가 유일하게 존재하는 것은 동치임을 증명하여라.

27. $T\in\mathcal{L}(V)$이고 $s_1,\ldots,s_n$이 $T$의 특이값이라고 하자. $e_1,\ldots,e_n$과 $f_1,\ldots,f_n$이 $V$의 정규직교기저이고 모든 $v\in V$에 대해

    $$
    Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_n\langle v,e_n\rangle f_n
    $$

    라고 하자. $S\in\mathcal{L}(V)$를

    $$
    Sv=\langle v,e_1\rangle f_1+\cdots+\langle v,e_n\rangle f_n
    $$

    로 정의한다.

    (a) $S$가 유니터리이고

    $$
    \Vert T-S\Vert=\max\lbrace|s_1-1|,\ldots,|s_n-1|\rbrace
    $$

    임을 보여라.

    (b) $E\in\mathcal{L}(V)$가 유니터리이면 $\Vert T-E\Vert\ge\Vert T-S\Vert$임을 보여라.

28. $T\in\mathcal{L}(V)$라고 하자. 어떤 유니터리 연산자 $S\in\mathcal{L}(V)$가 존재하여

    $$
    T=\sqrt{TT^*}\thinspace S
    $$

    가 됨을 증명하여라.

29. $T\in\mathcal{L}(V)$라고 하자.

    (a) 극분해를 사용하여 어떤 유니터리 연산자 $S\in\mathcal{L}(V)$가 존재해

    $$
    TT^*=ST^*TS^*
    $$

    가 됨을 보여라.

    (b) (a)가 $T$와 $T^*$가 같은 특이값을 가진다는 사실을 어떻게 함의하는지 보여라.

30. $T\in\mathcal{L}(V)$이고 $S\in\mathcal{L}(V)$가 유니터리 연산자이며 $R\in\mathcal{L}(V)$가 양의 연산자이고 $T=SR$라고 하자. 다음을 증명하여라.

    $$
    R=\sqrt{T^*T}.
    $$

31. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$가 정규라고 하자. 어떤 유니터리 연산자 $S\in\mathcal{L}(V)$가 존재하여 $T=S\sqrt{T^*T}$이고, $S$와 $\sqrt{T^*T}$가 모두 $V$의 같은 정규직교기저에 대해 대각행렬을 가짐을 증명하여라.

32. $T\in\mathcal{L}(V,W)$이고 $T\ne 0$이라고 하자. $s_1,\ldots,s_m$을 $T$의 양의 특이값이라고 하자. $(\text{null}T)^\perp$의 정규직교기저 $e_1,\ldots,e_m$이 존재하여

    $$
    T\left(E\left(\frac{e_1}{s_1},\ldots,\frac{e_m}{s_m}\right)\right)
    $$

    가 $\text{range}T$에서 $0$을 중심으로 하고 반지름이 $1$인 공과 같음을 보여라.
