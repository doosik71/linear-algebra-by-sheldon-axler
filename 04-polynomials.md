# 4장 다항식

이 장에서는 한 벡터공간에서 자기 자신으로 가는 선형사상을 연구할 때 사용할 다항식 관련 내용을 다룬다. 이 장의 많은 결과는 다른 과목에서 이미 익숙할 수 있다. 여기서는 완결성을 위해 포함한다. 이 장은 선형대수 자체에 관한 장은 아니므로, 강의에서는 빠르게 지나갈 수도 있다. 그러나 적어도 이 장의 모든 결과의 진술은 읽고 이해해야 한다. 뒤의 장들에서 계속 사용될 것이기 때문이다.

이 장은 복소수의 대수적 성질에 대한 짧은 논의로 시작한다. 그런 다음 상수가 아닌 다항식이 그 차수보다 많은 영점을 가질 수 없음을 증명한다. 또한 다항식의 나눗셈 알고리즘을 선형대수에 바탕을 두어 증명한다. 선형대수를 사용하지 않는 증명에 이미 익숙하더라도, 이 증명은 읽을 가치가 있다.

앞으로 보겠지만, 대수학의 기본정리는 스칼라체가 $\mathbb{C}$이면 모든 다항식이 일차 인수들로 인수분해되고, 스칼라체가 $\mathbb{R}$이면 차수가 최대 $2$인 인수들로 인수분해된다는 사실로 이어진다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.

그림: 수학자이자 시인인 오마르 하이얌(1048-1131)의 동상. 그가 1070년에 쓴 대수학 책에는 삼차다항식에 대한 최초의 본격적인 연구가 들어 있었다.

## 복소수

복소수 계수 또는 실수 계수 다항식을 논의하기 전에, 복소수에 대해 조금 더 알아둘 필요가 있다.

**4.1 정의: 실수부, $\text{Re}z$, 허수부, $\text{Im}z$**

$z=a+bi$라고 하자. 여기서 $a$와 $b$는 실수이다.

- $z$의 **실수부**는 $\text{Re}z$로 나타내며, $\text{Re}z=a$로 정의한다.
- $z$의 **허수부**는 $\text{Im}z$로 나타내며, $\text{Im}z=b$로 정의한다.

따라서 모든 복소수 $z$에 대해

$$
z=\text{Re}z+(\text{Im}z)i
$$

이다.

**4.2 정의: 복소켤레, $\overline{z}$, 절댓값, $|z|$**

$z \in \mathbb{C}$라고 하자.

- $z$의 **복소켤레**는 $\overline{z}$로 나타내며,

  $$
  \overline{z}=\text{Re}z-(\text{Im}z)i
  $$

  로 정의한다.

- 복소수 $z$의 **절댓값**은 $|z|$로 나타내며,

  $$
  |z|=\sqrt{(\text{Re}z)^2+(\text{Im}z)^2}
  $$

  로 정의한다.

**4.3 예: 실수부, 허수부, 복소켤레, 절댓값**

$z=3+2i$라고 하자. 그러면

- $\text{Re}z=3$이고 $\text{Im}z=2$이다.
- $\overline{z}=3-2i$이다.
- $|z|=\sqrt{3^2+2^2}=\sqrt{13}$이다.

복소수 $z \in \mathbb{C}$를 순서쌍 $(\text{Re}z,\text{Im}z)\in\mathbb{R}^2$와 동일시하면 $\mathbb{C}$를 $\mathbb{R}^2$와 동일시할 수 있다. $\mathbb{C}$는 $1$차원 복소 벡터공간이지만, $\mathbb{R}^2$와 동일시된 $\mathbb{C}$를 $2$차원 실수 벡터공간으로 생각할 수도 있다.

각 복소수의 절댓값은 음이 아닌 수이다. 구체적으로 $z \in \mathbb{C}$이면, $|z|$는 $\mathbb{R}^2$의 원점에서 점 $(\text{Re}z,\text{Im}z)\in\mathbb{R}^2$까지의 거리와 같다.

$\overline{z}=z$일 필요충분조건은 $z$가 실수라는 것이다. 이를 확인하라.

실수부와 허수부, 복소켤레, 절댓값은 다음 여러 부분으로 된 결과에 나열된 성질들을 가진다.

**4.4 복소수의 성질**

$w,z\in\mathbb{C}$라고 하자. 그러면 다음 등식과 부등식이 성립한다.

$z$와 $\overline{z}$의 합:

$$
z+\overline{z}=2\text{Re}z.
$$

$z$와 $\overline{z}$의 차:

$$
z-\overline{z}=2(\text{Im}z)i.
$$

$z$와 $\overline{z}$의 곱:

$$
z\overline{z}=|z|^2.
$$

복소켤레의 덧셈성과 곱셈성:

$$
\overline{w+z}=\overline{w}+\overline{z}
\quad\text{그리고}\quad
\overline{wz}=\overline{w}\thinspace\overline{z}.
$$

복소켤레를 두 번 취하면 원래 수가 된다:

$$
\overline{\overline{z}}=z.
$$

실수부와 허수부는 $|z|$로 제한된다:

$$
|\text{Re}z|\le |z|
\quad\text{그리고}\quad
|\text{Im}z|\le |z|.
$$

복소켤레의 절댓값:

$$
|\overline{z}|=|z|.
$$

절댓값의 곱셈성:

$$
|wz|=|w|\thinspace|z|.
$$

삼각부등식:

$$
|w+z|\le |w|+|z|.
$$

기하학적으로 삼각부등식은 삼각형의 각 변의 길이가 나머지 두 변의 길이의 합보다 작거나 같다는 사실을 뜻한다.

증명. 위의 마지막 항목을 제외한 모든 주장은 직접 확인하는 일상적인 계산이므로 독자에게 맡긴다. 삼각부등식을 확인하기 위해 다음을 계산한다.

$$
\begin{aligned}
|w+z|^2
&=(w+z)\overline{(w+z)} \cr
&=(w+z)(\overline{w}+\overline{z}) \cr
&=w\overline{w}+z\overline{z}+w\overline{z}+z\overline{w} \cr
&=|w|^2+|z|^2+2\text{Re}(w\overline{z}) \cr
&\le |w|^2+|z|^2+2|w\overline{z}| \cr
&=|w|^2+|z|^2+2|w|\thinspace|z| \cr
&=(|w|+|z|)^2.
\end{aligned}
$$

이제 양변의 제곱근을 취하면 원하는 부등식 $|w+z|\le |w|+|z|$를 얻는다. 역삼각부등식은 연습문제 2번을 보라.

## 다항식의 영점

함수 $p:\mathbb{F}\to\mathbb{F}$가 차수 $m$의 다항식이라는 것은 $a_0,\ldots,a_m\in\mathbb{F}$가 존재하고 $a_m\ne 0$이며, 모든 $z\in\mathbb{F}$에 대해

$$
p(z)=a_0+a_1z+\cdots+a_mz^m
$$

가 성립한다는 뜻이었다. 위와 같은 꼴의 $p$의 표현이 유일하지 않다면, 하나의 다항식이 여러 차수를 가질 수도 있을 것이다. 우리의 첫 목표는 이런 일이 일어나지 않음을 보이는 것이다.

방정식 $p(z)=0$의 해는 다항식 $p\in\mathcal{P}(\mathbb{F})$를 연구할 때 핵심적인 역할을 한다. 그래서 이 해에는 특별한 이름이 붙어 있다.

**4.5 정의: 다항식의 영점**

$p(\lambda)=0$이면, 수 $\lambda\in\mathbb{F}$를 다항식 $p\in\mathcal{P}(\mathbb{F})$의 **영점** 또는 **근**이라고 한다.

다음 결과는 다항식의 차수가 유일하다는 것을 보일 때 사용할 핵심 도구이다.

**4.6 다항식의 각 영점은 일차 인수에 대응한다**

$m$이 양의 정수이고 $p\in\mathcal{P}(\mathbb{F})$가 차수 $m$의 다항식이라고 하자. 또한 $\lambda\in\mathbb{F}$라고 하자. 그러면 $p(\lambda)=0$일 필요충분조건은 차수 $m-1$의 다항식 $q\in\mathcal{P}(\mathbb{F})$가 존재하여 모든 $z\in\mathbb{F}$에 대해

$$
p(z)=(z-\lambda)q(z)
$$

가 성립하는 것이다.

증명. 먼저 $p(\lambda)=0$이라고 하자. 모든 $z\in\mathbb{F}$에 대해

$$
p(z)=a_0+a_1z+\cdots+a_mz^m
$$

가 되도록 $a_0,a_1,\ldots,a_m\in\mathbb{F}$를 잡는다. 그러면 모든 $z\in\mathbb{F}$에 대해

**(4.7)**

$$
p(z)=p(z)-p(\lambda)=a_1(z-\lambda)+\cdots+a_m(z^m-\lambda^m)
$$

이다. 각 $k\in\lbrace1,\ldots,m\rbrace$에 대해

$$
z^k-\lambda^k
=(z-\lambda)\sum_{j=1}^k \lambda^{j-1}z^{k-j}
$$

이므로, $z^k-\lambda^k$는 $z-\lambda$에 차수 $k-1$의 어떤 다항식을 곱한 것과 같다. 따라서 (4.7)은 $p$가 $z-\lambda$에 차수 $m-1$의 어떤 다항식을 곱한 것임을 보여 준다.

반대 방향을 증명하자. 어떤 다항식 $q\in\mathcal{P}(\mathbb{F})$가 존재하여 모든 $z\in\mathbb{F}$에 대해 $p(z)=(z-\lambda)q(z)$라고 하자. 그러면

$$
p(\lambda)=(\lambda-\lambda)q(\lambda)=0
$$

이므로 원하는 결론을 얻는다.

이제 다항식이 너무 많은 영점을 가질 수 없음을 증명할 수 있다.

**4.8 차수 $m$이면 영점은 최대 $m$개이다**

$m$이 양의 정수이고 $p\in\mathcal{P}(\mathbb{F})$가 차수 $m$의 다항식이라고 하자. 그러면 $p$는 $\mathbb{F}$ 안에서 최대 $m$개의 영점을 가진다.

증명. $m$에 대한 귀납법을 사용한다. $m=1$이면 원하는 결과가 성립한다. 실제로 $a_1\ne 0$이면 다항식 $a_0+a_1z$는 하나의 영점만 가지며, 그 영점은 $-a_0/a_1$이다. 이제 $m>1$이고, 원하는 결과가 $m-1$에 대해 성립한다고 가정하자.

$p$가 $\mathbb{F}$ 안에서 영점을 가지지 않으면 원하는 결과가 성립하므로 끝난다. 따라서 $p$가 어떤 영점 $\lambda\in\mathbb{F}$를 가진다고 하자. 4.6에 의해 차수 $m-1$의 다항식 $q\in\mathcal{P}(\mathbb{F})$가 존재하여 모든 $z\in\mathbb{F}$에 대해

$$
p(z)=(z-\lambda)q(z)
$$

가 성립한다. 귀납가정에 의해 $q$는 $\mathbb{F}$ 안에서 최대 $m-1$개의 영점을 가진다. 위 식은 $\mathbb{F}$ 안에서 $p$의 영점들이 $\lambda$와 $\mathbb{F}$ 안에서의 $q$의 영점들뿐임을 보여 준다. 따라서 $p$는 $\mathbb{F}$ 안에서 최대 $m$개의 영점을 가진다.

위 결과는 다항식의 계수들이 유일하게 결정됨을 함의한다. 만약 한 다항식이 서로 다른 두 계수 집합을 가진다면, 두 표현을 빼서 어떤 계수는 $0$이 아닌데 영점을 무한히 많이 가지는 다항식을 얻게 되기 때문이다. 특히 다항식의 차수는 유일하게 정의된다.

$0$ 다항식의 차수는 $-\infty$로 정의한다. 이렇게 하면

$$
\deg(pq)=\deg p+\deg q
$$

같은 자연스러운 결과를 다룰 때 예외를 둘 필요가 없다. 필요할 때는 $-\infty$에 대해 기대되는 산술을 사용한다. 예를 들어 모든 정수 $m$에 대해 $-\infty<m$이고 $-\infty+m=-\infty$이다.

## 다항식의 나눗셈 알고리즘

$p$와 $s$가 음이 아닌 정수이고 $s\ne 0$이면, 음이 아닌 정수 $q$와 $r$이 존재하여

$$
p=sq+r
$$

이고 $r<s$이다. 이를 $p$를 $s$로 나누어 몫 $q$와 나머지 $r$을 얻는 것으로 생각하라. 다음 결과는 다항식에 대한 유사한 결과를 준다. 따라서 다음 결과는 흔히 다항식의 나눗셈 알고리즘이라고 불린다. 다만 여기서 서술된 형태는 실제 알고리즘이라기보다는 유용한 결과이다.

다항식의 나눗셈 알고리즘은 다항식 $p$를 다항식 $s$로 나눌 때 나머지 다항식 $r$을 준다고 생각하라.

다항식의 나눗셈 알고리즘은 선형대수를 사용하지 않고도 증명할 수 있다. 그러나 선형대수 교재에 어울리게, 여기서 주는 증명은 선형대수 기법을 사용한다. 이 증명은 계수가 $\mathbb{F}$에 있고 차수가 최대 $n$인 다항식들의 $(n+1)$차원 벡터공간 $\mathcal{P}_n(\mathbb{F})$의 기저를 보기 좋게 활용한다.

**4.9 다항식의 나눗셈 알고리즘**

$p,s\in\mathcal{P}(\mathbb{F})$이고 $s\ne 0$이라고 하자. 그러면 다음을 만족하는 다항식 $q,r\in\mathcal{P}(\mathbb{F})$가 유일하게 존재한다.

$$
p=sq+r
$$

그리고

$$
\deg r<\deg s.
$$

증명. $n=\deg p$이고 $m=\deg s$라고 하자. $n<m$이면 $q=0$과 $r=p$를 택하면 원하는 식 $p=sq+r$와 $\deg r<\deg s$를 얻는다. 따라서 이제 $n\ge m$이라고 가정한다.

다음 리스트를 보자.

**(4.10)**

$$
1,z,\ldots,z^{m-1},s,zs,\ldots,z^{n-m}s
$$

이 리스트의 각 다항식은 서로 다른 차수를 가지므로 $\mathcal{P}_n(\mathbb{F})$에서 선형독립이다. 또한 (4.10)의 길이는 $n+1$이고, 이는 $\dim\mathcal{P}_n(\mathbb{F})$와 같다. 따라서 (4.10)은 2.38에 의해 $\mathcal{P}_n(\mathbb{F})$의 기저이다.

$p\in\mathcal{P}_n(\mathbb{F})$이고 (4.10)이 $\mathcal{P}_n(\mathbb{F})$의 기저이므로, 다음을 만족하는 상수 $a_0,a_1,\ldots,a_{m-1}\in\mathbb{F}$와 $b_0,b_1,\ldots,b_{n-m}\in\mathbb{F}$가 유일하게 존재한다.

**(4.11)**

$$
\begin{aligned}
p
&=a_0+a_1z+\cdots+a_{m-1}z^{m-1}
+b_0s+b_1zs+\cdots+b_{n-m}z^{n-m}s \cr
&=\underbrace{a_0+a_1z+\cdots+a_{m-1}z^{m-1}}_{r}
+s\underbrace{(b_0+b_1z+\cdots+b_{n-m}z^{n-m})}_{q}.
\end{aligned}
$$

위에서 정의한 $r$과 $q$에 대해 $p=sq+r$이고 $\deg r<\deg s$임을 알 수 있다.

이 조건을 만족하는 $q,r\in\mathcal{P}(\mathbb{F})$의 유일성은 (4.11)을 만족하는 상수 $a_0,a_1,\ldots,a_{m-1}\in\mathbb{F}$와 $b_0,b_1,\ldots,b_{n-m}\in\mathbb{F}$의 유일성에서 따라온다.

## $\mathbb{C}$ 위에서의 다항식 인수분해

대수학의 기본정리는 존재정리이다. 그 증명은 영점을 찾는 방법을 제공하지 않는다. 이차공식은 차수 $2$인 다항식의 영점을 명시적으로 준다. 차수 $3$과 $4$인 다항식에 대해서도 이와 비슷하지만 더 복잡한 공식들이 있다. 차수 $5$ 이상인 다항식에는 그런 공식이 존재하지 않는다.

우리는 $\mathbb{F}$가 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다고 두어 복소수 계수 다항식과 실수 계수 다항식을 동시에 다루어 왔다. 이제 이 두 경우 사이의 차이를 보게 된다. 먼저 복소수 계수 다항식을 다룬다. 그 다음 그 결과를 사용하여 실수 계수 다항식에 대응하는 결과를 증명한다.

대수학의 기본정리에 대한 우리의 증명은 $\mathbb{R}^2$의 닫힌 원판 위의 연속 실숫값 함수가 최솟값을 가진다는 결과를 암묵적으로 사용한다. 웹 검색을 해 보면 대수학의 기본정리에 대한 여러 다른 증명을 찾을 수 있다. 해석함수에 익숙하다면 리우빌 정리를 사용하는 증명이 특히 아름답다. 대수학의 기본정리의 모든 증명은 어떤 형태로든 해석학을 사용해야 한다. 예를 들어 $\mathbb{C}$를 $c+di$ 꼴의 수들의 집합으로 바꾸되 $c,d$를 유리수로 제한하면 이 결과는 참이 아니기 때문이다.

**4.12 대수학의 기본정리, 첫 번째 형태**

복소수 계수를 가지는 모든 상수가 아닌 다항식은 $\mathbb{C}$ 안에 영점을 가진다.

증명. 드무아브르 정리는 다음과 같다. $k$가 양의 정수이고 $\theta\in\mathbb{R}$이면

$$
(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta.
$$

이 정리는 $k$에 대한 귀납법과 코사인, 사인의 덧셈공식을 사용하여 증명할 수 있다.

$w\in\mathbb{C}$이고 $k$가 양의 정수라고 하자. 극좌표를 사용하면 어떤 $r\ge 0$과 $\theta\in\mathbb{R}$가 존재하여

$$
r(\cos\theta+i\sin\theta)=w
$$

가 된다. 드무아브르 정리는

$$
\left(r^{1/k}\left(\cos\frac{\theta}{k}+i\sin\frac{\theta}{k}\right)\right)^k=w
$$

를 함의한다. 따라서 모든 복소수는 $k$제곱근을 가진다. 이 사실을 곧 사용할 것이다.

$p$가 복소수 계수를 가지는 상수가 아닌 다항식이고, 최고차 비영항이 $c_mz^m$이라고 하자. 그러면 $|z|\to\infty$일 때 $|p(z)|\to\infty$이다. 실제로 $|z|\to\infty$일 때

$$
\frac{|p(z)|}{|z^m|}\to |c_m|
$$

이기 때문이다. 따라서 연속함수 $z\mapsto |p(z)|$는 어떤 점 $\zeta\in\mathbb{C}$에서 전역 최솟값을 가진다. $p(\zeta)=0$임을 보이기 위해 $p(\zeta)\ne 0$이라고 가정하자.

새 다항식 $q$를

$$
q(z)=\frac{p(z+\zeta)}{p(\zeta)}
$$

로 정의한다. 함수 $z\mapsto |q(z)|$는 $z=0$에서 전역 최솟값 $1$을 가진다.

$$
q(z)=1+a_kz^k+\cdots+a_mz^m
$$

라고 쓰자. 여기서 $k$는 $z^k$의 계수가 $0$이 아닌 가장 작은 양의 정수이다. 다시 말해 $a_k\ne 0$이다.

$\beta\in\mathbb{C}$가

$$
\beta^k=-\frac{1}{a_k}
$$

를 만족하도록 잡는다. 상수 $c>1$가 존재하여 $t\in(0,1)$이면

$$
\begin{aligned}
|q(t\beta)|
&\le |1+a_kt^k\beta^k|+t^{k+1}c \cr
&=1-t^k(1-tc).
\end{aligned}
$$

따라서 위 부등식에서 $t=1/(2c)$를 취하면 $|q(t\beta)|<1$이다. 이는 $z\mapsto |q(z)|$의 전역 최솟값이 $1$이라는 가정과 모순이다. 이 모순은 $p(\zeta)=0$임을 뜻한다. 따라서 $p$는 원하는 대로 영점을 가진다.

컴퓨터는 기발한 수치적 방법을 사용하여 정확한 영점을 찾을 수 없는 경우에도 임의의 다항식의 영점에 대한 좋은 근삿값을 찾을 수 있다. 예를 들어 다음 다항식 $p$의 영점에 대한 정확한 공식은 결코 주어지지 않을 것이다.

$$
p(x)=x^5-5x^4-6x^3+17x^2+4x-7.
$$

그러나 컴퓨터는 $p$의 영점이 대략 다음 다섯 수임을 찾을 수 있다.

$$
-1.87,\quad -0.74,\quad 0.62,\quad 1.47,\quad 5.51.
$$

대수학의 기본정리의 첫 번째 형태는 복소수 계수 다항식에 대한 다음 인수분해 결과로 이어진다. 이 인수분해에서 $p$의 영점은 $\lambda_1,\ldots,\lambda_m$이다. 이 값들만이 다음 결과의 등식 오른쪽을 $0$으로 만드는 $z$의 값이다.

**4.13 대수학의 기본정리, 두 번째 형태**

$p\in\mathcal{P}(\mathbb{C})$가 상수가 아닌 다항식이면, $p$는 다음 꼴의 인수분해를 가진다.

$$
p(z)=c(z-\lambda_1)\cdots(z-\lambda_m),
$$

여기서 $c,\lambda_1,\ldots,\lambda_m\in\mathbb{C}$이다. 이 인수분해는 인수들의 순서를 제외하고 유일하다.

증명. $p\in\mathcal{P}(\mathbb{C})$이고 $m=\deg p$라고 하자. $m$에 대한 귀납법을 사용한다. $m=1$이면 원하는 인수분해가 존재하고 유일하다. 이제 $m>1$이고, 차수 $m-1$인 모든 다항식에 대해 원하는 인수분해가 존재하고 유일하다고 가정하자.

먼저 $p$의 원하는 인수분해가 존재함을 보이자. 대수학의 기본정리의 첫 번째 형태(4.12)에 의해 $p$는 어떤 영점 $\lambda\in\mathbb{C}$를 가진다. 4.6에 의해 차수 $m-1$의 다항식 $q$가 존재하여 모든 $z\in\mathbb{C}$에 대해

$$
p(z)=(z-\lambda)q(z)
$$

가 성립한다. 귀납가정에 의해 $q$는 원하는 인수분해를 가진다. 이를 위 식에 대입하면 $p$의 원하는 인수분해를 얻는다.

이제 유일성을 살펴보자. 수 $c$는 $p$에서 $z^m$의 계수로 유일하게 결정된다. 따라서 순서를 제외하고 $\lambda_1,\ldots,\lambda_m$을 고르는 방법이 하나뿐임을 보이면 충분하다. 모든 $z\in\mathbb{C}$에 대해

$$
(z-\lambda_1)\cdots(z-\lambda_m)
=(z-\tau_1)\cdots(z-\tau_m)
$$

라고 하자. 위 등식의 왼쪽은 $z=\lambda_1$일 때 $0$이므로, 오른쪽의 $\tau$들 중 하나는 $\lambda_1$과 같다. 이름을 다시 붙여 $\tau_1=\lambda_1$이라고 가정할 수 있다. 이제 $z\ne\lambda_1$이면 위 등식의 양변을 $z-\lambda_1$로 나누어

$$
(z-\lambda_2)\cdots(z-\lambda_m)
=(z-\tau_2)\cdots(z-\tau_m)
$$

를 얻는다. 이 등식은 적어도 $z=\lambda_1$일 가능성을 제외한 모든 $z\in\mathbb{C}$에 대해 성립한다. 사실 이 등식은 모든 $z\in\mathbb{C}$에 대해 성립한다. 그렇지 않다면 오른쪽을 왼쪽에서 빼서 $0$이 아닌 다항식이 무한히 많은 영점을 가지게 되기 때문이다. 위 등식과 귀납가정은 순서를 제외하고 $\lambda$들이 $\tau$들과 같음을 함의한다. 이로써 유일성의 증명이 끝난다.

## $\mathbb{R}$ 위에서의 다항식 인수분해

$\mathbb{R}$에 대해서는 대수학의 기본정리가 실패한다. 이것이 앞으로 보게 될 실수 벡터공간 위의 선형대수와 복소수 벡터공간 위의 선형대수 사이의 차이를 설명한다.

실수 계수를 가지는 다항식은 실수 영점을 전혀 가지지 않을 수 있다. 예를 들어 다항식 $1+x^2$는 실수 영점이 없다.

$\mathbb{R}$ 위에서의 인수분해 정리를 얻기 위해, 우리는 $\mathbb{C}$ 위에서의 인수분해 정리를 사용할 것이다. 다음 결과에서 시작하자.

**4.14 실수 계수 다항식의 비실수 영점은 켤레쌍으로 나타난다**

$p\in\mathcal{P}(\mathbb{C})$가 실수 계수를 가지는 다항식이라고 하자. $\lambda\in\mathbb{C}$가 $p$의 영점이면 $\overline{\lambda}$도 $p$의 영점이다.

증명. $a_0,\ldots,a_m$이 실수이고

$$
p(z)=a_0+a_1z+\cdots+a_mz^m
$$

라고 하자. $\lambda\in\mathbb{C}$가 $p$의 영점이라고 하자. 그러면

$$
a_0+a_1\lambda+\cdots+a_m\lambda^m=0.
$$

이 등식의 양변에 복소켤레를 취하면

$$
a_0+a_1\overline{\lambda}+\cdots+a_m\overline{\lambda}^{\thinspace m}=0
$$

을 얻는다. 여기서 복소켤레의 기본 성질(4.4)을 사용했다. 위 식은 $\overline{\lambda}$가 $p$의 영점임을 보여 준다.

아래 결과와 관련하여 이차공식을 생각해 보라.

실수 계수 다항식에 대한 인수분해 정리가 필요하다. 다음 결과에서 시작한다.

**4.15 이차다항식의 인수분해**

$b,c\in\mathbb{R}$라고 하자. 그러면

$$
x^2+bx+c=(x-\lambda_1)(x-\lambda_2)
$$

꼴의 다항식 인수분해가 $\lambda_1,\lambda_2\in\mathbb{R}$에 대해 존재할 필요충분조건은 $b^2\ge 4c$이다.

증명. 다음을 주목하라.

$$
x^2+bx+c=\left(x+\frac{b}{2}\right)^2+\left(c-\frac{b^2}{4}\right).
$$

위 등식은 완전제곱식 만들기라고 불리는 기법의 바탕이다.

먼저 $b^2<4c$라고 하자. 그러면 위 등식의 오른쪽은 모든 $x\in\mathbb{R}$에 대해 양수이다. 따라서 다항식 $x^2+bx+c$는 실수 영점을 가지지 않고, 따라서 $\lambda_1,\lambda_2\in\mathbb{R}$에 대해 $(x-\lambda_1)(x-\lambda_2)$ 꼴로 인수분해될 수 없다.

반대로 이제 $b^2\ge 4c$라고 하자. 그러면

$$
d^2=\frac{b^2}{4}-c
$$

를 만족하는 실수 $d$가 존재한다. 앞의 등식에서

$$
\begin{aligned}
x^2+bx+c
&=\left(x+\frac{b}{2}\right)^2-d^2 \cr
&=\left(x+\frac{b}{2}+d\right)\left(x+\frac{b}{2}-d\right)
\end{aligned}
$$

를 얻고, 이것이 원하는 인수분해이다.

다음 결과는 $\mathbb{R}$ 위에서 다항식을 인수분해한다. 증명의 아이디어는 대수학의 기본정리의 두 번째 형태(4.13)를 사용하여 $p$를 복소수 계수 다항식으로 인수분해하는 것이다. $p$의 복소수이지만 실수가 아닌 영점들은 쌍으로 나타난다. 4.14를 보라. 따라서 $p$를 $\mathcal{P}(\mathbb{C})$의 원소로 인수분해했을 때 $\lambda$가 실수가 아닌 복소수이고 $(x-\lambda)$ 꼴의 항이 나타난다면, $(x-\overline{\lambda})$도 인수로 나타난다. 이 두 인수를 곱하면

$$
x^2-2(\text{Re}\lambda)x+|\lambda|^2
$$

를 얻는다. 이것은 필요한 형태의 이차 인수이다.

위 문단에서 개략적으로 설명한 아이디어는 원하는 인수분해의 존재 증명에 거의 충분하다. 그러나 한 가지 점을 조심해야 한다. $\lambda$가 실수가 아닌 복소수이고, $p$를 $\mathcal{P}(\mathbb{C})$의 원소로 인수분해했을 때 $(x-\lambda)$가 인수로 나타난다고 하자. 4.14에 의해 $(x-\overline{\lambda})$도 인수로 나타난다는 것은 보장된다. 그러나 4.14는 이 두 인수가 같은 횟수만큼 나타난다고 말하지 않는다. 위 아이디어가 작동하려면 이 점이 필요하다. 아래 증명은 이 문제를 우회한다.

다음 결과에서 $m$ 또는 $M$이 $0$일 수도 있다. 수 $\lambda_1,\ldots,\lambda_m$은 정확히 $p$의 실수 영점들이다. 다음 등식의 오른쪽이 $0$이 되는 실수 $x$의 값은 이 값들뿐이기 때문이다.

**4.16 $\mathbb{R}$ 위에서의 다항식 인수분해**

$p\in\mathcal{P}(\mathbb{R})$가 상수가 아닌 다항식이라고 하자. 그러면 $p$는 다음 꼴의 인수분해를 가진다.

$$
p(x)=c(x-\lambda_1)\cdots(x-\lambda_m)(x^2+b_1x+c_1)\cdots(x^2+b_Mx+c_M),
$$

여기서

$$
c,\lambda_1,\ldots,\lambda_m,b_1,\ldots,b_M,c_1,\ldots,c_M\in\mathbb{R}
$$

이고, 각 $k$에 대해 $b_k^2<4c_k$이다. 이 인수분해는 인수들의 순서를 제외하고 유일하다.

증명. 먼저 원하는 인수분해가 존재함을 증명하고, 그 뒤 유일성을 증명한다.

$p$를 $\mathcal{P}(\mathbb{C})$의 원소로 생각하자. $p$의 모든 복소수 영점이 실수이면 4.13에 의해 원하는 인수분해를 얻는다. 따라서 $p$가 $\lambda\notin\mathbb{R}$인 영점 $\lambda\in\mathbb{C}$를 가진다고 하자. 4.14에 의해 $\overline{\lambda}$도 $p$의 영점이다. 따라서 어떤 다항식 $q\in\mathcal{P}(\mathbb{C})$에 대해

$$
\begin{aligned}
p(x)
&=(x-\lambda)(x-\overline{\lambda})q(x) \cr
&=\left(x^2-2(\text{Re}\lambda)x+|\lambda|^2\right)q(x)
\end{aligned}
$$

라고 쓸 수 있다. 여기서 $q$의 차수는 $p$의 차수보다 $2$ 작다. $q$가 실수 계수를 가진다는 것을 증명할 수 있다면, $p$의 차수에 대한 귀납법으로 이 결과의 존재 부분이 끝난다.

$q$가 실수 계수를 가진다는 것을 보이기 위해 위 식을 $q$에 대해 풀면, 모든 $x\in\mathbb{R}$에 대해

$$
q(x)=\frac{p(x)}{x^2-2(\text{Re}\lambda)x+|\lambda|^2}
$$

이다. 위 등식은 모든 $x\in\mathbb{R}$에 대해 $q(x)\in\mathbb{R}$임을 함의한다. $n=\deg p$이고 $a_0,\ldots,a_{n-2}\in\mathbb{C}$라고 하여

$$
q(x)=a_0+a_1x+\cdots+a_{n-2}x^{n-2}
$$

라고 쓰자. 그러면 모든 $x\in\mathbb{R}$에 대해

$$
0=\text{Im}q(x)
=(\text{Im}a_0)+(\text{Im}a_1)x+\cdots+(\text{Im}a_{n-2})x^{n-2}
$$

이다. 이는 4.8에 의해 $\text{Im}a_0,\ldots,\text{Im}a_{n-2}$가 모두 $0$임을 함의한다. 따라서 $q$의 모든 계수는 실수이다. 이로써 원하는 인수분해가 존재함을 보였다.

이제 인수분해의 유일성을 살펴보자. $b_k^2<4c_k$인 꼴의 인수 $x^2+b_kx+c_k$는 어떤 $\lambda_k\in\mathbb{C}$에 대해

$$
(x-\lambda_k)(x-\overline{\lambda_k})
$$

꼴로 유일하게 쓸 수 있다. 잠시 생각해 보면, $p$를 $\mathcal{P}(\mathbb{R})$의 원소로 보는 두 가지 서로 다른 인수분해는 $p$를 $\mathcal{P}(\mathbb{C})$의 원소로 보는 두 가지 서로 다른 인수분해로 이어진다. 이는 4.13에 모순이다.

## 연습문제 4

1. $w,z\in\mathbb{C}$라고 하자. 다음 등식과 부등식을 확인하라.

   (a) $z+\overline{z}=2\text{Re}z$

   (b) $z-\overline{z}=2(\text{Im}z)i$

   (c) $z\overline{z}=|z|^2$

   (d) $\overline{w+z}=\overline{w}+\overline{z}$ 그리고 $\overline{wz}=\overline{w}\thinspace\overline{z}$

   (e) $\overline{\overline{z}}=z$

   (f) $|\text{Re}z|\le |z|$ 그리고 $|\text{Im}z|\le |z|$

   (g) $|\overline{z}|=|z|$

   (h) $|wz|=|w|\thinspace|z|$

   위 결과들은 독자에게 맡겨 두었던 4.4의 부분들이다.

2. $w,z\in\mathbb{C}$이면

   $$
   \bigl||w|-|z|\bigr|\le |w-z|
   $$

   임을 증명하라.

   위 부등식은 역삼각부등식이라고 불린다.

3. $V$가 복소 벡터공간이고 $\varphi\in V'$라고 하자. 각 $v\in V$에 대해

   $$
   \sigma(v)=\text{Re}\varphi(v)
   $$

   로 $\sigma:V\to\mathbb{R}$를 정의한다. 모든 $v\in V$에 대해

   $$
   \varphi(v)=\sigma(v)-i\sigma(iv)
   $$

   임을 보여라.

4. $m$이 양의 정수라고 하자. 집합

   $$
   \lbrace0\rbrace\cup\lbrace p\in\mathcal{P}(\mathbb{F}):\deg p=m\rbrace
   $$

   은 $\mathcal{P}(\mathbb{F})$의 부분공간인가?

5. 집합

   $$
   \lbrace0\rbrace\cup\lbrace p\in\mathcal{P}(\mathbb{F}):\deg p\text{는 짝수}\rbrace
   $$

   은 $\mathcal{P}(\mathbb{F})$의 부분공간인가?

6. $m$과 $n$이 $m\le n$인 양의 정수이고 $\lambda_1,\ldots,\lambda_m\in\mathbb{F}$라고 하자. $\deg p=n$이고

   $$
   0=p(\lambda_1)=\cdots=p(\lambda_m)
   $$

   이며 다른 영점은 가지지 않는 다항식 $p\in\mathcal{P}(\mathbb{F})$가 존재함을 증명하라.

7. $m$이 음이 아닌 정수이고 $z_1,\ldots,z_{m+1}$이 $\mathbb{F}$의 서로 다른 원소이며 $w_1,\ldots,w_{m+1}\in\mathbb{F}$라고 하자. 다음을 만족하는 유일한 다항식 $p\in\mathcal{P}_m(\mathbb{F})$가 존재함을 증명하라.

   $$
   p(z_k)=w_k
   $$

   각 $k=1,\ldots,m+1$에 대해.

   이 결과는 선형대수를 사용하지 않고도 증명할 수 있다. 그러나 선형대수를 조금 사용하는 더 명확하고 더 짧은 증명을 찾아보라.

8. $p\in\mathcal{P}(\mathbb{C})$의 차수가 $m$이라고 하자. $p$가 서로 다른 $m$개의 영점을 가질 필요충분조건은 $p$와 그 도함수 $p'$가 공통 영점을 가지지 않는 것임을 증명하라.

9. 실수 계수를 가지는 홀수 차수의 모든 다항식은 실수 영점을 가진다는 것을 증명하라.

10. $p\in\mathcal{P}(\mathbb{R})$에 대해 $Tp:\mathbb{R}\to\mathbb{R}$를 다음과 같이 정의한다.

    $$
    (Tp)(x)=
    \begin{cases}
    \dfrac{p(x)-p(3)}{x-3}, & x\ne 3,\cr
    p'(3), & x=3.
    \end{cases}
    $$

    각 $x\in\mathbb{R}$에 대해 위와 같이 정의한다. 모든 다항식 $p\in\mathcal{P}(\mathbb{R})$에 대해 $Tp\in\mathcal{P}(\mathbb{R})$임을 보이고, 또한 $T:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$가 선형사상임을 보여라.

11. $p\in\mathcal{P}(\mathbb{C})$라고 하자. $q:\mathbb{C}\to\mathbb{C}$를 다음과 같이 정의한다.

    $$
    q(z)=p(z)\overline{p(\overline{z})}.
    $$

    $q$가 실수 계수를 가지는 다항식임을 증명하라.

12. $m$이 음이 아닌 정수이고 $p\in\mathcal{P}_m(\mathbb{C})$라고 하자. 서로 다른 실수 $x_0,x_1,\ldots,x_m$이 존재하여 각 $k=0,1,\ldots,m$에 대해 $p(x_k)\in\mathbb{R}$라고 하자. 그러면 $p$의 모든 계수가 실수임을 증명하라.

13. $p\in\mathcal{P}(\mathbb{F})$이고 $p\ne 0$이라고 하자. $U=\lbrace pq:q\in\mathcal{P}(\mathbb{F})\rbrace$라고 하자.

    (a) $\dim\mathcal{P}(\mathbb{F})/U=\deg p$임을 보여라.

    (b) $\mathcal{P}(\mathbb{F})/U$의 기저를 찾아라.

14. $p,q\in\mathcal{P}(\mathbb{C})$가 공통 영점을 가지지 않는 상수가 아닌 다항식이라고 하자. $m=\deg p$이고 $n=\deg q$라고 하자. 아래 (a)-(c)에 제시된 선형대수적 방법을 사용하여

    $$
    rp+sq=1
    $$

    을 만족하는 $r\in\mathcal{P}_{n-1}(\mathbb{C})$와 $s\in\mathcal{P}_{m-1}(\mathbb{C})$가 존재함을 증명하라.

    (a) $T:\mathcal{P}_{n-1}(\mathbb{C})\times\mathcal{P}_{m-1}(\mathbb{C})\to\mathcal{P}_{m+n-1}(\mathbb{C})$를

    $$
    T(r,s)=rp+sq
    $$

    로 정의한다. 선형사상 $T$가 단사임을 보여라.

    (b) (a)의 선형사상 $T$가 전사임을 보여라.

    (c) (b)를 사용하여 $rp+sq=1$을 만족하는 $r\in\mathcal{P}_{n-1}(\mathbb{C})$와 $s\in\mathcal{P}_{m-1}(\mathbb{C})$가 존재한다고 결론 내려라.
