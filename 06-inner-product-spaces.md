# 6장 내적공간

벡터공간을 정의할 때 우리는 $\mathbb{R}^2$와 $\mathbb{R}^3$의 선형 구조, 즉 덧셈과 스칼라곱을 일반화했다. 길이와 각도 같은 기하학적 특징은 무시했다. 이런 생각들은 내적이라는 개념 안에 들어 있으며, 이 장에서 그것을 살펴본다.

모든 내적은 노름을 유도한다. 노름은 길이로 생각할 수 있다. 이 노름은 피타고라스 정리, 삼각부등식, 평행사변형 등식, 코시-슈바르츠 부등식 같은 핵심 성질을 만족한다.

유클리드 기하에서 수직인 벡터라는 개념은 내적공간의 맥락에서 직교 벡터라는 이름을 갖는다. 우리는 정규직교기저가 내적공간에서 매우 유용하다는 것을 보게 될 것이다. 그램-슈미트 절차는 그런 기저를 구성한다. 이 장은 이러한 도구들을 모아 최소화 문제를 푸는 것으로 끝난다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.
- $V$와 $W$는 $\mathbb{F}$ 위의 벡터공간을 뜻한다.

그림: 현재 존스 홉킨스 대학교의 일부인 George Peabody Library. 이 도서관은 James Sylvester(1814-1897)가 그 대학의 첫 수학 교수로 있을 때 문을 열었다. Sylvester의 저작에는 수학에서 matrix라는 단어를 처음 사용한 일이 포함된다.

## 6A 내적과 노름

### 내적

내적 개념의 동기를 얻기 위해, $\mathbb{R}^2$와 $\mathbb{R}^3$의 벡터를 원점을 시작점으로 하는 화살표로 생각하자. $\mathbb{R}^2$ 또는 $\mathbb{R}^3$에 있는 벡터 $v$의 길이를 $v$의 노름이라고 부르며 $\Vert v\Vert$로 나타낸다. 따라서 $v=(a,b)\in\mathbb{R}^2$이면

$$
\Vert v\Vert=\sqrt{a^2+b^2}
$$

이다. 마찬가지로 $v=(a,b,c)\in\mathbb{R}^3$이면

$$
\Vert v\Vert=\sqrt{a^2+b^2+c^2}
$$

이다.

더 높은 차원에서는 그림을 그릴 수 없지만, $\mathbb{R}^n$으로의 일반화는 쉽다. $x=(x_1,\ldots,x_n)\in\mathbb{R}^n$의 노름을

$$
\Vert x\Vert=\sqrt{x_1^2+\cdots+x_n^2}
$$

로 정의한다.

노름은 $\mathbb{R}^n$ 위에서 선형이 아니다. 논의 안에 선형성을 넣기 위해 점곱을 도입한다.

**6.1 정의: 점곱**

$x,y\in\mathbb{R}^n$에 대해, $x$와 $y$의 **점곱** $x\cdot y$를

$$
x\cdot y=x_1y_1+\cdots+x_ny_n
$$

으로 정의한다. 여기서 $x=(x_1,\ldots,x_n)$이고 $y=(y_1,\ldots,y_n)$이다.

벡터를 화살표가 아니라 점으로 생각한다면, $\Vert x\Vert$는 원점에서 점 $x$까지의 거리로 해석해야 한다.

$\mathbb{R}^n$의 두 벡터의 점곱은 벡터가 아니라 수이다. 모든 $x\in\mathbb{R}^n$에 대해

$$
x\cdot x=\Vert x\Vert^2
$$

임에 주목하라. 더 나아가 $\mathbb{R}^n$의 점곱은 다음 성질들을 가진다.

- 모든 $x\in\mathbb{R}^n$에 대해 $x\cdot x\ge 0$이다.
- $x\cdot x=0$일 필요충분조건은 $x=0$인 것이다.
- $y\in\mathbb{R}^n$을 고정하면, $x\in\mathbb{R}^n$을 $x\cdot y$로 보내는 $\mathbb{R}^n$에서 $\mathbb{R}$로 가는 사상은 선형이다.
- 모든 $x,y\in\mathbb{R}^n$에 대해 $x\cdot y=y\cdot x$이다.

내적은 점곱의 일반화이다. 이 시점에서 내적은 방금 논의한 점곱의 성질들을 추상화하여 정의될 것이라고 추측할 수 있다. 실수 벡터공간에 대해서는 이 추측이 맞다. 그러나 실수 벡터공간과 복소 벡터공간 모두에 유용한 정의를 만들기 위해서는, 정의를 내리기 전에 복소수 경우를 살펴봐야 한다.

$\lambda=a+bi$이고 $a,b\in\mathbb{R}$이면 다음을 떠올리자.

- $\lambda$의 절댓값 $|\lambda|$는 $|\lambda|=\sqrt{a^2+b^2}$로 정의된다.
- $\lambda$의 복소켤레 $\overline{\lambda}$는 $\overline{\lambda}=a-bi$로 정의된다.
- $|\lambda|^2=\lambda\overline{\lambda}$이다.

절댓값과 복소켤레의 정의와 기본 성질은 4장을 보라.

$z=(z_1,\ldots,z_n)\in\mathbb{C}^n$에 대해, $z$의 노름을

$$
\Vert z\Vert=\sqrt{|z_1|^2+\cdots+|z_n|^2}
$$

로 정의한다. $\Vert z\Vert$가 음이 아닌 수가 되기를 원하므로 절댓값이 필요하다. 다음에 주목하라.

$$
\Vert z\Vert^2=z_1\overline{z_1}+\cdots+z_n\overline{z_n}.
$$

$\mathbb{R}^n$에서 그랬던 것처럼 $\Vert z\Vert^2$를 $z$와 자기 자신의 내적으로 생각하고 싶다. 따라서 위 식은 $w=(w_1,\ldots,w_n)\in\mathbb{C}^n$와 $z$의 내적이

$$
w_1\overline{z_1}+\cdots+w_n\overline{z_n}
$$

이어야 함을 암시한다. $w$와 $z$의 역할을 바꾸면 위 표현은 복소켤레로 바뀐다. 따라서 $w$와 $z$의 내적은 $z$와 $w$의 내적의 복소켤레와 같아야 한다고 기대해야 한다. 이런 동기를 가지고, 이제 실수 또는 복소 벡터공간일 수 있는 $V$ 위의 내적을 정의할 준비가 되었다.

다음 정의에서 사용하는 표기에 대해 한 가지 주의하자. $\lambda\in\mathbb{C}$에 대해 $\lambda\ge 0$이라는 표기는 $\lambda$가 실수이고 음이 아니라는 뜻이다.

**6.2 정의: 내적**

$V$ 위의 **내적**은 $V$의 원소들의 각 순서쌍 $(u,v)$를 수 $\langle u,v\rangle\in\mathbb{F}$로 보내는 함수로, 다음 성질들을 가진다.

양의성:

$$
\langle v,v\rangle\ge 0
$$

가 모든 $v\in V$에 대해 성립한다.

정부호성:

$$
\langle v,v\rangle=0
$$

일 필요충분조건은 $v=0$인 것이다.

첫 번째 자리에서의 덧셈성:

$$
\langle u+v,w\rangle=\langle u,w\rangle+\langle v,w\rangle
$$

가 모든 $u,v,w\in V$에 대해 성립한다.

첫 번째 자리에서의 동차성:

$$
\langle \lambda u,v\rangle=\lambda\langle u,v\rangle
$$

가 모든 $\lambda\in\mathbb{F}$와 모든 $u,v\in V$에 대해 성립한다.

켤레대칭성:

$$
\langle u,v\rangle=\overline{\langle v,u\rangle}
$$

가 모든 $u,v\in V$에 대해 성립한다.

대부분의 수학자는 위와 같이 내적을 정의하지만, 많은 물리학자는 첫 번째 자리 대신 두 번째 자리에서 동차성을 요구하는 정의를 사용한다.

모든 실수는 자신의 복소켤레와 같다. 따라서 실수 벡터공간을 다룬다면 위의 마지막 조건에서 복소켤레를 생략하고, 모든 $u,v\in V$에 대해 $\langle u,v\rangle=\langle v,u\rangle$이라고 말하면 된다.

**6.3 예: 내적**

(a) $\mathbb{F}^n$ 위의 유클리드 내적은 모든 $(w_1,\ldots,w_n),(z_1,\ldots,z_n)\in\mathbb{F}^n$에 대해

$$
\langle (w_1,\ldots,w_n),(z_1,\ldots,z_n)\rangle
=w_1\overline{z_1}+\cdots+w_n\overline{z_n}
$$

으로 정의된다.

(b) $c_1,\ldots,c_n$이 양수이면, 모든 $(w_1,\ldots,w_n),(z_1,\ldots,z_n)\in\mathbb{F}^n$에 대해

$$
\langle (w_1,\ldots,w_n),(z_1,\ldots,z_n)\rangle
=c_1w_1\overline{z_1}+\cdots+c_nw_n\overline{z_n}
$$

로 $\mathbb{F}^n$ 위의 내적을 정의할 수 있다.

(c) 구간 $[-1,1]$ 위의 연속 실숫값 함수들의 벡터공간에 대해, 모든 연속 실숫값 함수 $f,g$에 대해

$$
\langle f,g\rangle=\int_{-1}^{1}fg
$$

로 내적을 정의할 수 있다.

(d) 모든 $p,q\in\mathcal{P}(\mathbb{R})$에 대해

$$
\langle p,q\rangle=p(0)q(0)+\int_{-1}^{1}p'q'
$$

로 $\mathcal{P}(\mathbb{R})$ 위의 내적을 정의할 수 있다.

(e) 모든 $p,q\in\mathcal{P}(\mathbb{R})$에 대해

$$
\langle p,q\rangle=\int_0^\infty p(x)q(x)e^{-x}\thinspace dx
$$

로 $\mathcal{P}(\mathbb{R})$ 위의 내적을 정의할 수 있다.

**6.4 정의: 내적공간**

**내적공간**은 벡터공간 $V$와 그 위의 내적으로 이루어진 것이다.

내적공간의 가장 중요한 예는 위 예 (a)의 유클리드 내적을 가진 $\mathbb{F}^n$이다. $\mathbb{F}^n$을 내적공간이라고 부르면, 달리 명시하지 않는 한 그 내적은 유클리드 내적이라고 가정해야 한다.

$V$와 $W$가 내적공간이라는 가정을 계속 반복하지 않기 위해 다음 가정을 둔다.

**6.5 표기: $V,W$**

이 장의 나머지와 다음 장에서 $V$와 $W$는 $\mathbb{F}$ 위의 내적공간을 뜻한다.

여기에는 약간의 언어 남용이 있다. 내적공간은 벡터공간과 그 벡터공간 위의 내적으로 이루어진 것이다. 벡터공간 $V$가 내적공간이라고 말할 때, 우리는 $V$ 위의 어떤 내적이 함께 주어져 있거나 문맥에서 분명하다고 생각한다. 벡터공간이 $\mathbb{F}^n$이면 그 내적은 유클리드 내적이다.

**6.6 내적의 기본 성질**

(a) 각 고정된 $v\in V$에 대해, $u\in V$를 $\langle u,v\rangle$로 보내는 함수는 $V$에서 $\mathbb{F}$로 가는 선형사상이다.

(b) 모든 $v\in V$에 대해 $\langle 0,v\rangle=0$이다.

(c) 모든 $v\in V$에 대해 $\langle v,0\rangle=0$이다.

(d) 모든 $u,v,w\in V$에 대해

$$
\langle u,v+w\rangle=\langle u,v\rangle+\langle u,w\rangle
$$

이다.

(e) 모든 $\lambda\in\mathbb{F}$와 모든 $u,v\in V$에 대해

$$
\langle u,\lambda v\rangle=\overline{\lambda}\langle u,v\rangle
$$

이다.

증명.

(a) $v\in V$에 대해 $u\mapsto\langle u,v\rangle$의 선형성은 내적 정의의 첫 번째 자리에서의 덧셈성과 동차성에서 따라온다.

(b) 모든 선형사상은 $0$을 $0$으로 보낸다. 따라서 (b)는 (a)에서 따라온다.

(c) $v\in V$이면 내적 정의의 켤레대칭성과 (b)에 의해

$$
\langle v,0\rangle=\overline{\langle 0,v\rangle}=\overline{0}=0.
$$

(d) $u,v,w\in V$라고 하자. 그러면

$$
\begin{aligned}
\langle u,v+w\rangle
&=\overline{\langle v+w,u\rangle} \cr
&=\overline{\langle v,u\rangle+\langle w,u\rangle} \cr
&=\overline{\langle v,u\rangle}+\overline{\langle w,u\rangle} \cr
&=\langle u,v\rangle+\langle u,w\rangle.
\end{aligned}
$$

(e) $\lambda\in\mathbb{F}$이고 $u,v\in V$라고 하자. 그러면

$$
\begin{aligned}
\langle u,\lambda v\rangle
&=\overline{\langle \lambda v,u\rangle} \cr
&=\overline{\lambda\langle v,u\rangle} \cr
&=\overline{\lambda}\thinspace\overline{\langle v,u\rangle} \cr
&=\overline{\lambda}\langle u,v\rangle.
\end{aligned}
$$

### 노름

내적을 정의하게 된 처음 동기는 $\mathbb{R}^2$와 $\mathbb{R}^3$의 벡터들의 노름이었다. 이제 각 내적이 노름을 결정한다는 것을 본다.

**6.7 정의: 노름, $\Vert v\Vert$**

$v\in V$에 대해, $v$의 **노름** $\Vert v\Vert$를

$$
\Vert v\Vert=\sqrt{\langle v,v\rangle}
$$

로 정의한다.

**6.8 예: 노름**

(a) $(z_1,\ldots,z_n)\in\mathbb{F}^n$이고 유클리드 내적을 사용하면

$$
\Vert(z_1,\ldots,z_n)\Vert=\sqrt{|z_1|^2+\cdots+|z_n|^2}.
$$

(b) $[-1,1]$ 위의 연속 실숫값 함수들의 벡터공간에서, 내적이 6.3(c)처럼 주어져 있고 $f$가 그 벡터공간의 원소이면

$$
\Vert f\Vert=\sqrt{\int_{-1}^{1}f^2}
$$

이다.

**6.9 노름의 기본 성질**

$v\in V$라고 하자.

(a) $\Vert v\Vert=0$일 필요충분조건은 $v=0$인 것이다.

(b) 모든 $\lambda\in\mathbb{F}$에 대해

$$
\Vert\lambda v\Vert=|\lambda|\Vert v\Vert
$$

이다.

증명.

(a) 원하는 결과는 $\langle v,v\rangle=0$일 필요충분조건이 $v=0$인 것에서 따라온다.

(b) $\lambda\in\mathbb{F}$라고 하자. 그러면

$$
\begin{aligned}
\Vert\lambda v\Vert^2
&=\langle \lambda v,\lambda v\rangle \cr
&=\lambda\langle v,\lambda v\rangle \cr
&=\lambda\overline{\lambda}\langle v,v\rangle \cr
&=|\lambda|^2\Vert v\Vert^2.
\end{aligned}
$$

이제 양변의 제곱근을 취하면 원하는 등식을 얻는다.

위 결과 (b)의 증명은 일반 원리를 보여 준다. 노름을 직접 다루는 것보다 노름의 제곱을 다루는 것이 보통 더 쉽다.

이제 중요한 정의에 도달한다.

**6.10 정의: 직교**

$\langle u,v\rangle=0$이면 두 벡터 $u,v\in V$를 **직교**한다고 한다.

orthogonal이라는 말은 "직각을 이룬"이라는 뜻의 그리스어에서 왔다. 위 정의에서 두 벡터의 순서는 중요하지 않다. $\langle u,v\rangle=0$일 필요충분조건은 $\langle v,u\rangle=0$인 것이기 때문이다. $u$와 $v$가 직교한다고 말하는 대신, $u$가 $v$에 직교한다고 말하기도 한다.

연습문제 15번은 $u,v$가 $\mathbb{R}^2$의 영이 아닌 벡터이면

$$
\langle u,v\rangle=\Vert u\Vert\thinspace\Vert v\Vert\cos\theta
$$

임을 증명하라고 한다. 여기서 $\theta$는 $u$와 $v$를 원점을 시작점으로 하는 화살표로 생각할 때 두 벡터 사이의 각도이다. 따라서 $\mathbb{R}^2$의 두 영이 아닌 벡터가 유클리드 내적에 대해 직교할 필요충분조건은 두 벡터 사이 각도의 코사인이 $0$인 것이며, 이는 평면기하의 보통 의미에서 두 벡터가 수직일 필요충분조건이다. 따라서 직교라는 말을 수직을 뜻하는 세련된 말로 생각할 수 있다.

직교성에 대한 연구를 쉬운 결과로 시작한다.

**6.11 직교성과 $0$**

(a) $0$은 $V$의 모든 벡터에 직교한다.

(b) $0$은 자기 자신에 직교하는 $V$의 유일한 벡터이다.

증명.

(a) 6.6(b)가 모든 $v\in V$에 대해 $\langle 0,v\rangle=0$이라고 말했음을 떠올리자.

(b) $v\in V$이고 $\langle v,v\rangle=0$이면, 내적의 정의에 의해 $v=0$이다.

특수한 경우 $V=\mathbb{R}^2$에 대해서 다음 정리는 3500년 전 바빌로니아에서 알려져 있었고, 그 뒤 2500년 전 그리스에서 다시 발견되어 증명되었다. 물론 아래 증명은 원래의 증명은 아니다.

**6.12 피타고라스 정리**

$u,v\in V$라고 하자. $u$와 $v$가 직교하면

$$
\Vert u+v\Vert^2=\Vert u\Vert^2+\Vert v\Vert^2
$$

이다.

증명. $\langle u,v\rangle=0$이라고 하자. 그러면

$$
\begin{aligned}
\Vert u+v\Vert^2
&=\langle u+v,u+v\rangle \cr
&=\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle \cr
&=\Vert u\Vert^2+\Vert v\Vert^2.
\end{aligned}
$$

$u,v\in V$이고 $v\ne 0$라고 하자. 우리는 $u$를 $v$의 스칼라배와 $v$에 직교하는 벡터 $w$의 합으로 쓰고 싶다.

$u$를 $v$의 스칼라배와 $v$에 직교하는 벡터의 합으로 나타내는 직교분해를 찾기 위해, 스칼라를 $c\in\mathbb{F}$라고 하자. 그러면

$$
u=cv+(u-cv).
$$

따라서 $v$가 $u-cv$에 직교하도록 $c$를 골라야 한다. 즉

$$
0=\langle u-cv,v\rangle=\langle u,v\rangle-c\Vert v\Vert^2
$$

가 되기를 원한다. 위 식은 $c$를 $\langle u,v\rangle/\Vert v\Vert^2$로 택해야 함을 보여 준다. 이렇게 $c$를 택하면

$$
u=\frac{\langle u,v\rangle}{\Vert v\Vert^2}v+
\left(u-\frac{\langle u,v\rangle}{\Vert v\Vert^2}v\right)
$$

로 쓸 수 있다. 위 식은 $u$를 $v$의 스칼라배와 $v$에 직교하는 벡터의 합으로 명시적으로 쓴다. 이를 확인하라. 따라서 다음 핵심 결과가 증명되었다.

**6.13 직교분해**

$u,v\in V$이고 $v\ne 0$라고 하자.

$$
c=\frac{\langle u,v\rangle}{\Vert v\Vert^2},
\quad
w=u-\frac{\langle u,v\rangle}{\Vert v\Vert^2}v
$$

라고 두자. 그러면

$$
u=cv+w
\quad\text{그리고}\quad
\langle w,v\rangle=0
$$

이다.

직교분해 6.13은 다음 결과인 코시-슈바르츠 부등식의 증명에 사용된다. 이 부등식은 수학에서 가장 중요한 부등식 중 하나이다.

**6.14 코시-슈바르츠 부등식**

$u,v\in V$라고 하자. 그러면

$$
|\langle u,v\rangle|\le \Vert u\Vert\thinspace\Vert v\Vert.
$$

이 부등식에서 등호가 성립할 필요충분조건은 $u,v$ 중 하나가 다른 하나의 스칼라배인 것이다.

증명. $v=0$이면 원하는 부등식의 양변이 모두 $0$이다. 따라서 $v\ne 0$이라고 가정해도 된다. 6.13이 주는 직교분해

$$
u=\frac{\langle u,v\rangle}{\Vert v\Vert^2}v+w
$$

를 생각하자. 여기서 $w$는 $v$에 직교한다. 피타고라스 정리에 의해

$$
\begin{aligned}
\Vert u\Vert^2
&=\left\Vert\frac{\langle u,v\rangle}{\Vert v\Vert^2}v\right\Vert^2+\Vert w\Vert^2 \cr
&=\frac{|\langle u,v\rangle|^2}{\Vert v\Vert^2}+\Vert w\Vert^2 \cr
&\ge \frac{|\langle u,v\rangle|^2}{\Vert v\Vert^2}.
\end{aligned}
\tag{6.15}
$$

이 부등식의 양변에 $\Vert v\Vert^2$를 곱하고 제곱근을 취하면 원하는 부등식을 얻는다.

오귀스탱-루이 코시(1789-1857)는 1821년에 6.16(a)를 증명했다. 코시의 제자인 빅토르 부냐콥스키(1804-1889)는 1859년에 6.16(b)와 같은 적분 부등식을 증명했다. 몇십 년 뒤 헤르만 슈바르츠(1843-1921)의 비슷한 발견이 더 많은 관심을 끌었고, 이 부등식의 이름으로 이어졌다.

위 문단의 증명은 코시-슈바르츠 부등식에서 등호가 성립할 필요충분조건이 (6.15)에서 등호가 성립하는 것임을 보여 준다. 이는 $w=0$일 필요충분조건이다. 그런데 6.13에 의해 $w=0$일 필요충분조건은 $u$가 $v$의 배수인 것이다. 따라서 코시-슈바르츠 부등식에서 등호가 성립할 필요충분조건은 $u$가 $v$의 스칼라배이거나 $v$가 $u$의 스칼라배인 것이다. 이 표현은 $u$ 또는 $v$가 $0$인 경우도 포함하도록 선택되었다.

**6.16 예: 코시-슈바르츠 부등식**

(a) $x_1,\ldots,x_n,y_1,\ldots,y_n\in\mathbb{R}$이면

$$
(x_1y_1+\cdots+x_ny_n)^2
\le
(x_1^2+\cdots+x_n^2)(y_1^2+\cdots+y_n^2).
$$

이는 보통 유클리드 내적을 사용하여 벡터 $(x_1,\ldots,x_n),(y_1,\ldots,y_n)\in\mathbb{R}^n$에 코시-슈바르츠 부등식을 적용하면 따라온다.

(b) $f,g$가 $[-1,1]$ 위의 연속 실숫값 함수이면

$$
\left|\int_{-1}^{1}fg\right|^2
\le
\left(\int_{-1}^{1}f^2\right)\left(\int_{-1}^{1}g^2\right).
$$

이는 예 6.3(c)에 코시-슈바르츠 부등식을 적용하면 따라온다.

다음 결과는 삼각부등식이라고 불린다. 기하학적으로는 삼각형의 각 변의 길이가 다른 두 변의 길이의 합보다 작거나 같다는 뜻이다. 삼각부등식은 두 점 사이의 가장 짧은 꺾은선 경로가 하나의 선분임을 함의한다. 꺾은선 경로는 선분들로 이루어진 경로이다.

**6.17 삼각부등식**

$u,v\in V$라고 하자. 그러면

$$
\Vert u+v\Vert\le \Vert u\Vert+\Vert v\Vert.
$$

이 부등식에서 등호가 성립할 필요충분조건은 $u,v$ 중 하나가 다른 하나의 음이 아닌 실수배인 것이다.

증명. 우리는

$$
\begin{aligned}
\Vert u+v\Vert^2
&=\langle u+v,u+v\rangle \cr
&=\langle u,u\rangle+\langle v,v\rangle+\langle u,v\rangle+\langle v,u\rangle \cr
&=\langle u,u\rangle+\langle v,v\rangle+\langle u,v\rangle+\overline{\langle u,v\rangle} \cr
&=\Vert u\Vert^2+\Vert v\Vert^2+2\text{Re}\langle u,v\rangle \cr
&\le \Vert u\Vert^2+\Vert v\Vert^2+2|\langle u,v\rangle| \tag{6.18}\cr
&\le \Vert u\Vert^2+\Vert v\Vert^2+2\Vert u\Vert\thinspace\Vert v\Vert \tag{6.19}\cr
&=(\Vert u\Vert+\Vert v\Vert)^2.
\end{aligned}
$$

여기서 (6.19)는 코시-슈바르츠 부등식(6.14)에서 따라온다. 위 부등식 양변의 제곱근을 취하면 원하는 부등식을 얻는다.

위 증명은 삼각부등식에서 등호가 성립할 필요충분조건이 (6.18)과 (6.19)에서 모두 등호가 성립하는 것임을 보여 준다. 따라서 삼각부등식에서 등호가 성립할 필요충분조건은

**(6.20)**

$$
\langle u,v\rangle=\Vert u\Vert\thinspace\Vert v\Vert
$$

인 것이다. $u,v$ 중 하나가 다른 하나의 음이 아닌 실수배이면 (6.20)이 성립한다. 반대로 (6.20)이 성립한다고 하자. 그러면 코시-슈바르츠 부등식(6.14)에서 등호가 성립하기 위한 조건에 의해 $u,v$ 중 하나는 다른 하나의 스칼라배이다. 이 스칼라는 (6.20)에 의해 음이 아닌 실수여야 한다. 이로써 증명이 끝난다.

역삼각부등식은 연습문제 20번을 보라.

다음 결과는 평행사변형 등식이라고 불린다. 그 기하학적 의미는 모든 평행사변형에서 두 대각선 길이의 제곱의 합이 네 변 길이의 제곱의 합과 같다는 것이다. 여기서의 증명은 유클리드 기하의 보통 증명보다 더 직접적이다.

**6.21 평행사변형 등식**

$u,v\in V$라고 하자. 그러면

$$
\Vert u+v\Vert^2+\Vert u-v\Vert^2=2(\Vert u\Vert^2+\Vert v\Vert^2).
$$

증명. 우리는

$$
\begin{aligned}
\Vert u+v\Vert^2+\Vert u-v\Vert^2
&=\langle u+v,u+v\rangle+\langle u-v,u-v\rangle \cr
&=\Vert u\Vert^2+\Vert v\Vert^2+\langle u,v\rangle+\langle v,u\rangle \cr
&\quad+\Vert u\Vert^2+\Vert v\Vert^2-\langle u,v\rangle-\langle v,u\rangle \cr
&=2(\Vert u\Vert^2+\Vert v\Vert^2).
\end{aligned}
$$

원하는 결과가 성립한다.

### 연습문제 6A

1. 증명하거나 반례를 들어라. $v_1,\ldots,v_m\in V$이면

$$
\sum_{j=1}^m\sum_{k=1}^m\langle v_j,v_k\rangle\ge 0.
$$

2. $S\in\mathcal{L}(V)$라고 하자. 모든 $u,v\in V$에 대해

$$
\langle u,v\rangle_1=\langle Su,Sv\rangle
$$

로 $\langle\cdot,\cdot\rangle_1$을 정의한다. $\langle\cdot,\cdot\rangle_1$이 $V$ 위의 내적일 필요충분조건은 $S$가 단사인 것임을 보여라.

3. (a) $\mathbb{R}^2$의 원소들의 순서쌍 $((x_1,x_2),(y_1,y_2))$를 $|x_1y_1|+|x_2y_2|$로 보내는 함수가 $\mathbb{R}^2$ 위의 내적이 아님을 보여라.

   (b) $\mathbb{R}^3$의 원소들의 순서쌍 $((x_1,x_2,x_3),(y_1,y_2,y_3))$를 $x_1y_1+x_3y_3$로 보내는 함수가 $\mathbb{R}^3$ 위의 내적이 아님을 보여라.

4. $T\in\mathcal{L}(V)$가 모든 $v\in V$에 대해 $\Vert Tv\Vert\le \Vert v\Vert$를 만족한다고 하자. $T-\sqrt{2}I$가 단사임을 증명하라.

5. $V$가 실수 내적공간이라고 하자.

   (a) 모든 $u,v\in V$에 대해 $\langle u+v,u-v\rangle=\Vert u\Vert^2-\Vert v\Vert^2$임을 보여라.

   (b) $u,v\in V$가 같은 노름을 가지면 $u+v$가 $u-v$에 직교함을 보여라.

   (c) (b)를 사용하여 마름모의 대각선들이 서로 수직임을 보여라.

6. $u,v\in V$라고 하자. 다음을 증명하라.

$$
\langle u,v\rangle=0
\Longleftrightarrow
\Vert u\Vert\le \Vert u+av\Vert\quad(a\in\mathbb{F}).
$$

7. $u,v\in V$라고 하자. 모든 $a,b\in\mathbb{R}$에 대해 $\Vert au+bv\Vert=\Vert bu+av\Vert$일 필요충분조건은 $\Vert u\Vert=\Vert v\Vert$인 것임을 증명하라.

8. $a,b,c,x,y\in\mathbb{R}$이고

$$
a^2+b^2+c^2+x^2+y^2\le 1
$$

이라고 하자. $a+b+c+4x+9y\le 10$임을 증명하라.

9. $u,v\in V$이고 $\Vert u\Vert=\Vert v\Vert=1$, $\langle u,v\rangle=1$이라고 하자. $u=v$임을 증명하라.

10. $u,v\in V$이고 $\Vert u\Vert\le 1$, $\Vert v\Vert\le 1$이라고 하자. 다음을 증명하라.

$$
\sqrt{1-\Vert u\Vert^2}\sqrt{1-\Vert v\Vert^2}\le 1-|\langle u,v\rangle|.
$$

11. $u$는 $(1,3)$의 스칼라배이고, $v$는 $(1,3)$에 직교하며, $(1,2)=u+v$가 되도록 하는 벡터 $u,v\in\mathbb{R}^2$를 찾아라.

12. $a,b,c,d$가 양수라고 하자.

   (a) 다음을 증명하라.

$$
(a+b+c+d)\left(\frac1a+\frac1b+\frac1c+\frac1d\right)\ge 16.
$$

   (b) 어떤 양수 $a,b,c,d$에 대해 위 부등식에서 등호가 성립하는가?

13. 평균의 제곱은 제곱들의 평균보다 작거나 같음을 보여라. 더 정확히, $a_1,\ldots,a_n\in\mathbb{R}$이면 $a_1,\ldots,a_n$의 평균의 제곱은 $a_1^2,\ldots,a_n^2$의 평균보다 작거나 같음을 보여라.

14. $v\in V$이고 $v\ne 0$이라고 하자. $v/\Vert v\Vert$가 $V$의 단위구 위에서 $v$에 가장 가까운 유일한 원소임을 증명하라. 더 정확히, $u\in V$이고 $\Vert u\Vert=1$이면

$$
\left\Vert v-\frac{v}{\Vert v\Vert}\right\Vert\le \Vert v-u\Vert
$$

이고, 등호는 $u=v/\Vert v\Vert$일 때만 성립함을 증명하라.

15. $u,v$가 $\mathbb{R}^2$의 영이 아닌 벡터라고 하자. 다음을 증명하라.

$$
\langle u,v\rangle=\Vert u\Vert\thinspace\Vert v\Vert\cos\theta,
$$

여기서 $\theta$는 $u$와 $v$를 원점을 시작점으로 하는 화살표로 생각할 때 두 벡터 사이의 각도이다.

   힌트: $u,v,u-v$가 이루는 삼각형에 코사인 법칙을 사용하라.

16. $\mathbb{R}^2$ 또는 $\mathbb{R}^3$에 있는 두 벡터를 원점을 시작점으로 하는 화살표로 생각하면, 두 벡터 사이의 각도는 기하학적으로 정의할 수 있다. 그러나 $n>3$일 때 $\mathbb{R}^n$에서는 기하가 그렇게 분명하지 않다. 따라서 두 영이 아닌 벡터 $x,y\in\mathbb{R}^n$ 사이의 각도를

$$
\arccos\frac{\langle x,y\rangle}{\Vert x\Vert\thinspace\Vert y\Vert}
$$

로 정의한다. 이 정의의 동기는 연습문제 15번에서 온다. 이 정의가 의미 있음을 보이려면 왜 코시-슈바르츠 부등식이 필요한지 설명하라.

17. 모든 실수 $a_1,\ldots,a_n$과 $b_1,\ldots,b_n$에 대해

$$
\left(\sum_{k=1}^n a_kb_k\right)^2
\le
\left(\sum_{k=1}^n ka_k^2\right)
\left(\sum_{k=1}^n \frac{b_k^2}{k}\right)
$$

임을 증명하라.

18. (a) $f:[1,\infty)\to[0,\infty)$가 연속이라고 하자. 다음을 보여라.

$$
\left(\int_1^\infty f\right)^2
\le
\int_1^\infty x^2(f(x))^2\thinspace dx.
$$

   (b) 어떤 연속함수 $f:[1,\infty)\to[0,\infty)$에 대해 (a)의 부등식에서 양변이 모두 유한하면서 등호가 성립하는가?

19. $v_1,\ldots,v_n$이 $V$의 기저이고 $T\in\mathcal{L}(V)$라고 하자. $\lambda$가 $T$의 고윳값이면

$$
|\lambda|^2
\le
\sum_{j=1}^n\sum_{k=1}^n|\mathcal{M}(T)_{j,k}|^2
$$

임을 증명하라. 여기서 $\mathcal{M}(T)_{j,k}$는 기저 $v_1,\ldots,v_n$에 대한 $T$의 행렬에서 $j$행 $k$열의 성분이다.

20. $u,v\in V$이면

$$
\bigl|\Vert u\Vert-\Vert v\Vert\bigr|\le \Vert u-v\Vert
$$

임을 증명하라.

   위 부등식은 역삼각부등식이라고 불린다. $V=\mathbb{C}$인 경우의 역삼각부등식은 4장의 연습문제 2번을 보라.

21. $u,v\in V$가

$$
\Vert u\Vert=3,\quad \Vert u+v\Vert=4,\quad \Vert u-v\Vert=6
$$

을 만족한다고 하자. $\Vert v\Vert$는 어떤 수인가?

22. $u,v\in V$이면

$$
\Vert u+v\Vert\thinspace\Vert u-v\Vert\le \Vert u\Vert^2+\Vert v\Vert^2
$$

임을 보여라.

23. $v_1,\ldots,v_m\in V$가 각 $k=1,\ldots,m$에 대해 $\Vert v_k\Vert\le 1$을 만족한다고 하자. 다음을 만족하는 $a_1,\ldots,a_m\in\lbrace1,-1\rbrace$가 존재함을 보여라.

$$
\Vert a_1v_1+\cdots+a_mv_m\Vert\le \sqrt{m}.
$$

24. 증명하거나 반례를 들어라. $\Vert\cdot\Vert$가 $\mathbb{R}^2$ 위의 어떤 내적에 대응하는 노름이면, 어떤 $(x,y)\in\mathbb{R}^2$가 존재하여

$$
\Vert(x,y)\Vert\ne \max\lbrace|x|,|y|\rbrace
$$

이다.

25. $p>0$이라고 하자. 모든 $(x,y)\in\mathbb{R}^2$에 대해

$$
\Vert(x,y)\Vert=(|x|^p+|y|^p)^{1/p}
$$

로 주어지는 대응 노름을 가지는 $\mathbb{R}^2$ 위의 내적이 존재할 필요충분조건은 $p=2$인 것임을 증명하라.

26. $V$가 실수 내적공간이라고 하자. 모든 $u,v\in V$에 대해

$$
\langle u,v\rangle=\frac{\Vert u+v\Vert^2-\Vert u-v\Vert^2}{4}
$$

임을 증명하라.

27. $V$가 복소 내적공간이라고 하자. 모든 $u,v\in V$에 대해

$$
\langle u,v\rangle
=\frac{\Vert u+v\Vert^2-\Vert u-v\Vert^2+\Vert u+iv\Vert^2 i-\Vert u-iv\Vert^2 i}{4}
$$

임을 증명하라.

28. 벡터공간 $U$ 위의 노름은 다음 성질을 만족하는 함수 $\Vert\cdot\Vert:U\to[0,\infty)$이다. $\Vert u\Vert=0$일 필요충분조건은 $u=0$이고, 모든 $\alpha\in\mathbb{F}$와 모든 $u\in U$에 대해 $\Vert\alpha u\Vert=|\alpha|\Vert u\Vert$이며, 모든 $u,v\in U$에 대해 $\Vert u+v\Vert\le \Vert u\Vert+\Vert v\Vert$이다. 평행사변형 등식을 만족하는 노름은 내적에서 나온다는 것을 증명하라. 다시 말해, $\Vert\cdot\Vert$가 평행사변형 등식을 만족하는 $U$ 위의 노름이면, 모든 $u\in U$에 대해 $\Vert u\Vert=\langle u,u\rangle^{1/2}$가 되도록 하는 $U$ 위의 내적 $\langle\cdot,\cdot\rangle$이 존재함을 보여라.

29. $V_1,\ldots,V_m$이 내적공간이라고 하자. 다음 식이 $V_1\times\cdots\times V_m$ 위의 내적을 정의함을 보여라.

$$
\langle (u_1,\ldots,u_m),(v_1,\ldots,v_m)\rangle
=\langle u_1,v_1\rangle+\cdots+\langle u_m,v_m\rangle.
$$

   위 식의 오른쪽에서 각 $k=1,\ldots,m$에 대해 $\langle u_k,v_k\rangle$는 $V_k$ 위의 내적을 뜻한다. 같은 표기를 사용하고 있지만, $V_1,\ldots,V_m$ 각각은 서로 다른 내적을 가질 수 있다.

30. $V$가 실수 내적공간이라고 하자. $u,v,w,x\in V$에 대해

$$
\langle u+iv,w+ix\rangle_{\mathbb{C}}
=\langle u,w\rangle+\langle v,x\rangle+(\langle v,w\rangle-\langle u,x\rangle)i
$$

로 정의한다.

   (a) $\langle\cdot,\cdot\rangle_{\mathbb{C}}$가 $V_{\mathbb{C}}$를 복소 내적공간으로 만든다는 것을 보여라.

   (b) $u,v\in V$이면

$$
\langle u,v\rangle_{\mathbb{C}}=\langle u,v\rangle
\quad\text{그리고}\quad
\Vert u+iv\Vert_{\mathbb{C}}^2=\Vert u\Vert^2+\Vert v\Vert^2
$$

   임을 보여라.

   복소화 $V_{\mathbb{C}}$의 정의는 1B절의 연습문제 8번을 보라.

31. $u,v,w\in V$라고 하자. 다음을 증명하라.

$$
\left\Vert w-\frac12(u+v)\right\Vert^2
=\frac{\Vert w-u\Vert^2+\Vert w-v\Vert^2}{2}-\frac{\Vert u-v\Vert^2}{4}.
$$

32. $E$가 $V$의 부분집합이고, $u,v\in E$이면 $\frac12(u+v)\in E$라는 성질을 가진다고 하자. $w\in V$라고 하자. $E$ 안에서 $w$에 가장 가까운 점은 많아야 하나뿐임을 보여라. 다시 말해, 모든 $x\in E$에 대해

$$
\Vert w-u\Vert\le \Vert w-x\Vert
$$

를 만족하는 $u\in E$는 많아야 하나뿐임을 보여라.

33. $f,g$가 $\mathbb{R}$에서 $\mathbb{R}^n$으로 가는 미분가능 함수라고 하자.

   (a) 다음을 보여라.

$$
\langle f(t),g(t)\rangle'
=\langle f'(t),g(t)\rangle+\langle f(t),g'(t)\rangle.
$$

   (b) $c$가 양수이고 모든 $t\in\mathbb{R}$에 대해 $\Vert f(t)\Vert=c$라고 하자. 모든 $t\in\mathbb{R}$에 대해 $\langle f'(t),f(t)\rangle=0$임을 보여라.

   (c) (b)의 결과를 원점을 중심으로 하는 $\mathbb{R}^n$의 구 위에 놓인 곡선의 접벡터라는 관점에서 기하학적으로 해석하라.

   함수 $f:\mathbb{R}\to\mathbb{R}^n$가 미분가능하다는 것은, 각 $t\in\mathbb{R}$에 대해 $f(t)=(f_1(t),\ldots,f_n(t))$가 되도록 하는 미분가능 함수 $f_1,\ldots,f_n:\mathbb{R}\to\mathbb{R}$가 존재한다는 뜻이다. 더 나아가 각 $t\in\mathbb{R}$에 대해 도함수 $f'(t)\in\mathbb{R}^n$는

$$
f'(t)=(f_1'(t),\ldots,f_n'(t))
$$

로 정의된다.

34. 내적을 사용하여 아폴로니오스 항등식을 증명하라. 한 삼각형의 변의 길이가 $a,b,c$이고, 길이 $c$인 변의 중점에서 맞은편 꼭짓점까지의 선분 길이를 $d$라고 하자. 그러면

$$
a^2+b^2=\frac12c^2+2d^2.
$$

35. 양의 정수 $n$을 고정하자. $\mathbb{R}^n$ 위의 두 번 미분가능한 실숫값 함수 $p$의 라플라시안 $\Delta p$는 $\mathbb{R}^n$ 위의 다음 함수이다.

$$
\Delta p=\frac{\partial^2p}{\partial x_1^2}+\cdots+\frac{\partial^2p}{\partial x_n^2}.
$$

함수 $p$는 $\Delta p=0$이면 조화함수라고 불린다.

$\mathbb{R}^n$ 위의 다항식은 $m_1,\ldots,m_n$이 음이 아닌 정수일 때 $x_1^{m_1}\cdots x_n^{m_n}$ 꼴의 함수들의 실수 계수 선형결합이다. $q$가 $\mathbb{R}^n$ 위의 다항식이라고 하자. $\Vert x\Vert=1$인 모든 $x\in\mathbb{R}^n$에 대해 $p(x)=q(x)$가 되도록 하는 $\mathbb{R}^n$ 위의 조화다항식 $p$가 존재함을 증명하라.

   이 연습문제에 필요한 조화함수에 관한 유일한 사실은 다음이다. $p$가 $\mathbb{R}^n$ 위의 조화함수이고 $\Vert x\Vert=1$인 모든 $x\in\mathbb{R}^n$에 대해 $p(x)=0$이면, $p=0$이다.

   힌트: 원하는 조화다항식 $p$는 어떤 다항식 $r$에 대해 $q+(1-\Vert x\Vert^2)r$ 꼴일 것이라고 추측하는 것이 자연스럽다. 적당한 벡터공간 위의 연산자 $T$를

$$
Tr=\Delta((1-\Vert x\Vert^2)r)
$$

   로 정의하고, $T$가 단사이고 따라서 전사임을 보임으로써 $q+(1-\Vert x\Vert^2)r$이 조화함수가 되도록 하는 $\mathbb{R}^n$ 위의 다항식 $r$이 존재함을 증명하라.

코시와 슈바르츠의 부등식에 대한 셰익스피어풍 소네트를 입력으로 받아 ChatGPT가 쓴 시:

> 수들이 사는 영역, 비밀이 놓인 곳에서  
> 고귀한 진리가 깊은 곳에서 떠오른다.  
> 코시와 슈바르츠는 그 지혜를 펼쳐  
> 모두가 간직할 부등식을 남긴다.  
> 두 벡터는 이 결속으로 서로 얽히고,  
> 내적은 금빛 실처럼 그들을 엮는다.  
> 그 크기는 섭리에 의해 제한되어,  
> 운명이 정한 경계 안에 머문다.  
> 그림자가 내리고 황혼이 날을 흐려도,  
> 이 부등식은 시험을 견딜 것이다.  
> 우리 탐구를 이끌고 길을 비추며,  
> 그 진리 안에서 이해가 쉬게 하리라.  
> 그러니 뮤즈들이여, 이 고귀한 업적을 노래하라.  
> 코시-슈바르츠, 누구도 넘을 수 없는 경계를.

## 6B 정규직교기저

### 정규직교 리스트와 그램-슈미트 절차

**6.22 정의: 정규직교**

내적공간에서 벡터들의 리스트는 그 리스트의 각 벡터의 노름이 $1$이고, 리스트의 서로 다른 두 벡터가 서로 직교하면 **정규직교**라고 한다.

즉 $e_1,\ldots,e_m$이 정규직교라는 것은

$$
\langle e_j,e_k\rangle=
\begin{cases}
1, & j=k,\cr
0, & j\ne k
\end{cases}
$$

라는 뜻이다.

**6.23 예: 정규직교 리스트**

- $\mathbb{F}^n$의 표준기저는 정규직교 리스트이다.
- $\mathbb{F}^3$에서

  $$
  \left(\frac{1}{\sqrt 3},\frac{1}{\sqrt 3},\frac{1}{\sqrt 3}\right),
  \left(-\frac{1}{\sqrt 2},\frac{1}{\sqrt 2},0\right)
  $$

  는 정규직교 리스트이다.
- 앞의 리스트에

  $$
  \left(\frac{1}{\sqrt 6},\frac{1}{\sqrt 6},-\frac{2}{\sqrt 6}\right)
  $$

  를 덧붙이면 $\mathbb{F}^3$의 정규직교 리스트가 된다.
- 양의 정수 $n$에 대해

  $$
  \frac{1}{\sqrt{2\pi}},
  \frac{\cos x}{\sqrt\pi},\ldots,\frac{\cos nx}{\sqrt\pi},
  \frac{\sin x}{\sqrt\pi},\ldots,\frac{\sin nx}{\sqrt\pi}
  $$

  는 내적

  $$
  \langle f,g\rangle=\int_{-\pi}^{\pi} f(x)g(x)\thinspace dx
  $$

  이 주어진 $C[-\pi,\pi]$의 정규직교 리스트이다. 삼각함수로 이루어진 이런 리스트는 조수나 진동처럼 주기적인 현상을 분석하는 데 핵심적인 역할을 한다.
- $\mathcal{P}_2(\mathbb{R})$에 내적

  $$
  \langle p,q\rangle=\int_{-1}^{1}p(x)q(x)\thinspace dx
  $$

  가 주어져 있다고 하자. 표준기저 $1,x,x^2$은 정규직교 리스트가 아니다. 각 벡터를 그 노름으로 나누면

  $$
  \frac{1}{\sqrt 2},\sqrt{\frac32}x,\sqrt{\frac52}x^2
  $$

  를 얻는다. 이 리스트의 각 벡터는 노름 $1$이고, 두 번째 벡터는 첫 번째와 세 번째 벡터에 직교한다. 그러나 첫 번째 벡터와 세 번째 벡터는 직교하지 않으므로 이 리스트는 정규직교 리스트가 아니다.

**6.24 정규직교 리스트의 선형결합의 노름**

$e_1,\ldots,e_m$이 정규직교 리스트이고 $a_1,\ldots,a_m\in\mathbb{F}$이면

$$
\Vert a_1e_1+\cdots+a_me_m\Vert^2
=|a_1|^2+\cdots+|a_m|^2.
$$

**증명**

정규직교 조건에서 서로 다른 항들이 모두 직교하므로, 피타고라스 정리를 반복해서 적용하면 원하는 등식이 바로 나온다.

**6.25 정규직교 리스트는 일차독립이다**

모든 정규직교 리스트는 일차독립이다.

**증명**

$e_1,\ldots,e_m$이 정규직교 리스트이고

$$
a_1e_1+\cdots+a_me_m=0
$$

이라고 하자. 6.24에 의해

$$
|a_1|^2+\cdots+|a_m|^2=0
$$

이므로 $a_1=\cdots=a_m=0$이다. 따라서 $e_1,\ldots,e_m$은 일차독립이다.

**6.26 베셀 부등식**

$e_1,\ldots,e_m$이 $V$의 정규직교 리스트이고 $v\in V$이면

$$
|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_m\rangle|^2\le \Vert v\Vert^2.
$$

**증명**

다음과 같이 두 벡터를 정의하자.

$$
u=\langle v,e_1\rangle e_1+\cdots+\langle v,e_m\rangle e_m,
\qquad
w=v-u.
$$

각 $k=1,\ldots,m$에 대해 $\langle w,e_k\rangle=0$이므로 $w$는 $u$에 직교한다. 따라서 피타고라스 정리와 6.24에 의해

$$
\Vert v\Vert^2=\Vert u+w\Vert^2=\Vert u\Vert^2+\Vert w\Vert^2
\ge \Vert u\Vert^2
=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_m\rangle|^2.
$$

**6.27 정의: 정규직교기저**

내적공간의 정규직교 리스트가 그 공간의 기저이면, 그 리스트를 **정규직교기저**라고 한다.

**6.28 차원과 같은 길이의 정규직교 리스트**

$V$가 유한차원이고 $e_1,\ldots,e_{\dim V}$가 $V$의 정규직교 리스트이면 $e_1,\ldots,e_{\dim V}$는 $V$의 정규직교기저이다.

**증명**

6.25에 의해 이 리스트는 일차독립이다. 길이가 $\dim V$인 일차독립 리스트는 $V$의 기저이므로 결론이 따른다.

**6.29 예: $\mathbb{F}^4$의 정규직교기저**

$\mathbb{F}^4$의 다음 리스트는 정규직교기저이다.

$$
\left(\frac12,\frac12,\frac12,\frac12\right),
\left(\frac12,\frac12,-\frac12,-\frac12\right),
\left(\frac12,-\frac12,-\frac12,\frac12\right),
\left(-\frac12,\frac12,-\frac12,\frac12\right).
$$

각 벡터의 노름은 $1$이고, 예를 들어 첫 번째 벡터와 세 번째 벡터의 내적은

$$
\frac14-\frac14-\frac14+\frac14=0
$$

이다. 다른 서로 다른 두 벡터에 대해서도 같은 방식으로 내적이 $0$임을 확인할 수 있다. 따라서 이 리스트는 정규직교 리스트이고, 길이가 $\dim\mathbb{F}^4=4$이므로 정규직교기저이다.

**6.30 정규직교기저를 이용한 벡터의 전개**

$e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $u,v\in V$라고 하자. 그러면 다음이 성립한다.

(a)

$$
v=\langle v,e_1\rangle e_1+\cdots+\langle v,e_n\rangle e_n.
$$

(b)

$$
\Vert v\Vert^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2.
$$

(c)

$$
\langle u,v\rangle
=\langle u,e_1\rangle\overline{\langle v,e_1\rangle}
+\cdots+
\langle u,e_n\rangle\overline{\langle v,e_n\rangle}.
$$

**증명**

(a)를 보이기 위해 $v=a_1e_1+\cdots+a_ne_n$이라고 쓰자. 각 $k$에 대해 양변에 $e_k$와의 내적을 취하면 $a_k=\langle v,e_k\rangle$이다.

(b)는 (a)와 6.24를 적용하면 된다.

(c)는 (a)를 $u$와 $v$에 각각 적용한 뒤 내적의 선형성과 켤레선형성을 사용하면 얻어진다.

**6.31 예: 정규직교기저에 대한 전개**

6.29의 정규직교기저에 대해 $(1,2,4,7)\in\mathbb{F}^4$는 다음과 같이 전개된다.

$$
\begin{aligned}
(1,2,4,7)
&=7\left(\frac12,\frac12,\frac12,\frac12\right)
-4\left(\frac12,\frac12,-\frac12,-\frac12\right)\cr
&\quad+\left(\frac12,-\frac12,-\frac12,\frac12\right)
+2\left(-\frac12,\frac12,-\frac12,\frac12\right).
\end{aligned}
$$

**6.32 그램-슈미트 절차**

$v_1,\ldots,v_m$이 $V$의 일차독립 리스트라고 하자. $f_1=v_1$로 두고, $k=2,\ldots,m$에 대해

$$
f_k
=v_k-\frac{\langle v_k,f_1\rangle}{\Vert f_1\Vert^2}f_1
-\cdots-
\frac{\langle v_k,f_{k-1}\rangle}{\Vert f_{k-1}\Vert^2}f_{k-1}
$$

로 정의하자. 그리고 각 $k=1,\ldots,m$에 대해

$$
e_k=\frac{f_k}{\Vert f_k\Vert}
$$

라고 하자. 그러면 $e_1,\ldots,e_m$은 $V$의 정규직교 리스트이고, 각 $k=1,\ldots,m$에 대해

$$
\text{span}(v_1,\ldots,v_k)=\text{span}(e_1,\ldots,e_k)
$$

가 성립한다.

**증명**

$f_k$의 정의에서 $f_k\in\text{span}(v_1,\ldots,v_k)$이고, $f_k$는 $f_1,\ldots,f_{k-1}$ 각각에 직교한다. 귀납적으로

$$
\text{span}(v_1,\ldots,v_{k-1})
=\text{span}(e_1,\ldots,e_{k-1})
\tag{6.33}
$$

라고 가정하면 $f_k\ne 0$이다. 실제로 $f_k=0$이면 $v_k\in\text{span}(v_1,\ldots,v_{k-1})$가 되어 $v_1,\ldots,v_m$의 일차독립성에 모순이다. 따라서 $e_k=f_k/\Vert f_k\Vert$가 잘 정의되고 노름은 $1$이다.

또한 $f_k$가 앞의 $f_j$들에 직교하므로 $e_k$도 앞의 $e_j$들에 직교한다. 마지막으로 $e_k$는 $f_k$의 스칼라배이고, $f_k$의 정의를 정리하면 $v_k$가 $\text{span}(f_1,\ldots,f_k)$에 속하므로

$$
\text{span}(v_1,\ldots,v_k)=\text{span}(f_1,\ldots,f_k)
=\text{span}(e_1,\ldots,e_k)
$$

이다.

**6.34 예: $\mathcal{P}_2(\mathbb{R})$에서 그램-슈미트 절차**

$\mathcal{P}_2(\mathbb{R})$에 내적

$$
\langle p,q\rangle=\int_{-1}^{1}p(x)q(x)\thinspace dx
$$

가 주어져 있다고 하자. 표준기저 $v_1=1$, $v_2=x$, $v_3=x^2$에 그램-슈미트 절차를 적용하면

$$
f_1=1,\qquad \Vert f_1\Vert^2=2,
$$

$$
f_2=x,\qquad \Vert f_2\Vert^2=\frac23,
$$

$$
f_3=x^2-\frac13,\qquad \Vert f_3\Vert^2=\frac{8}{45}
$$

을 얻는다. 따라서

$$
\sqrt{\frac12},\quad
\sqrt{\frac32}x,\quad
\sqrt{\frac{45}{8}}\left(x^2-\frac13\right)
$$

는 $\mathcal{P}_2(\mathbb{R})$의 정규직교기저이다.

**6.35 정규직교기저의 존재**

모든 유한차원 내적공간은 정규직교기저를 가진다.

**증명**

$V$의 임의의 기저에 그램-슈미트 절차를 적용하면 정규직교기저를 얻는다.

**6.36 정규직교 리스트의 확장**

유한차원 내적공간의 모든 정규직교 리스트는 그 공간의 정규직교기저로 확장될 수 있다.

**증명**

정규직교 리스트는 6.25에 의해 일차독립이다. 이를 $V$의 기저로 확장한 뒤, 그 기저에 그램-슈미트 절차를 적용한다. 처음에 주어진 정규직교 리스트는 이미 정규직교이므로 그램-슈미트 절차에서 변하지 않는다.

**6.37 정규직교기저에 대한 상삼각 행렬**

$V$가 유한차원 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$가 어떤 정규직교기저에 대해 상삼각 행렬을 가지는 것과, $T$의 최소다항식이 $\mathbb{F}$에서 일차식들의 곱으로 분해되는 것은 동치이다.

**증명**

$T$가 어떤 기저 $v_1,\ldots,v_n$에 대해 상삼각 행렬을 가진다고 하자. 그램-슈미트 절차로부터 얻은 정규직교기저 $e_1,\ldots,e_n$은 각 $k$에 대해

$$
\text{span}(v_1,\ldots,v_k)=\text{span}(e_1,\ldots,e_k)
$$

를 만족한다. 상삼각 행렬 조건은 바로 이 부분공간들이 모두 $T$에 대해 불변이라는 뜻이므로, $T$는 $e_1,\ldots,e_n$에 대해서도 상삼각 행렬을 가진다. 이제 5.44를 적용하면 원하는 동치가 따른다.

**6.38 슈어 정리**

$V$가 유한차원 복소 내적공간이고 $T\in\mathcal{L}(V)$이면, $T$는 $V$의 어떤 정규직교기저에 대해 상삼각 행렬을 가진다.

**증명**

복소수체 위에서는 모든 다항식이 일차식들의 곱으로 분해된다. 따라서 6.37을 적용하면 된다.

### 내적공간 위의 선형함수

**6.39 정의: 선형함수와 쌍대공간**

$V$ 위의 **선형함수**는 $V$에서 $\mathbb{F}$로 가는 선형사상이다.

$V$에서 $\mathbb{F}$로 가는 모든 선형함수들의 벡터공간을 $V$의 **쌍대공간**이라 하고 $V'$로 나타낸다. 즉

$$
V'=\mathcal{L}(V,\mathbb{F}).
$$

**6.40 예: $\mathbb{F}^3$ 위의 선형함수**

$\varphi:\mathbb{F}^3\to\mathbb{F}$를

$$
\varphi(z_1,z_2,z_3)=2z_1-5z_2+z_3
$$

로 정의하면 $\varphi$는 $\mathbb{F}^3$ 위의 선형함수이다. 표준 내적을 사용하면

$$
\varphi(z_1,z_2,z_3)
=\langle (z_1,z_2,z_3),(2,-5,1)\rangle
$$

이다.

**6.41 예: 다항식공간 위의 선형함수**

$\varphi:\mathcal{P}_5(\mathbb{R})\to\mathbb{R}$를

$$
\varphi(p)=\int_{-1}^{1}p(t)\cos(\pi t)\thinspace dt
$$

로 정의하면 $\varphi$는 $\mathcal{P}_5(\mathbb{R})$ 위의 선형함수이다.

6.41의 예에서 $\mathcal{P}_5(\mathbb{R})$에 내적

$$
\langle p,q\rangle=\int_{-1}^{1}p(t)q(t)\thinspace dt
$$

를 주면, 어떤 다항식 $q\in\mathcal{P}_5(\mathbb{R})$가 존재하여 모든 $p\in\mathcal{P}_5(\mathbb{R})$에 대해

$$
\varphi(p)=\langle p,q\rangle
$$

가 성립한다. 다음 정리는 유한차원 내적공간에서 모든 선형함수가 이런 방식으로 표현된다는 것을 말한다.

**6.42 리스 표현정리**

$V$가 유한차원 내적공간이고 $\varphi$가 $V$ 위의 선형함수라고 하자. 그러면 모든 $u\in V$에 대해

$$
\varphi(u)=\langle u,v\rangle
$$

가 되게 하는 유일한 $v\in V$가 존재한다.

**증명**

$e_1,\ldots,e_n$을 $V$의 정규직교기저라고 하자. $u\in V$이면 6.30에 의해

$$
u=\langle u,e_1\rangle e_1+\cdots+\langle u,e_n\rangle e_n.
$$

따라서

$$
\varphi(u)=\langle u,e_1\rangle\varphi(e_1)+\cdots+
\langle u,e_n\rangle\varphi(e_n).
$$

이제

$$
v=\overline{\varphi(e_1)}e_1+\cdots+\overline{\varphi(e_n)}e_n
\tag{6.43}
$$

로 두면 모든 $u\in V$에 대해 $\varphi(u)=\langle u,v\rangle$이다.

유일성을 보이자. 모든 $u\in V$에 대해 $\langle u,v\rangle=\langle u,w\rangle$라고 하면, 특히 $u=v-w$를 대입하여

$$
\Vert v-w\Vert^2=0
$$

을 얻는다. 따라서 $v=w$이다.

**6.44 예: 리스 표현정리로 다항식 찾기**

$\mathcal{P}_2(\mathbb{R})$에 내적

$$
\langle p,q\rangle=\int_{-1}^{1}p(t)q(t)\thinspace dt
$$

가 주어져 있다고 하자. 모든 $p\in\mathcal{P}_2(\mathbb{R})$에 대해

$$
\int_{-1}^{1}p(t)\cos(\pi t)\thinspace dt
=\int_{-1}^{1}p(t)q(t)\thinspace dt
\tag{6.45}
$$

가 성립하게 하는 $q\in\mathcal{P}_2(\mathbb{R})$를 구하자.

$\varphi(p)=\int_{-1}^{1}p(t)\cos(\pi t)\thinspace dt$라고 두면 $\varphi$는 $\mathcal{P}_2(\mathbb{R})$ 위의 선형함수이다. 6.34의 정규직교기저를 6.43에 대입하면

$$
\begin{aligned}
q(x)
&=\left(\int_{-1}^{1}\sqrt{\frac12}\cos(\pi t)\thinspace dt\right)\sqrt{\frac12}\cr
&\quad+
\left(\int_{-1}^{1}\sqrt{\frac32}t\cos(\pi t)\thinspace dt\right)\sqrt{\frac32}x\cr
&\quad+
\left(\int_{-1}^{1}\sqrt{\frac{45}{8}}\left(t^2-\frac13\right)\cos(\pi t)\thinspace dt\right)
\sqrt{\frac{45}{8}}\left(x^2-\frac13\right).
\end{aligned}
$$

계산하면

$$
q(x)=\frac{15}{2\pi^2}(1-3x^2)
$$

이다. 이것이 6.45를 만족하는 유일한 다항식이다.

같은 방식으로 $\mathcal{P}_5(\mathbb{R})$에서는 다음 다항식이 모든 $p\in\mathcal{P}_5(\mathbb{R})$에 대해 대응되는 표현을 준다.

$$
q(x)=\frac{105}{8\pi^4}
\left((27-2\pi^2)+(24\pi^2-270)x^2+(315-30\pi^2)x^4\right).
$$

이 계산에서 선택한 정규직교기저는 답을 찾는 도구일 뿐이다. 리스 표현정리의 유일성 때문에 얻어진 벡터 $q$는 어떤 정규직교기저를 쓰더라도 같다. 6.58과 6C의 연습문제 13번에서는 리스 표현정리의 다른 증명을 보게 된다.

### 연습문제 6B

1. $e_1,\ldots,e_m$이 $V$의 리스트이고 모든 $a_1,\ldots,a_m\in\mathbb{F}$에 대해

$$
\Vert a_1e_1+\cdots+a_me_m\Vert^2=|a_1|^2+\cdots+|a_m|^2
$$

   라고 하자. $e_1,\ldots,e_m$이 정규직교 리스트임을 증명하여라.

2. $\mathbb{R}^2$의 모든 정규직교기저를 구하여라.

3. $e_1,\ldots,e_m$이 $V$의 정규직교 리스트이고 $v\in V$라고 하자. 6.26의 베셀 부등식에서 등호가 성립하는 것은 $v\in\text{span}(e_1,\ldots,e_m)$인 것과 동치임을 증명하여라.

4. 양의 정수 $n$에 대해

   $$
   \frac{1}{\sqrt{2\pi}},
   \frac{\cos x}{\sqrt\pi},\ldots,\frac{\cos nx}{\sqrt\pi},
   \frac{\sin x}{\sqrt\pi},\ldots,\frac{\sin nx}{\sqrt\pi}
   $$

   가 내적 $\langle f,g\rangle=\int_{-\pi}^{\pi}f(x)g(x)\thinspace dx$가 주어진 $C[-\pi,\pi]$의 정규직교 리스트임을 증명하여라.

   힌트: 다음 항등식을 사용하여라.

   $$
   \sin x\cos y=\frac{\sin(x-y)+\sin(x+y)}{2},
   $$

   $$
   \cos x\cos y=\frac{\cos(x-y)+\cos(x+y)}{2},
   $$

   $$
   \sin x\sin y=\frac{\cos(x-y)-\cos(x+y)}{2}.
   $$

5. $f\in C[-\pi,\pi]$라고 하자. 음이 아닌 정수 $k$에 대해

   $$
   a_k=\frac{1}{\sqrt\pi}\int_{-\pi}^{\pi}f(x)\cos(kx)\thinspace dx
   $$

   라고 하고, 양의 정수 $k$에 대해

   $$
   b_k=\frac{1}{\sqrt\pi}\int_{-\pi}^{\pi}f(x)\sin(kx)\thinspace dx
   $$

   라고 하자. 다음 부등식을 증명하여라.

   $$
   \frac{a_0^2}{2}+\sum_{k=1}^{\infty}(a_k^2+b_k^2)
   \le
   \int_{-\pi}^{\pi}f(x)^2\thinspace dx.
   $$

6. $e_1,\ldots,e_n$이 $V$의 정규직교기저이고 $v_1,\ldots,v_n\in V$가 각 $k$에 대해

   $$
   \Vert e_k-v_k\Vert<\frac{1}{\sqrt n}
   $$

   를 만족한다고 하자. $v_1,\ldots,v_n$이 $V$의 기저임을 증명하여라. 부등식의 $<$를 $\le$로 바꾸면 결론이 거짓이 될 수 있음을 보이는 예도 제시하여라.

7. $T\in\mathcal{L}(\mathbb{R}^3)$가 기저

   $$
   (1,0,0),\quad (1,1,1),\quad (1,1,2)
   $$

   에 대해 상삼각 행렬을 가진다고 하자. $T$가 상삼각 행렬을 가지는 $\mathbb{R}^3$의 정규직교기저를 구하여라.

8. $\mathcal{P}_2(\mathbb{R})$에 내적

   $$
   \langle p,q\rangle=\int_{0}^{1}p(x)q(x)\thinspace dx
   $$

   가 주어져 있다고 하자. 기저 $1,x,x^2$에 그램-슈미트 절차를 적용하여 $\mathcal{P}_2(\mathbb{R})$의 정규직교기저를 구하여라. 또한 $Tp=p'$로 정의되는 미분 연산자 $T$의 이 정규직교기저에 대한 행렬을 구하여라.

9. $e_1,\ldots,e_m$이 $v_1,\ldots,v_m$에 그램-슈미트 절차를 적용하여 얻은 리스트라고 하자. 각 $k=1,\ldots,m$에 대해 $\langle v_k,e_k\rangle>0$임을 증명하여라.

10. $v_1,\ldots,v_m$이 $V$의 일차독립 리스트라고 하자. $e_1,\ldots,e_m$이 각 $k=1,\ldots,m$에 대해

    $$
    \text{span}(v_1,\ldots,v_k)=\text{span}(e_1,\ldots,e_k)
    $$

    를 만족하고 $\langle v_k,e_k\rangle>0$인 정규직교 리스트라면, $e_1,\ldots,e_m$은 $v_1,\ldots,v_m$에 그램-슈미트 절차를 적용하여 얻은 리스트임을 증명하여라.

11. 모든 $p\in\mathcal{P}_2(\mathbb{R})$에 대해

    $$
    p\left(\frac12\right)=\int_{0}^{1}p(x)q(x)\thinspace dx
    $$

    가 성립하게 하는 $q\in\mathcal{P}_2(\mathbb{R})$를 구하여라.

12. 모든 $p\in\mathcal{P}_2(\mathbb{R})$에 대해

    $$
    \int_{0}^{1}p(x)\cos(\pi x)\thinspace dx=\int_{0}^{1}p(x)q(x)\thinspace dx
    $$

    가 성립하게 하는 $q\in\mathcal{P}_2(\mathbb{R})$를 구하여라.

13. $v_1,\ldots,v_m$이 $V$의 리스트라고 하자. 그램-슈미트 절차를 형식적으로 적용할 때 어떤 $f_k$가 $0$이 되는 것은 $v_1,\ldots,v_m$이 일차종속인 것과 동치임을 증명하여라.

14. $V$가 실 내적공간이고 $v_1,\ldots,v_m$이 $V$의 일차독립 리스트라고 하자. 정확히 $2^m$개의 정규직교 리스트 $e_1,\ldots,e_m$이 존재하여 각 $k=1,\ldots,m$에 대해

    $$
    \text{span}(v_1,\ldots,v_k)=\text{span}(e_1,\ldots,e_k)
    $$

    가 성립함을 증명하여라.

15. $\langle\cdot,\cdot\rangle_1$과 $\langle\cdot,\cdot\rangle_2$가 $V$ 위의 두 내적이고, 모든 $u,v\in V$에 대해

    $$
    \langle u,v\rangle_1=0
    $$

    인 것과

    $$
    \langle u,v\rangle_2=0
    $$

    인 것이 동치라고 하자. 어떤 양의 수 $c$가 존재하여 모든 $u,v\in V$에 대해

    $$
    \langle u,v\rangle_1=c\langle u,v\rangle_2
    $$

    가 성립함을 증명하여라.

16. $V$가 유한차원이고 $\langle\cdot,\cdot\rangle_1$, $\langle\cdot,\cdot\rangle_2$가 $V$ 위의 두 내적이라고 하자. 이 두 내적에서 오는 노름을 각각 $\Vert\cdot\Vert_1$, $\Vert\cdot\Vert_2$라고 할 때, 어떤 양의 수 $c$가 존재하여 모든 $v\in V$에 대해

    $$
    \Vert v\Vert_1\le c\Vert v\Vert_2
    $$

    가 성립함을 증명하여라.

17. $\mathbb{F}=\mathbb{C}$이고 $V$가 유한차원이며 $T\in\mathcal{L}(V)$라고 하자. $T$의 유일한 고윳값이 $1$이고 모든 $v\in V$에 대해 $\Vert Tv\Vert\le\Vert v\Vert$이면 $T=I$임을 증명하여라.

18. $u_1,\ldots,u_m$이 $V$의 일차독립 리스트라고 하자. 각 $k=1,\ldots,m$에 대해 $\langle u_k,v\rangle=1$을 만족하는 $v\in V$가 존재함을 증명하여라.

19. $v_1,\ldots,v_n$이 $V$의 기저라고 하자. 다음을 만족하는 $V$의 기저 $u_1,\ldots,u_n$이 존재함을 증명하여라.

    $$
    \langle v_j,u_k\rangle=
    \begin{cases}
    0, & j\ne k,\cr
    1, & j=k.
    \end{cases}
    $$

20. $\mathbb{F}=\mathbb{C}$이고 $V$가 유한차원이라고 하자. $\mathcal{E}$가 $\mathcal{L}(V)$의 부분집합이고, $\mathcal{E}$의 임의의 두 연산자가 서로 교환한다고 하자. 그러면 $V$의 어떤 정규직교기저가 존재하여 $\mathcal{E}$의 모든 원소가 그 기저에 대해 상삼각 행렬을 가짐을 증명하여라.

21. $V$가 유한차원 복소 내적공간이고 $T\in\mathcal{L}(V)$의 모든 고윳값의 절댓값이 $1$보다 작다고 하자. 모든 $\varepsilon>0$에 대해 어떤 양의 정수 $m$이 존재하여 모든 $v\in V$에 대해

    $$
    \Vert T^m v\Vert\le\varepsilon\Vert v\Vert
    $$

    가 성립함을 증명하여라.

22. $V=C[-1,1]$에 내적

    $$
    \langle f,g\rangle=\int_{-1}^{1}f(x)g(x)\thinspace dx
    $$

    가 주어져 있다고 하자. $\varphi\in V'$를 $\varphi(f)=f(0)$으로 정의하자. 모든 $f\in V$에 대해

    $$
    \varphi(f)=\langle f,g\rangle
    $$

    가 성립하게 하는 $g\in V$가 존재하지 않음을 증명하여라. 이것은 유한차원이라는 가정 없이 리스 표현정리가 성립하지 않을 수 있음을 보여 준다.

23. $V$가 유한차원 내적공간이라고 하자. $d:V\times V\to[0,\infty)$를

    $$
    d(u,v)=\Vert u-v\Vert
    $$

    로 정의한다.

    (a) $d$가 $V$ 위의 거리임을 증명하여라.

    (b) 이 거리에서 $V$가 완비임을 증명하여라.

    (c) $V$의 모든 유한차원 부분공간이 닫힌집합임을 증명하여라.

## 6C 직교여공간과 최소화 문제

### 직교여공간

**6.46 정의: 직교여공간**

$U$가 $V$의 부분집합이면 $U$의 **직교여공간** $U^\perp$는 $U$의 모든 벡터에 직교하는 $V$의 모든 벡터들의 집합이다. 즉

$$
U^\perp=\lbrace v\in V:\text{ 모든 }u\in U\text{에 대해 }\langle u,v\rangle=0\rbrace.
$$

**6.47 예: 직교여공간**

- $V=\mathbb{R}^3$이고 $U=\lbrace(2,3,5)\rbrace$이면

  $$
  U^\perp=\lbrace(x,y,z)\in\mathbb{R}^3:2x+3y+5z=0\rbrace.
  $$

  따라서 $U^\perp$는 원점을 지나는 평면이다.
- $U=\lbrace(x,y,z)\in\mathbb{R}^3:2x+3y+5z=0\rbrace$이면

  $$
  U^\perp=\lbrace(2t,3t,5t):t\in\mathbb{R}\rbrace.
  $$

  따라서 원점을 지나는 평면의 직교여공간은 그 평면에 수직인 직선이다.
- 일반적으로 $\mathbb{R}^3$에서 원점을 지나는 평면의 직교여공간은 그 평면에 수직인 원점을 지나는 직선이고, 원점을 지나는 직선의 직교여공간은 그 직선에 수직인 원점을 지나는 평면이다.
- $V=\mathbb{F}^5$이고

  $$
  U=\lbrace(a,b,0,0,0):a,b\in\mathbb{F}\rbrace
  $$

  이면

  $$
  U^\perp=\lbrace(0,0,x,y,z):x,y,z\in\mathbb{F}\rbrace.
  $$

- $e_1,\ldots,e_m,f_1,\ldots,f_n$이 $V$의 정규직교기저이면

  $$
  \left(\text{span}(e_1,\ldots,e_m)\right)^\perp
  =\text{span}(f_1,\ldots,f_n).
  $$

**6.48 직교여공간의 기본 성질**

$U,G,H$가 $V$의 부분집합이라고 하자. 그러면 다음이 성립한다.

(a) $U^\perp$는 $V$의 부분공간이다.

(b) $\lbrace0\rbrace^\perp=V$.

(c) $V^\perp=\lbrace0\rbrace$.

(d) $U\cap U^\perp\subset \lbrace0\rbrace$.

(e) $G\subset H$이면 $H^\perp\subset G^\perp$.

**증명**

(a)는 내적의 선형성에서 바로 따른다. (b)는 모든 벡터가 $0$에 직교한다는 사실이고, (c)는 $v\in V^\perp$이면 특히 $\langle v,v\rangle=0$이므로 $v=0$이라는 사실이다. (d)는 $v\in U\cap U^\perp$이면 $v$가 자기 자신에 직교하므로 $v=0$임을 말한다. (e)는 $H$의 모든 벡터에 직교하는 벡터는 그 부분집합 $G$의 모든 벡터에도 직교하기 때문이다.

**6.49 유한차원 부분공간과 그 직교여공간의 직합**

$U$가 $V$의 유한차원 부분공간이면

$$
V=U\oplus U^\perp.
$$

**증명**

$e_1,\ldots,e_m$을 $U$의 정규직교기저라고 하자. 임의의 $v\in V$에 대해

$$
v=
\underbrace{\langle v,e_1\rangle e_1+\cdots+\langle v,e_m\rangle e_m}_{u}
+
\underbrace{\left(v-\langle v,e_1\rangle e_1-\cdots-\langle v,e_m\rangle e_m\right)}_{w}
\tag{6.50}
$$

라고 쓸 수 있다. 여기서 $u\in U$이고, 각 $k$에 대해 $\langle w,e_k\rangle=0$이므로 $w\in U^\perp$이다. 따라서 $V=U+U^\perp$이다. 또한 6.48(d)에 의해 $U\cap U^\perp=\lbrace0\rbrace$이므로 합은 직합이다.

**6.51 직교여공간의 차원**

$V$가 유한차원이고 $U$가 $V$의 부분공간이면

$$
\dim U^\perp=\dim V-\dim U.
$$

**증명**

6.49와 직합의 차원 공식에서 바로 따른다.

**6.52 직교여공간의 직교여공간**

$U$가 $V$의 유한차원 부분공간이면

$$
(U^\perp)^\perp=U.
$$

**증명**

먼저 $u\in U$이면 $u$는 $U^\perp$의 모든 벡터에 직교한다. 따라서

$$
U\subset (U^\perp)^\perp.
\tag{6.53}
$$

이제 6.51을 두 번 적용하면

$$
\dim (U^\perp)^\perp
=\dim V-\dim U^\perp
=\dim V-(\dim V-\dim U)
=\dim U
$$

이다. 6.53의 포함관계와 두 공간의 차원이 같다는 사실에서 결론이 따른다.

**6.54 직교여공간이 $\lbrace0\rbrace$인 경우**

$U$가 유한차원 내적공간 $V$의 부분공간이면

$$
U^\perp=\lbrace0\rbrace
$$

인 것과 $U=V$인 것은 동치이다.

**증명**

$U=V$이면 6.48(c)에 의해 $U^\perp=\lbrace0\rbrace$이다. 반대로 $U^\perp=\lbrace0\rbrace$이면 6.51에 의해 $\dim U=\dim V$이고, 따라서 $U=V$이다.

**6.55 정의: 직교사영**

$U$가 $V$의 유한차원 부분공간이라고 하자. 6.49에 의해 각 $v\in V$는 유일하게

$$
v=u+w,\qquad u\in U,\quad w\in U^\perp
$$

로 쓸 수 있다. $P_Uv=u$로 정의되는 사상 $P_U:V\to V$를 $U$ 위로의 **직교사영**이라고 한다.

**6.56 예: 일차원 부분공간 위로의 직교사영**

$u\in V$이고 $u\ne 0$라고 하자. $U=\text{span}(u)$이면 모든 $v\in V$에 대해

$$
P_Uv=\frac{\langle v,u\rangle}{\Vert u\Vert^2}u.
$$

실제로 $v-\frac{\langle v,u\rangle}{\Vert u\Vert^2}u$는 $u$에 직교하므로 위 식이 직교사영의 정의와 일치한다.

**6.57 직교사영의 성질**

$U$가 $V$의 유한차원 부분공간이라고 하자. 그러면 다음이 성립한다.

(a) $P_U\in\mathcal{L}(V)$.

(b) 모든 $u\in U$에 대해 $P_Uu=u$.

(c) 모든 $w\in U^\perp$에 대해 $P_Uw=0$.

(d) $\text{range}P_U=U$.

(e) $\text{null}P_U=U^\perp$.

(f) 모든 $v\in V$에 대해 $v-P_Uv\in U^\perp$.

(g) $P_U^2=P_U$.

(h) 모든 $v\in V$에 대해 $\Vert P_Uv\Vert\le \Vert v\Vert$.

(i) $e_1,\ldots,e_m$이 $U$의 정규직교기저이면 모든 $v\in V$에 대해

$$
P_Uv=\langle v,e_1\rangle e_1+\cdots+\langle v,e_m\rangle e_m.
$$

**증명**

(i)는 6.50의 $u$ 부분이 바로 $P_Uv$라는 사실에서 나온다. (a)는 (i)의 식에서 선형성이 바로 보인다. (b), (c), (d), (e), (f)는 직교사영의 정의에서 즉시 따른다. (g)는 $P_Uv\in U$이므로 (b)를 $P_Uv$에 적용하면 된다. (h)는 $v=P_Uv+(v-P_Uv)$이고 두 항이 서로 직교하므로 피타고라스 정리에 의해

$$
\Vert v\Vert^2=\Vert P_Uv\Vert^2+\Vert v-P_Uv\Vert^2\ge \Vert P_Uv\Vert^2
$$

이다.

**6.58 리스 표현정리의 또 다른 증명**

$V$가 유한차원 내적공간이라고 하자. 각 $v\in V$에 대해 $\varphi_v\in V'$를

$$
\varphi_v(u)=\langle u,v\rangle
$$

로 정의한다. 그러면 $v\mapsto\varphi_v$는 $V$에서 $V'$로 가는 일대일 대응이다.

$\mathbb{F}=\mathbb{R}$이면 이 대응은 선형이다. 그러나 $\mathbb{F}=\mathbb{C}$이면 일반적으로 선형이 아니다. 실제로

$$
\varphi_{\lambda v}=\overline{\lambda}\varphi_v
$$

이기 때문이다.

**증명**

일대일성은 $\varphi_v=0$이면 $\Vert v\Vert^2=\varphi_v(v)=0$이므로 $v=0$이라는 사실에서 따른다. 이제 임의의 $\varphi\in V'$가 어떤 $\varphi_v$와 같음을 보이면 된다.

$\varphi=0$이면 $v=0$을 택하면 된다. 이제 $\varphi\ne 0$이라고 하자. 그러면 $\text{null}\varphi\ne V$이므로 6.54에 의해 $(\text{null}\varphi)^\perp\ne\lbrace0\rbrace$이다. $0\ne w\in(\text{null}\varphi)^\perp$를 택하고

$$
v=\frac{\overline{\varphi(w)}}{\Vert w\Vert^2}w
\tag{6.59}
$$

라고 두자. 그러면

$$
\Vert v\Vert=\frac{|\varphi(w)|}{\Vert w\Vert}
\tag{6.60}
$$

이고 $\varphi(v)=\Vert v\Vert^2$이다. 임의의 $u\in V$에 대해

$$
u-\frac{\varphi(u)}{\varphi(v)}v\in\text{null}\varphi
$$

이다. 이 벡터는 $v$에 직교하므로

$$
\left\langle u-\frac{\varphi(u)}{\Vert v\Vert^2}v,v\right\rangle=0.
$$

따라서 $\langle u,v\rangle=\varphi(u)$이다. 즉 $\varphi=\varphi_v$이다.

### 최소화 문제

**6.61 부분공간까지의 거리 최소화**

$U$가 $V$의 유한차원 부분공간이고 $v\in V$, $u\in U$라고 하자. 그러면

$$
\Vert v-P_Uv\Vert\le \Vert v-u\Vert.
$$

또한 위 부등식에서 등호가 성립하는 것은 $u=P_Uv$인 것과 동치이다.

**증명**

$v-P_Uv\in U^\perp$이고 $P_Uv-u\in U$이므로 두 벡터는 서로 직교한다. 따라서

$$
\begin{aligned}
\Vert v-P_Uv\Vert^2
&\le \Vert v-P_Uv\Vert^2+\Vert P_Uv-u\Vert^2\cr
&=\Vert(v-P_Uv)+(P_Uv-u)\Vert^2\cr
&=\Vert v-u\Vert^2.
\end{aligned}
\tag{6.62}
$$

등호는 $\Vert P_Uv-u\Vert=0$일 때, 즉 $u=P_Uv$일 때 정확히 성립한다.

**6.63 예: 사인 함수의 최적 다항식 근사**

차수가 최대 $5$인 다항식 $u$ 중에서

$$
\int_{-\pi}^{\pi}|\sin x-u(x)|^2\thinspace dx
$$

를 최소로 만드는 $u$를 찾고 싶다고 하자. $C[-\pi,\pi]$에 내적

$$
\langle f,g\rangle=\int_{-\pi}^{\pi}f(x)g(x)\thinspace dx
\tag{6.64}
$$

를 주고, $v(x)=\sin x$, $U=\mathcal{P}_5(\mathbb{R})$라고 두면 이 문제는 $\Vert v-u\Vert$를 최소화하는 $u\in U$를 찾는 문제이다.

6.61에 의해 답은 $P_Uv$이다. $1,x,x^2,x^3,x^4,x^5$에 그램-슈미트 절차를 적용해 $U$의 정규직교기저를 만든 뒤 6.57(i)를 사용하면 계산 결과

$$
u(x)=0.987862x-0.155271x^3+0.00564312x^5
\tag{6.65}
$$

를 얻는다. 이것은 구간 $[-\pi,\pi]$ 전체에서 평균제곱오차를 가장 작게 만드는 차수 최대 $5$의 다항식이다.

테일러 다항식

$$
p(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}
\tag{6.66}
$$

은 $0$ 근처에서는 매우 좋은 근사이지만, $|x|>2$에서는 6.65의 최적 근사보다 훨씬 나빠질 수 있다. 예를 들어 $x=3$에서 테일러 다항식의 오차는 대략 $0.4$인 반면, 6.65의 오차는 대략 $0.001$이다.

### 유사역

선형방정식 $Tv=w$를 생각하자. $T$가 가역이면 해는 $v=T^{-1}w$ 하나뿐이다. 그러나 $T$가 가역이 아니면 해가 없을 수도 있고, 여러 개 있을 수도 있다. 이때 자연스러운 질문은 두 가지이다.

- 해가 없으면 $\Vert Tv-w\Vert$를 최소로 만드는 $v$는 무엇인가?
- 해가 여러 개이면 그중 $\Vert v\Vert$가 가장 작은 해는 무엇인가?

유사역은 이 두 질문에 동시에 답을 준다.

**6.67 제한된 선형사상**

$V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 그러면

$$
T|_{(\text{null}T)^\perp}
$$

는 $(\text{null}T)^\perp$에서 $\text{range}T$로 가는 일대일 대응인 선형사상이다.

**증명**

제한사상이 선형이고 치역이 $\text{range}T$에 포함되는 것은 분명하다. 만약 $v\in(\text{null}T)^\perp$이고 $Tv=0$이면 $v\in\text{null}T\cap(\text{null}T)^\perp$이므로 $v=0$이다. 따라서 제한사상은 단사이다.

임의의 $w\in\text{range}T$에 대해 $w=Tv$인 $v\in V$를 택하자. $v=P_{(\text{null}T)^\perp}v+P_{\text{null}T}v$이고 $P_{\text{null}T}v\in\text{null}T$이므로

$$
w=Tv=T(P_{(\text{null}T)^\perp}v).
$$

따라서 제한사상은 $\text{range}T$ 위로 전사이다.

**6.68 정의: 유사역**

$V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. $T$의 **유사역** $T^\dagger\in\mathcal{L}(W,V)$는

$$
T^\dagger w
=\left(T|_{(\text{null}T)^\perp}\right)^{-1}
P_{\text{range}T}w
$$

로 정의된다.

즉 $w\in(\text{range}T)^\perp$이면 $T^\dagger w=0$이다. 또한 $w\in\text{range}T$이면 $T^\dagger w$는 $(\text{null}T)^\perp$에 속하고 $T(T^\dagger w)=w$를 만족하는 유일한 벡터이다.

**6.69 유사역의 대수적 성질**

$V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 그러면 다음이 성립한다.

(a) $T$가 가역이면 $T^\dagger=T^{-1}$이다.

(b) $TT^\dagger$는 $W$에서 $\text{range}T$ 위로의 직교사영이다. 즉

$$
TT^\dagger=P_{\text{range}T}.
$$

(c) $T^\dagger T$는 $V$에서 $(\text{null}T)^\perp$ 위로의 직교사영이다. 즉

$$
T^\dagger T=P_{(\text{null}T)^\perp}.
$$

**증명**

(a)는 $T$가 가역이면 $\text{null}T=\lbrace0\rbrace$이고 $\text{range}T=W$이므로 정의에서 바로 따른다.

(b)는 $w\in W$에 대해 $T^\dagger w$가 $P_{\text{range}T}w$의 제한사상 아래의 역상이 되도록 정의되었기 때문에

$$
TT^\dagger w=P_{\text{range}T}w
$$

이다.

(c)는 $v\in V$를 $v=u+n$으로 쓰되 $u\in(\text{null}T)^\perp$, $n\in\text{null}T$라고 하자. 그러면 $Tv=Tu$이고, 정의상 $T^\dagger(Tu)=u$이다. 따라서 $T^\dagger Tv=u=P_{(\text{null}T)^\perp}v$이다.

유사역은 무어-펜로즈 역이라고도 불린다. $T$가 전사이면 $TT^\dagger=I$이고, $T$가 단사이면 $T^\dagger T=I$이다.

**6.70 유사역이 주는 최적해**

$V$가 유한차원이고 $T\in\mathcal{L}(V,W)$, $w\in W$라고 하자. 그러면 다음이 성립한다.

(a) 모든 $v\in V$에 대해

$$
\Vert T(T^\dagger w)-w\Vert\le \Vert Tv-w\Vert.
$$

또한 등호가 성립하는 것은 $v\in T^\dagger w+\text{null}T$인 것과 동치이다.

(b) $v\in T^\dagger w+\text{null}T$이면

$$
\Vert T^\dagger w\Vert\le \Vert v\Vert.
$$

또한 등호가 성립하는 것은 $v=T^\dagger w$인 것과 동치이다.

**증명**

(a)는 $T(T^\dagger w)=P_{\text{range}T}w$이고 $Tv\in\text{range}T$이므로 6.61을 $W$의 부분공간 $\text{range}T$에 적용하면 얻어진다. 등호 조건도 6.61의 등호 조건에서 나온다.

(b) $v=T^\dagger w+n$이고 $n\in\text{null}T$라고 쓰면 $T^\dagger w\in(\text{null}T)^\perp$이므로 두 항은 직교한다. 따라서

$$
\Vert v\Vert^2=\Vert T^\dagger w\Vert^2+\Vert n\Vert^2.
$$

등호는 $n=0$일 때 정확히 성립한다.

**6.71 예: $\mathbb{F}^4$에서 $\mathbb{F}^3$으로 가는 선형사상의 유사역**

$T\in\mathcal{L}(\mathbb{F}^4,\mathbb{F}^3)$를

$$
T(a,b,c,d)=(a+b+c,2c+d,0)
$$

으로 정의하자. 그러면

$$
\text{range}T=\lbrace(x,y,0):x,y\in\mathbb{F}\rbrace
$$

이고, 따라서

$$
P_{\text{range}T}(x,y,z)=(x,y,0).
$$

또한

$$
\text{null}T
=\lbrace(a,b,c,d):a+b+c=0,\ 2c+d=0\rbrace
$$

이며 이 공간의 한 기저는

$$
(-1,1,0,0),\quad (-1,0,1,-2)
$$

이다. 따라서 $T^\dagger(x,y,z)$는

$$
T^\dagger(x,y,z)
=\left(T|_{(\text{null}T)^\perp}\right)^{-1}(x,y,0)
\tag{6.72}
$$

이다.

이를 구하려면 다음 연립방정식을 풀면 된다.

$$
\begin{aligned}
a+b+c&=x,\cr
2c+d&=y,\cr
-a+b&=0,\cr
-a+c-2d&=0.
\end{aligned}
$$

첫 두 식은 $T(a,b,c,d)=(x,y,0)$이라는 조건이고, 뒤의 두 식은 $(a,b,c,d)\in(\text{null}T)^\perp$라는 조건이다. 해는

$$
a=\frac{5x-2y}{11},\quad
b=\frac{5x-2y}{11},\quad
c=\frac{x+4y}{11},\quad
d=\frac{-2x+3y}{11}
$$

이다. 따라서

$$
T^\dagger(x,y,z)
=\frac{1}{11}(5x-2y,5x-2y,x+4y,-2x+3y).
$$

특히 $TT^\dagger(x,y,z)=(x,y,0)$이므로 6.69(b)를 이 예에서 직접 확인할 수 있다.

### 연습문제 6C

1. $v_1,\ldots,v_m\in V$라고 하자. 다음을 증명하여라.

   $$
   \lbrace v_1,\ldots,v_m\rbrace^\perp
   =\left(\text{span}(v_1,\ldots,v_m)\right)^\perp.
   $$

2. $U$가 $V$의 유한차원 부분공간이고 $u_1,\ldots,u_m$이 $U$의 기저라고 하자. 또한 $u_1,\ldots,u_m,v_1,\ldots,v_n$이 $V$의 기저라고 하자. 이 기저에 그램-슈미트 절차를 적용하여 얻은 리스트를 $e_1,\ldots,e_m,f_1,\ldots,f_n$이라고 하자. 그러면 $e_1,\ldots,e_m$은 $U$의 정규직교기저이고 $f_1,\ldots,f_n$은 $U^\perp$의 정규직교기저임을 증명하여라.

3. $\mathbb{R}^4$에서

   $$
   U=\text{span}((1,2,3,-4),(-5,4,3,2))
   $$

   라고 하자. $U$의 정규직교기저와 $U^\perp$의 정규직교기저를 각각 구하여라.

4. $e_1,\ldots,e_n$이 $V$의 벡터들로 이루어진 리스트이고 각 $e_k$의 노름이 $1$이라고 하자. 모든 $v\in V$에 대해

   $$
   \Vert v\Vert^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2
   $$

   가 성립하면 $e_1,\ldots,e_n$이 $V$의 정규직교기저임을 증명하여라.

5. $V$가 유한차원이고 $U$가 $V$의 부분공간이라고 하자. 다음을 증명하여라.

   $$
   P_{U^\perp}=I-P_U.
   $$

6. $V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

   $$
   T=TP_{(\text{null}T)^\perp}
   =P_{\text{range}T}T.
   $$

7. $V$가 유한차원이고 $X,Y$가 $V$의 부분공간이라고 하자. 다음 두 조건이 동치임을 증명하여라.

   $$
   P_XP_Y=0
   $$

   그리고 모든 $x\in X$, $y\in Y$에 대해 $\langle x,y\rangle=0$.

8. $U$가 $V$의 유한차원 부분공간이고 $v\in V$라고 하자. $\varphi:U\to\mathbb{F}$를

   $$
   \varphi(u)=\langle u,v\rangle
   $$

   로 정의한다. 리스 표현정리를 $U$에 적용하면 모든 $u\in U$에 대해

   $$
   \varphi(u)=\langle u,w\rangle
   $$

   를 만족하는 $w\in U$가 존재한다. 이때 $w=P_Uv$임을 증명하여라.

9. $V$가 유한차원이고 $P\in\mathcal{L}(V)$가 $P^2=P$를 만족한다고 하자. 또한 $\text{null}P$의 모든 벡터가 $\text{range}P$의 모든 벡터에 직교한다고 하자. 그러면 어떤 $V$의 부분공간 $U$가 존재하여 $P=P_U$임을 증명하여라.

10. $V$가 유한차원이고 $P\in\mathcal{L}(V)$가 $P^2=P$를 만족하며 모든 $v\in V$에 대해 $\Vert Pv\Vert\le\Vert v\Vert$라고 하자. 그러면 어떤 $V$의 부분공간 $U$가 존재하여 $P=P_U$임을 증명하여라.

11. $T\in\mathcal{L}(V)$이고 $U$가 $V$의 유한차원 부분공간이라고 하자. $U$가 $T$에 대해 불변인 것과

    $$
    P_UTP_U=TP_U
    $$

    인 것은 동치임을 증명하여라.

12. $V$가 유한차원이고 $T\in\mathcal{L}(V)$, $U$가 $V$의 부분공간이라고 하자. $U$와 $U^\perp$가 모두 $T$에 대해 불변인 것과

    $$
    P_UT=TP_U
    $$

    인 것은 동치임을 증명하여라.

13. $\mathbb{F}=\mathbb{R}$이고 $V$가 유한차원이라고 하자. 각 $v\in V$에 대해 $\varphi_v\in V'$를 $\varphi_v(u)=\langle u,v\rangle$로 정의한다.

    (a) $v\mapsto\varphi_v$가 $V$에서 $V'$로 가는 단사 선형사상임을 증명하여라.

    (b) 차원 세기를 사용하여 $v\mapsto\varphi_v$가 $V$에서 $V'$로 가는 동형사상임을 증명하여라.

    (c) (a)와 (b)를 사용하여 실수 유한차원 내적공간에서의 리스 표현정리를 다시 증명하여라.

14. $e_1,\ldots,e_n$이 $V$의 정규직교기저라고 하자. 리스 표현정리로 $V$와 $V'$를 동일시하면, $e_1,\ldots,e_n$의 쌍대기저가 다시 $e_1,\ldots,e_n$이 되는 이유를 설명하여라.

15. $\mathbb{R}^4$에서

    $$
    U=\text{span}((1,1,0,0),(1,1,1,2))
    $$

    라고 하자. $u\in U$ 중에서

    $$
    \Vert u-(1,2,3,4)\Vert
    $$

    를 최소로 만드는 $u$를 구하여라.

16. $C[-1,1]$에 내적

    $$
    \langle f,g\rangle=\int_{-1}^{1}f(x)g(x)\thinspace dx
    $$

    가 주어져 있고

    $$
    U=\lbrace f\in C[-1,1]:f(0)=0\rbrace
    $$

    라고 하자.

    (a) $U^\perp=\lbrace0\rbrace$임을 증명하여라.

    (b) 6.49와 6.52는 유한차원이라는 가정 없이는 성립하지 않을 수 있음을 설명하여라.

17. $p\in\mathcal{P}_3(\mathbb{R})$가 $p(0)=0$과 $p'(0)=0$을 만족한다고 하자. 다음 적분을 최소로 만드는 $p$를 구하여라.

$$
\int_{0}^{1}|2+3x-p(x)|^2\thinspace dx.
$$

18. $p\in\mathcal{P}_5(\mathbb{R})$ 중에서

    $$
    \int_{-\pi}^{\pi}|\sin x-p(x)|^2\thinspace dx
    $$

    를 최소로 만드는 $p$를 정확한 식으로 구하여라.

19. $V$가 유한차원이고 $P$가 $V$의 어떤 부분공간 위로의 직교사영이라고 하자. $P^\dagger=P$임을 증명하여라.

20. $V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

    $$
    \text{null}T^\dagger=(\text{range}T)^\perp
    $$

    그리고

    $$
    \text{range}T^\dagger=(\text{null}T)^\perp.
    $$

21. $T\in\mathcal{L}(\mathbb{F}^3,\mathbb{F}^2)$가

    $$
    T(a,b,c)=(a+b+c,2b+3c)
    $$

    로 정의되어 있다고 하자.

    (a) $T^\dagger(x,y)$의 공식을 구하여라.

    (b) $TT^\dagger$가 $\mathbb{F}^2$에서 $\text{range}T$ 위로의 직교사영임을 직접 확인하여라.

    (c) $T^\dagger T$가 $\mathbb{F}^3$에서 $(\text{null}T)^\perp$ 위로의 직교사영임을 직접 확인하여라.

22. $V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

    $$
    TT^\dagger T=T
    $$

    그리고

    $$
    T^\dagger TT^\dagger=T^\dagger.
    $$

23. $V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라고 하자. 다음을 증명하여라.

    $$
    (T^\dagger)^\dagger=T.
    $$
