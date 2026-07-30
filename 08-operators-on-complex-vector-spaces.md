# 8장 복소 벡터공간 위의 연산자

이 장에서는 연산자의 구조를 더 깊이 살펴본다. 대부분의 관심은 복소 벡터공간에 놓인다. 이 장의 일부 결과는 실 벡터공간과 복소 벡터공간 모두에 적용되므로, $\mathbb{F}=\mathbb{C}$라는 가정을 항상 두지는 않는다. 또한 여기서 다루는 내용에는 내적이 별로 도움이 되지 않으므로, 다시 유한차원 벡터공간이라는 일반적인 상황으로 돌아간다.

유한차원 복소 벡터공간 위에서도 어떤 연산자는 벡터공간의 기저를 이룰 만큼 충분한 고유벡터를 가지지 않을 수 있다. 그래서 우리는 고유벡터와 밀접하게 관련된 **일반화 고유벡터**를 고려할 것이다. 유한차원 복소 벡터공간 위의 모든 연산자에 대해, 그 연산자의 일반화 고유벡터들로 이루어진 기저가 존재함을 보게 된다. 일반화 고유공간 분해는 유한차원 복소 벡터공간 위의 임의의 연산자를 잘 기술해 준다.

어떤 거듭제곱이 $0$이 되는 연산자인 **멱영 연산자**는 이러한 연구에서 중요한 역할을 한다. 멱영 연산자는 유한차원 복소 벡터공간 위의 모든 가역 연산자가 제곱근을 가진다는 사실의 증명과 조르당 형식에 대한 접근에서 핵심 도구가 된다.

이 장은 트레이스를 정의하고 그 핵심 성질을 증명하며 끝난다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.
- $V$는 $\mathbb{F}$ 위의 유한차원 비영 벡터공간이다.

그림: 더블린 대학교 올드 라이브러리의 롱 룸. 윌리엄 해밀턴(1805-1865)은 이곳에서 학생이었고 이후 교수로 재직했다. 해밀턴은 1853년에 오늘날 케일리-해밀턴 정리라고 부르는 결과의 특수한 경우를 증명했다.

## 8A 일반화 고유벡터와 멱영 연산자

### 연산자의 거듭제곱의 영공간

이 장은 연산자의 거듭제곱들의 영공간을 연구하며 시작한다.

**8.1 증가하는 영공간의 열**

$T\in\mathcal{L}(V)$라고 하자. 그러면

$$
\{0\}=\text{null}T^0
\subset \text{null}T^1
\subset \cdots
\subset \text{null}T^k
\subset \text{null}T^{k+1}
\subset \cdots.
$$

**증명**

$k$가 음이 아닌 정수이고 $v\in\text{null}T^k$라고 하자. 그러면 $T^kv=0$이고, 따라서

$$
T^{k+1}v=T(T^kv)=T(0)=0.
$$

그러므로 $v\in\text{null}T^{k+1}$이다.

**8.2 영공간의 열에서 한 번 같아지면 계속 같다**

$T\in\mathcal{L}(V)$이고 $m$이 음이 아닌 정수이며

$$
\text{null}T^m=\text{null}T^{m+1}
$$

이라고 하자. 그러면

$$
\text{null}T^m
=\text{null}T^{m+1}
=\text{null}T^{m+2}
=\text{null}T^{m+3}
=\cdots.
$$

**증명**

$k$를 양의 정수라고 하자. $\text{null}T^{m+k}=\text{null}T^{m+k+1}$임을 보이면 된다. 8.1에 의해 왼쪽이 오른쪽에 포함됨은 이미 안다.

반대 포함을 보이자. $v\in\text{null}T^{m+k+1}$라고 하자. 그러면

$$
T^{m+1}(T^kv)=T^{m+k+1}v=0.
$$

따라서

$$
T^kv\in\text{null}T^{m+1}
=\text{null}T^m.
$$

그러므로 $T^{m+k}v=T^m(T^kv)=0$이고, $v\in\text{null}T^{m+k}$이다.

**8.3 영공간은 더 이상 커지지 않는다**

$T\in\mathcal{L}(V)$라고 하자. 그러면

$$
\text{null}T^{\dim V}
=\text{null}T^{\dim V+1}
=\text{null}T^{\dim V+2}
=\cdots.
$$

**증명**

8.2에 의해 $\text{null}T^{\dim V}=\text{null}T^{\dim V+1}$만 보이면 된다. 그렇지 않다고 하자. 그러면 8.1과 8.2에 의해

$$
\{0\}=\text{null}T^0
\subsetneqq \text{null}T^1
\subsetneqq \cdots
\subsetneqq \text{null}T^{\dim V}
\subsetneqq \text{null}T^{\dim V+1}
$$

이 된다. 각 진포함마다 차원이 적어도 $1$씩 증가하므로

$$
\dim\text{null}T^{\dim V+1}\ge \dim V+1
$$

이다. 이는 $V$의 부분공간이 $V$보다 큰 차원을 가질 수 없다는 사실에 모순이다.

**8.4 $V$는 $\text{null}T^{\dim V}$와 $\text{range}T^{\dim V}$의 직합이다**

$T\in\mathcal{L}(V)$라고 하자. 그러면

$$
V=\text{null}T^{\dim V}\oplus\text{range}T^{\dim V}.
$$

**증명**

$n=\dim V$라고 하자. 먼저

$$
\text{null}T^n\cap\text{range}T^n=\{0\}
\tag{8.5}
$$

임을 보이자. $v\in\text{null}T^n\cap\text{range}T^n$라고 하자. 그러면 $T^nv=0$이고, 어떤 $u\in V$가 존재하여 $v=T^nu$이다. 따라서

$$
T^{2n}u=T^nv=0.
$$

8.3에 의해 $T^nu=0$이고, 따라서 $v=T^nu=0$이다. 그러므로 (8.5)가 성립한다.

이제 (8.5)에 의해 $\text{null}T^n+\text{range}T^n$은 직합이다. 또한 기본정리(3.21)에 의해

$$
\dim(\text{null}T^n\oplus\text{range}T^n)
=\dim\text{null}T^n+\dim\text{range}T^n
=\dim V.
$$

따라서 이 직합은 $V$ 전체이다.

**8.6 예: $T\in\mathcal{L}(\mathbb{F}^3)$에 대해 $\mathbb{F}^3=\text{null}T^3\oplus\text{range}T^3$**

$T\in\mathcal{L}(\mathbb{F}^3)$를

$$
T(z_1,z_2,z_3)=(4z_2,0,5z_3)
$$

로 정의하자. 그러면

$$
\text{null}T=\{(z_1,0,0):z_1\in\mathbb{F}\}
$$

이고

$$
\text{range}T=\{(z_1,0,z_3):z_1,z_3\in\mathbb{F}\}.
$$

따라서 $\text{null}T\cap\text{range}T\ne\{0\}$이고, $\text{null}T+\text{range}T$는 직합이 아니다. 또한 $\text{null}T+\text{range}T\ne\mathbb{F}^3$이다.

그러나

$$
T^3(z_1,z_2,z_3)=(0,0,125z_3)
$$

이므로

$$
\text{null}T^3=\{(z_1,z_2,0):z_1,z_2\in\mathbb{F}\},
\qquad
\text{range}T^3=\{(0,0,z_3):z_3\in\mathbb{F}\}.
$$

따라서 8.4가 예측하듯이

$$
\mathbb{F}^3=\text{null}T^3\oplus\text{range}T^3.
$$

### 일반화 고유벡터

어떤 연산자들은 그 작용을 잘 설명할 만큼 충분한 고유벡터를 가지지 않는다. 그래서 우리는 일반화 고유벡터라는 개념을 도입한다.

$T\in\mathcal{L}(V)$를 고정하자. 우리는 $T$에 대해 불변인 부분공간들로

$$
V=V_1\oplus\cdots\oplus V_n
$$

처럼 $V$를 분해하여 $T$를 설명하고 싶다. 가장 단순한 비영 불변 부분공간은 $1$차원 부분공간이다. 위 분해에서 각 $V_k$가 $T$에 대해 불변인 $1$차원 부분공간이 되는 것은, $V$가 $T$의 고유벡터들로 이루어진 기저를 가지는 것과 동치이다. 이는 다시, $T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라고 할 때

$$
V=E(\lambda_1,T)\oplus\cdots\oplus E(\lambda_m,T)
\tag{8.7}
$$

라는 고유공간 분해가 존재하는 것과 동치이다.

그러나 복소 벡터공간에서도 일반적인 연산자에 대해서는 (8.7) 꼴의 분해가 성립하지 않을 수 있다. 일반화 고유벡터와 일반화 고유공간은 이 문제를 해결해 준다.

**8.8 정의: 일반화 고유벡터**

$T\in\mathcal{L}(V)$이고 $\lambda$가 $T$의 고윳값이라고 하자. 벡터 $v\in V$가 $v\ne 0$이고 어떤 양의 정수 $k$에 대해

$$
(T-\lambda I)^kv=0
$$

를 만족하면, $v$를 $\lambda$에 대응하는 $T$의 **일반화 고유벡터**라고 한다.

일반화 고윳값이라는 말은 정의하지 않는다. 새로 얻어지는 것이 없기 때문이다. 실제로 어떤 양의 정수 $k$에 대해 $(T-\lambda I)^k$가 단사가 아니면, $T-\lambda I$도 단사가 아니므로 $\lambda$는 $T$의 고윳값이다.

영이 아닌 벡터 $v\in V$가 $\lambda$에 대응하는 $T$의 일반화 고유벡터인 것은

$$
(T-\lambda I)^{\dim V}v=0
$$

인 것과 동치이다. 이는 8.1과 8.3을 $T-\lambda I$에 적용하면 나온다.

**8.9 일반화 고유벡터들로 이루어진 기저**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $V$는 $T$의 일반화 고유벡터들로 이루어진 기저를 가진다.

**증명**

$n=\dim V$라고 하자. $n$에 대한 귀납법을 사용한다. $n=1$이면 $V$의 모든 영이 아닌 벡터가 $T$의 고유벡터이므로 결론이 성립한다.

$n>1$이고 더 작은 차원에서는 결론이 성립한다고 하자. 복소 벡터공간이므로 $T$는 어떤 고윳값 $\lambda$를 가진다. 8.4를 $T-\lambda I$에 적용하면

$$
V=\text{null}(T-\lambda I)^n
\oplus
\text{range}(T-\lambda I)^n.
$$

$\text{null}(T-\lambda I)^n=V$이면 $V$의 모든 영이 아닌 벡터가 $T$의 일반화 고유벡터이므로 결론이 성립한다. 이제 그렇지 않다고 하자. $\lambda$가 고윳값이므로 $\text{null}(T-\lambda I)^n\ne\{0\}$이고, 따라서

$$
0<\dim\text{range}(T-\lambda I)^n<n.
$$

또한 $\text{range}(T-\lambda I)^n$은 $T$에 대해 불변이다. $S$를 이 부분공간에 대한 $T$의 제한이라고 하자. 귀납가정에 의해 $\text{range}(T-\lambda I)^n$은 $S$의 일반화 고유벡터들로 이루어진 기저를 가진다. 이 벡터들은 $T$의 일반화 고유벡터이기도 하다. 이 기저에 $\text{null}(T-\lambda I)^n$의 임의의 기저를 붙이면 $V$의 일반화 고유벡터들로 이루어진 기저를 얻는다.

**8.10 예: $\mathbb{C}^3$ 위의 연산자의 일반화 고유벡터**

$T\in\mathcal{L}(\mathbb{C}^3)$를

$$
T(z_1,z_2,z_3)=(4z_2,0,5z_3)
$$

로 정의하자. $T$의 고윳값은 $0$과 $5$이다. 고윳값 $0$에 대응하는 고유벡터는 $(z_1,0,0)$ 꼴의 영이 아닌 벡터이고, 고윳값 $5$에 대응하는 고유벡터는 $(0,0,z_3)$ 꼴의 영이 아닌 벡터이다. 따라서 이 연산자는 $\mathbb{C}^3$을 생성할 만큼 충분한 고유벡터를 가지지 않는다.

계산하면

$$
T^3(z_1,z_2,z_3)=(0,0,125z_3)
$$

이다. 따라서 고윳값 $0$에 대응하는 $T$의 일반화 고유벡터는 $(z_1,z_2,0)$ 꼴의 영이 아닌 벡터들이다.

또한

$$
(T-5I)^3(z_1,z_2,z_3)=(-125z_1+300z_2,-125z_2,0).
$$

따라서 고윳값 $5$에 대응하는 $T$의 일반화 고유벡터는 $(0,0,z_3)$ 꼴의 영이 아닌 벡터들이다.

그러므로 $\mathbb{C}^3$의 표준기저의 각 벡터는 $T$의 일반화 고유벡터이다. 이는 8.9가 약속한 것처럼 $T$의 일반화 고유벡터들로 이루어진 기저가 존재함을 보여 준다.

**8.11 일반화 고유벡터는 유일한 고윳값에 대응한다**

$T\in\mathcal{L}(V)$라고 하자. 그러면 $T$의 각 일반화 고유벡터는 $T$의 오직 하나의 고윳값에만 대응한다.

**증명**

$v\in V$가 $T$의 일반화 고유벡터이고 고윳값 $\alpha$와 $\lambda$ 모두에 대응한다고 하자. $(T-\alpha I)^mv=0$이 되는 가장 작은 양의 정수를 $m$이라고 하자. $n=\dim V$라고 하자. 그러면

$$
\begin{aligned}
0
&=(T-\lambda I)^nv\\
&=((T-\alpha I)+(\alpha-\lambda)I)^nv\\
&=\sum_{k=0}^n b_k(\alpha-\lambda)^{n-k}(T-\alpha I)^kv
\end{aligned}
$$

이다. 여기서 $b_0=1$이고 나머지 이항계수들의 구체적인 값은 중요하지 않다. 위 등식의 양변에 $(T-\alpha I)^{m-1}$를 적용하면

$$
0=(\alpha-\lambda)^n(T-\alpha I)^{m-1}v.
$$

$(T-\alpha I)^{m-1}v\ne 0$이므로 $\alpha=\lambda$이다.

**8.12 서로 다른 고윳값에 대응하는 일반화 고유벡터들은 일차독립이다**

$T\in\mathcal{L}(V)$라고 하자. 그러면 $T$의 서로 다른 고윳값에 대응하는 일반화 고유벡터들의 모든 리스트는 일차독립이다.

**증명**

결론이 거짓이라고 하자. 그러면 어떤 가장 작은 양의 정수 $m$에 대해, 서로 다른 고윳값 $\lambda_1,\ldots,\lambda_m$에 대응하는 일반화 고유벡터들의 일차종속 리스트 $v_1,\ldots,v_m$이 존재한다. $m$의 최소성 때문에 $a_1,\ldots,a_m$은 모두 $0$이 아니고

$$
a_1v_1+\cdots+a_mv_m=0
$$

을 만족한다고 할 수 있다. $n=\dim V$라고 하자. 위 등식의 양변에 $(T-\lambda_m I)^n$을 적용하면

$$
a_1(T-\lambda_m I)^nv_1+\cdots+
a_{m-1}(T-\lambda_m I)^nv_{m-1}=0.
\tag{8.13}
$$

$k\in\{1,\ldots,m-1\}$이면 $(T-\lambda_m I)^nv_k\ne 0$이다. 그렇지 않으면 $v_k$가 서로 다른 두 고윳값 $\lambda_k,\lambda_m$에 모두 대응하는 일반화 고유벡터가 되어 8.11에 모순이다. 또한

$$
(T-\lambda_k I)^n((T-\lambda_m I)^nv_k)
=(T-\lambda_m I)^n((T-\lambda_k I)^nv_k)=0.
$$

따라서 $(T-\lambda_m I)^nv_k$는 $\lambda_k$에 대응하는 일반화 고유벡터이다. 그러므로 (8.13)은 $m-1$개의 서로 다른 고윳값에 대응하는 일반화 고유벡터들의 일차종속 리스트를 준다. 이는 $m$의 최소성에 모순이다.

### 멱영 연산자

**8.14 정의: 멱영**

연산자의 어떤 거듭제곱이 $0$이면 그 연산자를 **멱영**이라고 한다.

즉 $T\in\mathcal{L}(V)$가 멱영인 것은 $V$의 모든 영이 아닌 벡터가 고윳값 $0$에 대응하는 $T$의 일반화 고유벡터인 것과 동치이다.

**8.15 예: 멱영 연산자**

(a) $T\in\mathcal{L}(\mathbb{F}^4)$를

$$
T(z_1,z_2,z_3,z_4)=(0,0,z_1,z_2)
$$

로 정의하면 $T^2=0$이므로 $T$는 멱영이다.

(b) 표준기저에 대한 행렬이

$$
\begin{pmatrix}
-3 & 9 & 0\\
-7 & 9 & 6\\
4 & 0 & -6
\end{pmatrix}
$$

인 $\mathbb{F}^3$ 위의 연산자는 위 행렬의 세제곱이 영행렬이므로 멱영이다.

(c) $\mathcal{P}_m(\mathbb{R})$ 위의 미분 연산자는 멱영이다. 차수가 최대 $m$인 모든 다항식의 $(m+1)$번째 도함수가 $0$이기 때문이다.

**8.16 멱영 연산자를 정의역의 차수만큼 거듭제곱하면 $0$이다**

$T\in\mathcal{L}(V)$가 멱영이라고 하자. 그러면

$$
T^{\dim V}=0.
$$

**증명**

$T$가 멱영이므로 어떤 양의 정수 $k$에 대해 $T^k=0$이다. 따라서 $\text{null}T^k=V$이다. 8.1과 8.3에 의해 $\text{null}T^{\dim V}=V$이고, 따라서 $T^{\dim V}=0$이다.

**8.17 멱영 연산자의 고윳값**

$T\in\mathcal{L}(V)$라고 하자.

(a) $T$가 멱영이면 $0$은 $T$의 고윳값이고, $T$는 다른 고윳값을 가지지 않는다.

(b) $\mathbb{F}=\mathbb{C}$이고 $0$이 $T$의 유일한 고윳값이면 $T$는 멱영이다.

**증명**

(a) $T$가 멱영이면 어떤 양의 정수 $m$에 대해 $T^m=0$이다. 따라서 $T$는 단사가 아니므로 $0$은 $T$의 고윳값이다.

이제 $\lambda$가 $T$의 고윳값이고 $Tv=\lambda v$인 $v\ne 0$가 있다고 하자. $T$를 반복해서 적용하면

$$
\lambda^m v=T^mv=0.
$$

따라서 $\lambda=0$이다.

(b) $\mathbb{F}=\mathbb{C}$이고 $0$이 $T$의 유일한 고윳값이라고 하자. 5.27(b)에 의해 $T$의 최소다항식은 어떤 양의 정수 $m$에 대해 $z^m$이다. 따라서 $T^m=0$이고, $T$는 멱영이다.

**8.18 멱영 연산자의 최소다항식과 상삼각 행렬**

$T\in\mathcal{L}(V)$라고 하자. 그러면 다음 조건들은 서로 동치이다.

(a) $T$는 멱영이다.

(b) $T$의 최소다항식은 어떤 양의 정수 $m$에 대해 $z^m$이다.

(c) 어떤 $V$의 기저에 대해 $T$의 행렬은 대각선 위와 그 아래의 모든 성분이 $0$인 다음 꼴이다.

$$
\begin{pmatrix}
0 & *\\
& \ddots\\
0 & 0
\end{pmatrix}
$$

**증명**

(a)가 성립한다고 하자. 그러면 어떤 양의 정수 $n$에 대해 $T^n=0$이다. 5.29에 의해 $z^n$은 $T$의 최소다항식의 다항식배이다. 따라서 최소다항식은 $z^m$ 꼴이다.

(b)가 성립한다고 하자. 최소다항식의 유일한 영점은 $0$이다. 5.44에 의해 어떤 기저에 대해 $T$의 행렬은 상삼각이고, 5.41에 의해 그 대각성분들은 모두 $0$이다. 따라서 (c)가 성립한다.

(c)가 성립하면 5.40에 의해 $T^{\dim V}=0$이다. 따라서 $T$는 멱영이다.

### 연습문제 8A

1. $T\in\mathcal{L}(V)$라고 하자. $\dim\text{null}T^4=8$이고 $\dim\text{null}T^6=9$이면 모든 정수 $m\ge 5$에 대해 $\dim\text{null}T^m=9$임을 증명하여라.

2. $T\in\mathcal{L}(V)$, $m$이 양의 정수, $v\in V$이고 $T^{m-1}v\ne 0$이지만 $T^mv=0$이라고 하자. 리스트

   $$
   v,Tv,T^2v,\ldots,T^{m-1}v
   $$

    가 일차독립임을 증명하여라.

3. $T\in\mathcal{L}(V)$라고 하자. 다음을 증명하여라.

   $$
   V=\text{null}T\oplus\text{range}T
   \Longleftrightarrow
   \text{null}T^2=\text{null}T.
   $$

4. $T\in\mathcal{L}(V)$, $\lambda\in\mathbb{F}$이고 $m$이 양의 정수라고 하자. $T$의 최소다항식이 $(z-\lambda)^m$의 다항식배이면

   $$
   \dim\text{null}(T-\lambda I)^m\ge m
   $$

    임을 증명하여라.

5. $T\in\mathcal{L}(V)$이고 $m$이 양의 정수라고 하자. 다음을 증명하여라.

   $$
   \dim\text{null}T^m\le m\dim\text{null}T.
   $$

6. $T\in\mathcal{L}(V)$라고 하자. 다음을 보여라.

   $$
   V=\text{range}T^0
   \supset \text{range}T^1
   \supset \cdots
   \supset \text{range}T^k
   \supset \text{range}T^{k+1}
   \supset \cdots.
   $$

7. $T\in\mathcal{L}(V)$이고 $m$이 음이 아닌 정수이며

   $$
   \text{range}T^m=\text{range}T^{m+1}
   $$

   이라고 하자. 모든 $k>m$에 대해 $\text{range}T^k=\text{range}T^m$임을 증명하여라.

8. $T\in\mathcal{L}(V)$라고 하자. 다음을 증명하여라.

   $$
   \text{range}T^{\dim V}
   =\text{range}T^{\dim V+1}
   =\text{range}T^{\dim V+2}
   =\cdots.
   $$

9. $T\in\mathcal{L}(V)$이고 $m$이 음이 아닌 정수라고 하자. 다음을 증명하여라.

   $$
   \text{null}T^m=\text{null}T^{m+1}
   \Longleftrightarrow
   \text{range}T^m=\text{range}T^{m+1}.
   $$

10. $T\in\mathcal{L}(\mathbb{C}^2)$를 $T(w,z)=(z,0)$으로 정의한다. $T$의 모든 일반화 고유벡터를 구하여라.

11. $T\in\mathcal{L}(V)$라고 하자. $V$가 $T$의 일반화 고유벡터들로 이루어진 기저를 가지는 것과, $T$의 최소다항식이 어떤 $\lambda_1,\ldots,\lambda_m\in\mathbb{F}$에 대해

    $$
    (z-\lambda_1)\cdots(z-\lambda_m)
    $$

    꼴의 다항식배로 완전히 분해되는 것은 동치임을 증명하여라. $\mathbb{F}=\mathbb{C}$인 경우는 5.27(b)와 8.9에서 따르므로, $\mathbb{F}=\mathbb{R}$인 경우를 생각하여라.

12. $T\in\mathcal{L}(V)$가 $V$의 모든 영이 아닌 벡터를 $T$의 일반화 고유벡터로 만든다고 하자. 어떤 $\lambda\in\mathbb{F}$가 존재하여 $T-\lambda I$가 멱영임을 증명하여라.

13. $S,T\in\mathcal{L}(V)$이고 $ST$가 멱영이라고 하자. $TS$도 멱영임을 증명하여라.

14. $T\in\mathcal{L}(V)$가 멱영이고 $T\ne 0$이라고 하자. $T$는 대각화가능이 아님을 증명하여라.

15. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$가 대각화가능인 것과 $T$의 모든 일반화 고유벡터가 $T$의 고유벡터인 것은 동치임을 증명하여라.

16. (a) 같은 벡터공간 위의 멱영 연산자 $S,T$ 중에서 $S+T$도 $ST$도 멱영이 아닌 예를 제시하여라.

    (b) $S,T\in\mathcal{L}(V)$가 멱영이고 $ST=TS$라고 하자. $S+T$와 $ST$가 멱영임을 증명하여라.

17. $T\in\mathcal{L}(V)$가 멱영이고 $m$이 양의 정수이며 $T^m=0$이라고 하자.

    (a) $I-T$가 가역이고

    $$
    (I-T)^{-1}=I+T+\cdots+T^{m-1}
    $$

    임을 증명하여라.

    (b) 위 공식을 어떻게 추측할 수 있는지 설명하여라.

18. $T\in\mathcal{L}(V)$가 멱영이라고 하자. 다음을 증명하여라.

    $$
    T^{1+\dim\text{range}T}=0.
    $$

19. $T\in\mathcal{L}(V)$가 멱영이 아니라고 하자. 다음을 보여라.

    $$
    V=\text{null}T^{\dim V-1}
    \oplus
    \text{range}T^{\dim V-1}.
    $$

20. $V$가 내적공간이고 $T\in\mathcal{L}(V)$가 정규이면서 멱영이라고 하자. $T=0$임을 증명하여라.

21. $T\in\mathcal{L}(V)$가

    $$
    \text{null}T^{\dim V-1}\ne\text{null}T^{\dim V}
    $$

    를 만족한다고 하자. $T$가 멱영이고, $0\le k\le\dim V$인 모든 정수 $k$에 대해 $\dim\text{null}T^k=k$임을 증명하여라.

22. $T\in\mathcal{L}(\mathbb{C}^5)$가 $\text{range}T^4\ne\text{range}T^5$를 만족한다고 하자. $T$가 멱영임을 증명하여라.

23. 유한차원 실 벡터공간 위의 연산자 $T$ 중에서 $0$이 유일한 고윳값이지만 $T$가 멱영은 아닌 예를 제시하여라.

24. 예 8.15의 각 항목에 대해, 그 멱영 연산자의 행렬이 8.18(c)가 약속한 상삼각 꼴이 되게 하는 정의역 벡터공간의 기저를 찾아라.

25. $V$가 내적공간이고 $T\in\mathcal{L}(V)$가 멱영이라고 하자. $T$의 행렬이 8.18(c)가 약속한 상삼각 꼴이 되게 하는 $V$의 정규직교기저가 존재함을 보여라.

## 8B 일반화 고유공간 분해

### 일반화 고유공간

**8.19 정의: 일반화 고유공간, $G(\lambda,T)$**

$T\in\mathcal{L}(V)$이고 $\lambda\in\mathbb{F}$라고 하자. $\lambda$에 대응하는 $T$의 **일반화 고유공간** $G(\lambda,T)$는

$$
G(\lambda,T)=\{v\in V:(T-\lambda I)^kv=0\text{인 양의 정수 }k\text{가 존재한다}\}
$$

로 정의된다.

따라서 $G(\lambda,T)$는 $\lambda$에 대응하는 $T$의 일반화 고유벡터들의 집합에 영벡터를 더한 것이다. 모든 고유벡터는 일반화 고유벡터이므로

$$
E(\lambda,T)\subset G(\lambda,T)
$$

이다.

**8.20 일반화 고유공간의 기술**

$T\in\mathcal{L}(V)$이고 $\lambda\in\mathbb{F}$라고 하자. 그러면

$$
G(\lambda,T)=\text{null}(T-\lambda I)^{\dim V}.
$$

**증명**

$v\in\text{null}(T-\lambda I)^{\dim V}$이면 정의상 $v\in G(\lambda,T)$이다. 반대로 $v\in G(\lambda,T)$이면 어떤 양의 정수 $k$에 대해 $v\in\text{null}(T-\lambda I)^k$이다. 8.1과 8.3을 $T-\lambda I$에 적용하면 $v\in\text{null}(T-\lambda I)^{\dim V}$이다.

**8.21 예: $\mathbb{C}^3$ 위의 연산자의 일반화 고유공간**

$T\in\mathcal{L}(\mathbb{C}^3)$를

$$
T(z_1,z_2,z_3)=(4z_2,0,5z_3)
$$

로 정의하자. 예 8.10에서 $T$의 고윳값은 $0$과 $5$임을 보았고, 대응하는 일반화 고유벡터들의 집합도 구했다. 여기에 $\{0\}$을 더하면

$$
G(0,T)=\{(z_1,z_2,0):z_1,z_2\in\mathbb{C}\}
$$

이고

$$
G(5,T)=\{(0,0,z_3):z_3\in\mathbb{C}\}.
$$

따라서

$$
\mathbb{C}^3=G(0,T)\oplus G(5,T).
$$

**8.22 일반화 고유공간 분해**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $\lambda_1,\ldots,\lambda_m$을 $T$의 서로 다른 고윳값들이라고 하자. 그러면 다음이 성립한다.

(a) 각 $k=1,\ldots,m$에 대해 $G(\lambda_k,T)$는 $T$에 대해 불변이다.

(b) 각 $k=1,\ldots,m$에 대해

$$
(T-\lambda_k I)|_{G(\lambda_k,T)}
$$

는 멱영이다.

(c)

$$
V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T).
$$

**증명**

(a) 8.20에 의해

$$
G(\lambda_k,T)=\text{null}(T-\lambda_k I)^{\dim V}.
$$

따라서 5.18을 $p(z)=(z-\lambda_k)^{\dim V}$에 적용하면 $G(\lambda_k,T)$가 $T$에 대해 불변임을 얻는다.

(b) $v\in G(\lambda_k,T)$이면 8.20에 의해 $(T-\lambda_k I)^{\dim V}v=0$이다. 따라서 제한 연산자 $(T-\lambda_k I)|_{G(\lambda_k,T)}$는 멱영이다.

(c) 먼저 $v_1+\cdots+v_m=0$이고 각 $v_k\in G(\lambda_k,T)$라고 하자. 영이 아닌 $v_k$들이 있다면 이들은 서로 다른 고윳값에 대응하는 일반화 고유벡터들이므로 8.12에 의해 일차독립이어야 한다. 따라서 각 $v_k=0$이다. 그러므로 합은 직합이다.

마지막으로 8.9에 의해 $V$의 모든 벡터는 $T$의 일반화 고유벡터들의 유한합으로 쓸 수 있다. 따라서 위 직합은 $V$ 전체이다.

### 고윳값의 중복도

**8.23 정의: 고윳값의 중복도**

$T\in\mathcal{L}(V)$이고 $\lambda$가 $T$의 고윳값이라고 하자. $\lambda$에 대응하는 $T$의 **중복도**는

$$
\dim G(\lambda,T)
$$

로 정의한다.

동치적으로, $\lambda$의 중복도는

$$
\dim\text{null}(T-\lambda I)^{\dim V}
$$

이다.

**8.24 예: $\mathbb{C}^3$ 위의 연산자의 고윳값 중복도**

$T\in\mathcal{L}(\mathbb{C}^3)$를

$$
T(z_1,z_2,z_3)=(6z_1+3z_2+4z_3,\;6z_2+2z_3,\;7z_3)
$$

로 정의하자. $T$의 표준 기저에 대한 행렬은

$$
\begin{pmatrix}
6&3&4\\
0&6&2\\
0&0&7
\end{pmatrix}
$$

이다. 따라서 $T$의 고윳값은 $6$과 $7$이다.

계산하면

$$
G(6,T)=\text{span}\bigl((1,0,0),(0,1,0)\bigr)
$$

이고

$$
G(7,T)=\text{span}\bigl((10,2,1)\bigr)
$$

이다. 그러므로 $6$의 중복도는 $2$이고 $7$의 중복도는 $1$이다. 또한

$$
\mathbb{C}^3=G(6,T)\oplus G(7,T)
$$

이며, $(1,0,0),(0,1,0),(10,2,1)$은 $T$의 일반화 고유벡터들로 이루어진 기저이다. 그러나 이 예에서 $T$는 고유벡터들로 이루어진 기저를 가지지 않는다.

**8.25 중복도의 합은 $\dim V$와 같다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$의 모든 고윳값의 중복도의 합은 $\dim V$와 같다.

**증명**

$\lambda_1,\ldots,\lambda_m$을 $T$의 서로 다른 고윳값들이라고 하자. 8.22에 의해

$$
V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T).
$$

따라서

$$
\dim V=\dim G(\lambda_1,T)+\cdots+\dim G(\lambda_m,T),
$$

이고 오른쪽은 바로 고윳값들의 중복도의 합이다.

$T$의 고윳값 $\lambda$의 **대수적 중복도**는 보통 특성다항식에서 $z-\lambda$의 지수로 정의된다. 여기서는 그것이 $\dim G(\lambda,T)$와 같다는 사실을 8.31에서 보일 것이다. $\lambda$의 **기하적 중복도**는

$$
\dim\text{null}(T-\lambda I)
$$

이다. 즉 고유공간의 차원이다. 일반적으로 기하적 중복도는 대수적 중복도보다 작거나 같다.

**8.26 정의: 특성다항식**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라 하고, 각 $\lambda_k$의 중복도를 $d_k$라고 하자. $T$의 **특성다항식**은

$$
(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}
$$

으로 정의된다.

**8.27 예: 특성다항식**

8.24의 연산자의 특성다항식은

$$
(z-6)^2(z-7)
$$

이다.

**8.28 특성다항식의 차수와 영점**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$의 특성다항식의 차수는 $\dim V$이고, 그 영점들은 정확히 $T$의 고윳값들이다.

**8.29 케일리-해밀턴 정리**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $q$가 $T$의 특성다항식이면

$$
q(T)=0.
$$

**증명**

$T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라 하고, 각 $\lambda_k$의 중복도를 $d_k$라고 하자. 그러면

$$
q(z)=(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}.
$$

8.22에 의해 $V$는 일반화 고유공간들의 직합이다. 각 $G(\lambda_k,T)$ 위에서

$$
(T-\lambda_k I)|_{G(\lambda_k,T)}
$$

는 멱영이다. 또한 $\dim G(\lambda_k,T)=d_k$이므로 8.16에 의해

$$
(T-\lambda_k I)^{d_k}v=0
$$

가 모든 $v\in G(\lambda_k,T)$에 대해 성립한다. 다항식으로 얻어지는 연산자들은 서로 가환하므로, $q(T)$는 각 일반화 고유공간 위에서 $0$이다. 따라서 $q(T)=0$이다.

**8.30 특성다항식은 최소다항식의 다항식배이다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$의 특성다항식은 $T$의 최소다항식의 다항식배이다.

**증명**

8.29에 의해 특성다항식 $q$는 $q(T)=0$을 만족한다. 따라서 5.29에 의해 $q$는 최소다항식의 다항식배이다.

**8.31 중복도는 상삼각 행렬의 대각선에 나타나는 횟수와 같다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$의 어떤 기저에 대한 행렬이 상삼각 행렬이라고 하자. 그러면 $T$의 각 고윳값이 이 행렬의 대각선에 나타나는 횟수는 그 고윳값의 중복도와 같다.

**증명**

$v_1,\ldots,v_n$을 $T$의 행렬이 상삼각 행렬이 되는 기저라고 하자. 그 대각선 성분을 $\lambda_1,\ldots,\lambda_n$이라 쓰자.

먼저 대각선 성분 가운데 $0$이 나타나는 횟수를 $d$라고 하자. $\lambda_k\ne 0$이면 $Tv_k$는 $Tv_1,\ldots,Tv_{k-1}$의 일차결합이 될 수 없다. 따라서 $0$이 아닌 대각선 성분에 대응하는 $Tv_k$들은 일차독립이고,

$$
\dim\text{range}T\ge n-d.
$$

그러므로

$$
\dim\text{null}T\le d.
\tag{8.32}
$$

같은 논리를 $T^n$에 적용하면

$$
\dim\text{null}T^n\le d.
\tag{8.33}
$$

이제 임의의 고윳값 $\lambda$에 대해 $T-\lambda I$를 생각하자. $\lambda$의 중복도를 $m_\lambda$라 하고, 원래 상삼각 행렬의 대각선에서 $\lambda$가 나타나는 횟수를 $d_\lambda$라 하자. 위 결과를 $T-\lambda I$에 적용하면

$$
\dim\text{null}(T-\lambda I)^n
=m_\lambda\le d_\lambda
\tag{8.34}
$$

이다.

모든 고윳값의 중복도의 합은 8.25에 의해 $n$이고, 대각선에 나타나는 고윳값들의 총개수도 $n$이다. 따라서 각 고윳값에 대해 두 수가 같아야 한다.

### 블록 대각행렬

**8.35 정의: 블록 대각행렬**

정사각행렬이 몇 개의 정사각행렬 $A_1,\ldots,A_m$을 대각선 블록으로 가지고, 그 밖의 위치는 모두 $0$이면 그 행렬을 **블록 대각행렬**이라고 한다. 즉 다음과 같은 꼴이다.

$$
\begin{pmatrix}
A_1&0&\cdots&0\\
0&A_2&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&A_m
\end{pmatrix}
$$

**8.36 예: 블록 대각행렬**

다음 행렬은 대각선 블록

$$
A_1=\begin{pmatrix}4\end{pmatrix},\qquad
A_2=\begin{pmatrix}2&-3\\0&2\end{pmatrix},\qquad
A_3=\begin{pmatrix}1&7\\0&1\end{pmatrix}
$$

를 가지는 블록 대각행렬이다.

$$
\begin{pmatrix}
4&0&0&0&0\\
0&2&-3&0&0\\
0&0&2&0&0\\
0&0&0&1&7\\
0&0&0&0&1
\end{pmatrix}
$$

**8.37 상삼각 블록을 가지는 블록 대각행렬**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라 하고, 각 $\lambda_k$의 중복도를 $d_k$라고 하자. 그러면 $T$의 어떤 기저에 대한 행렬은 블록 대각행렬이며, $k$번째 블록 $A_k$는 $d_k\times d_k$ 상삼각 행렬이고 대각선 성분이 모두 $\lambda_k$이다.

즉 각 블록은 다음과 같은 꼴이다.

$$
A_k=
\begin{pmatrix}
\lambda_k&*&\cdots&*\\
0&\lambda_k&\cdots&*\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&\lambda_k
\end{pmatrix}.
$$

**증명**

각 일반화 고유공간 $G(\lambda_k,T)$ 위에서

$$
(T-\lambda_k I)|_{G(\lambda_k,T)}
$$

는 멱영이다. 8.18에 의해 $G(\lambda_k,T)$에는 이 멱영 연산자의 행렬이 상삼각이고 대각선이 모두 $0$인 기저가 존재한다. 같은 기저에 대한 $T|_{G(\lambda_k,T)}$의 행렬은 대각선 성분이 모두 $\lambda_k$인 상삼각 행렬이다.

8.22에 의해 $V$는 이 일반화 고유공간들의 직합이므로, 각 일반화 고유공간에서 얻은 기저들을 이어 붙이면 원하는 블록 대각행렬을 주는 $V$의 기저가 된다.

**8.38 예: 블록 대각행렬**

8.24의 연산자 $T\in\mathcal{L}(\mathbb{C}^3)$에 대해 표준 기저에서의 행렬은 상삼각 행렬이지만 8.37의 블록 대각 꼴은 아니다. 그러나 일반화 고유벡터들로 이루어진 기저

$$
(1,0,0),\quad (0,1,0),\quad (10,2,1)
$$

에 대한 $T$의 행렬은

$$
\begin{pmatrix}
6&3&0\\
0&6&0\\
0&0&7
\end{pmatrix}
$$

이다.

### 연습문제 8B

1. $T\in\mathcal{L}(\mathbb{C}^2)$를 $T(w,z)=(-z,w)$로 정의하자. $T$의 서로 다른 고윳값에 대응하는 일반화 고유공간들을 구하여라.

2. $T\in\mathcal{L}(V)$가 가역이고 $\lambda\ne 0$이라고 하자. 다음을 증명하여라.

   $$
   G(\lambda,T)=G(\lambda^{-1},T^{-1})
   $$

3. $T\in\mathcal{L}(V)$이고 $S\in\mathcal{L}(V)$가 가역이라고 하자. $T$와 $S^{-1}TS$가 같은 고윳값들을 가지며, 대응하는 중복도도 같음을 증명하여라.

4. $\dim V\ge 2$이고 $T\in\mathcal{L}(V)$가

   $$
   \text{null}T^{\dim V-2}\ne \text{null}T^{\dim V-1}
   $$

   을 만족한다고 하자. $T$가 서로 다른 고윳값을 많아야 두 개만 가짐을 증명하여라.

5. $T\in\mathcal{L}(V)$의 고윳값이 $3$과 $8$뿐이라고 하자. $n=\dim V$라 할 때 다음을 증명하여라.

   $$
   V=\text{null}T^{n-2}\oplus\text{range}T^{n-2}
   $$

6. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $\lambda$가 $T$의 고윳값이라고 하자. $T$의 최소다항식을 서로 다른 일차인수들의 거듭제곱의 곱으로 나타낼 때, $z-\lambda$의 지수는

   $$
   (T-\lambda I)^m|_{G(\lambda,T)}=0
   $$

   을 만족하는 가장 작은 양의 정수 $m$임을 증명하여라.

7. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $\lambda$가 $T$의 중복도 $d$인 고윳값이면

   $$
   G(\lambda,T)=\text{null}(T-\lambda I)^d
   $$

   임을 증명하여라. 이는 8.20의 개선이다.

8. $T\in\mathcal{L}(V)$의 서로 다른 고윳값이 $\lambda_1,\ldots,\lambda_m$이라고 하자. 다음이 성립할 필요충분조건은 $T$의 최소다항식이 어떤 양의 정수 $k_1,\ldots,k_m$에 대해

   $$
   (z-\lambda_1)^{k_1}\cdots(z-\lambda_m)^{k_m}
   $$

   인 것임을 증명하여라.

   $$
   V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T)
   $$

9. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T=D+N$이고 $D$는 대각화 가능하며 $N$은 멱영이고 $DN=ND$가 되는 $D,N\in\mathcal{L}(V)$가 존재함을 증명하여라.

10. $V$가 복소 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교 기저이고, $\lambda_1,\ldots,\lambda_n$이 중복도를 포함한 $T$의 고윳값들이라고 하자. 다음을 증명하여라.

    $$
    |\lambda_1|^2+\cdots+|\lambda_n|^2\le
    \|Te_1\|^2+\cdots+\|Te_n\|^2
    $$

11. 특성다항식이 $(z-7)^2(z-8)^2$인 $\mathbb{C}^4$ 위의 연산자의 예를 들어라.

12. 특성다항식이 $(z-1)(z-5)^3$이고 최소다항식이 $(z-1)(z-5)^2$인 $\mathbb{C}^4$ 위의 연산자의 예를 들어라.

13. 특성다항식과 최소다항식이 모두 $z(z-1)^2(z-3)$인 $\mathbb{C}^4$ 위의 연산자의 예를 들어라.

14. 특성다항식이 $z(z-1)^2(z-3)$이고 최소다항식이 $z(z-1)(z-3)$인 $\mathbb{C}^4$ 위의 연산자의 예를 들어라.

15. $T\in\mathcal{L}(\mathbb{C}^4)$를

    $$
    T(z_1,z_2,z_3,z_4)=(0,z_1,z_2,z_3)
    $$

    로 정의하자. $T$의 특성다항식과 최소다항식을 구하여라.

16. $T\in\mathcal{L}(\mathbb{C}^6)$를

    $$
    T(z_1,z_2,z_3,z_4,z_5,z_6)=(0,z_1,z_2,0,z_4,0)
    $$

    로 정의하자. $T$의 특성다항식과 최소다항식을 구하여라.

17. $P\in\mathcal{L}(V)$가 $P^2=P$를 만족한다고 하자. $\dim\text{null}P=m$이고 $\dim\text{range}P=n$이면 $P$의 특성다항식이 $z^m(z-1)^n$임을 증명하여라.

18. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $\lambda$가 $T$의 고윳값이라고 하자. 다음 네 수가 모두 같음을 증명하여라.

- $T$의 최소다항식에서 $z-\lambda$의 지수
- $(T-\lambda I)^m|_{G(\lambda,T)}=0$이 되는 가장 작은 양의 정수 $m$
- $\text{null}(T-\lambda I)^m=\text{null}(T-\lambda I)^{m+1}$이 되는 가장 작은 양의 정수 $m$
- $\text{range}(T-\lambda I)^m=\text{range}(T-\lambda I)^{m+1}$이 되는 가장 작은 양의 정수 $m$

19. $\mathbb{F}=\mathbb{C}$이고 $V$가 내적공간이라고 하자. $S\in\mathcal{L}(V)$가 유니터리이면 $S$의 특성다항식의 상수항의 절댓값이 $1$임을 증명하여라.

20. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $V_1,\ldots,V_m$이 $T$에 대해 불변인 $V$의 부분공간들이고

    $$
    V=V_1\oplus\cdots\oplus V_m
    $$

    이라고 하자. $p_k$를 $T|_{V_k}$의 특성다항식이라고 하면, $T$의 특성다항식은 $p_1\cdots p_m$임을 증명하여라.

21. $p,q$가 복소계수의 최고차항 계수가 $1$인 다항식이고, $p$와 $q$가 같은 영점들을 가지며, $q$가 $p$의 다항식배라고 하자. 그러면 특성다항식이 $q$이고 최소다항식이 $p$인 $\mathbb{C}^{\deg q}$ 위의 연산자가 존재함을 증명하여라. 특히 복소계수의 모든 최고차항 계수가 $1$인 다항식은 어떤 연산자의 특성다항식이다.

22. $A$와 $B$가 같은 블록 크기를 가지는 블록 대각행렬이라고 하자.

    $$
    A=
    \begin{pmatrix}
    A_1&0&\cdots&0\\
    0&A_2&\cdots&0\\
    \vdots&\vdots&\ddots&\vdots\\
    0&0&\cdots&A_m
    \end{pmatrix},
    \qquad
    B=
    \begin{pmatrix}
    B_1&0&\cdots&0\\
    0&B_2&\cdots&0\\
    \vdots&\vdots&\ddots&\vdots\\
    0&0&\cdots&B_m
    \end{pmatrix}.
    $$

    그러면 $AB$도 블록 대각행렬이고, 그 대각선 블록들이 $A_1B_1,\ldots,A_mB_m$임을 증명하여라.

23. $T\in\mathcal{L}(V)$이고 $\mathbb{F}=\mathbb{R}$이라고 하자. $\lambda\in\mathbb{C}$라고 하자.

(a) $u,v\in V$에 대해 $u+iv\in G(\lambda,T_{\mathbb{C}})$일 필요충분조건은 $u-iv\in G(\overline{\lambda},T_{\mathbb{C}})$임을 증명하여라.

(b) $T_{\mathbb{C}}$에 대한 $\lambda$의 중복도와 $\overline{\lambda}$의 중복도가 같음을 증명하여라.

(c) 8.25와 (b)를 사용하여 $\dim V$가 홀수이면 $T_{\mathbb{C}}$가 실수 고윳값을 가져야 함을 증명하여라.

(d) (c)와 5A의 연습문제 17을 사용하여, $\dim V$가 홀수이면 $T$가 고윳값을 가짐을 증명하여라. 여기서 $T_{\mathbb{C}}$는 3B의 연습문제 33에서 정의한 $T$의 복소화이다.

## 8C 일반화 고유공간 분해의 결과

### 연산자의 제곱근

연산자 $R$이

$$
R^2=T
$$

를 만족하면 $R$을 $T$의 제곱근이라고 한다. 모든 연산자가 제곱근을 가지는 것은 아니다. 예를 들어 $T\in\mathcal{L}(\mathbb{C}^3)$를

$$
T(z_1,z_2,z_3)=(z_2,z_3,0)
$$

로 정의하면 $T$는 제곱근을 가지지 않는다. 이 사실은 연습문제 1에서 확인한다. 다음 결과는 가역 복소 연산자에는 항상 제곱근이 존재함을 보이는 핵심이다.

**8.39 항등연산자에 멱영 연산자를 더한 연산자의 제곱근**

$T\in\mathcal{L}(V)$가 멱영이면 $I+T$는 제곱근을 가진다.

**증명**

형식적으로

$$
\sqrt{1+x}=1+a_1x+a_2x^2+a_3x^3+\cdots
\tag{8.40}
$$

라고 쓰자. $T$가 멱영이므로 어떤 양의 정수 $m$에 대해 $T^m=0$이다. 따라서

$$
R=I+a_1T+a_2T^2+\cdots+a_{m-1}T^{m-1}
$$

꼴의 연산자를 찾으면 된다.

$R^2=I+T$가 되도록 계수들을 차례로 정한다. 첫 계수들은

$$
2a_1=1,\qquad 2a_2+a_1^2=0,\qquad 2a_3+2a_1a_2=0
$$

을 만족해야 한다. 일반적으로 $a_j$는 그보다 앞선 계수들로 결정된다. 이런 방식으로 $a_1,\ldots,a_{m-1}$을 정하면 $R^2=I+T$가 된다.

**8.41 복소 가역 연산자는 제곱근을 가진다**

$V$가 복소 벡터공간이고 $T\in\mathcal{L}(V)$가 가역이면 $T$는 제곱근을 가진다.

**증명**

$T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라 하자. $T$가 가역이므로 모든 $\lambda_k$는 $0$이 아니다.

각 일반화 고유공간 $G(\lambda_k,T)$ 위에서

$$
T|_{G(\lambda_k,T)}=\lambda_k I+N_k
$$

라고 쓸 수 있다. 여기서

$$
N_k=(T-\lambda_k I)|_{G(\lambda_k,T)}
$$

는 멱영이다. 따라서

$$
T|_{G(\lambda_k,T)}=\lambda_k\left(I+\frac{1}{\lambda_k}N_k\right).
$$

8.39에 의해 $I+\lambda_k^{-1}N_k$는 제곱근을 가진다. 또한 $\mathbb{C}$에서 $\lambda_k$는 제곱근을 가진다. 그러므로 $G(\lambda_k,T)$ 위에서 $T$의 제곱근 $R_k$를 정의할 수 있다.

8.22에 의해 모든 $v\in V$는 유일하게

$$
v=u_1+\cdots+u_m,\qquad u_k\in G(\lambda_k,T)
$$

로 쓸 수 있다. 이제

$$
Rv=R_1u_1+\cdots+R_mu_m
$$

로 정의하면 $R\in\mathcal{L}(V)$이고 $R^2=T$이다.

같은 아이디어로, 복소 가역 연산자는 임의의 양의 정수 $r$에 대해 $r$제곱근도 가진다.

### 조르당 형식

**8.42 예: 멱영 연산자의 단순한 행렬 표현**

$T\in\mathcal{L}(\mathbb{C}^4)$를

$$
T(z_1,z_2,z_3,z_4)=(0,z_1,z_2,z_3)
$$

로 정의하자. 그러면 $T^4=0$이다. $v=(1,0,0,0)$라고 하면

$$
T^3v,\quad T^2v,\quad Tv,\quad v
$$

는 $\mathbb{C}^4$의 기저이고, 이 기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}
$$

이다.

**8.43 예: 여러 블록을 가지는 멱영 연산자**

$T\in\mathcal{L}(\mathbb{C}^6)$를

$$
T(z_1,z_2,z_3,z_4,z_5,z_6)=(0,z_1,z_2,0,z_4,0)
$$

로 정의하자. 그러면 $T^3=0$이다. 다음 벡터들을 잡자.

$$
v_1=(1,0,0,0,0,0),\quad
v_2=(0,0,0,1,0,0),\quad
v_3=(0,0,0,0,0,1).
$$

그러면

$$
T^2v_1,\quad Tv_1,\quad v_1,\quad Tv_2,\quad v_2,\quad v_3
$$

는 $\mathbb{C}^6$의 기저이고, 이 기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&1&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0
\end{pmatrix}
$$

이다. 이는 크기가 $3,2,1$인 멱영 블록들의 블록 대각행렬이다.

**8.44 정의: 조르당 기저**

$T\in\mathcal{L}(V)$라고 하자. $T$의 어떤 기저에 대한 행렬이 블록 대각행렬이고, 각 대각선 블록이 어떤 $\lambda_k\in\mathbb{F}$에 대해

$$
\begin{pmatrix}
\lambda_k&1&0&\cdots&0\\
0&\lambda_k&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1\\
0&0&0&\cdots&\lambda_k
\end{pmatrix}
$$

꼴이면 그 기저를 $T$의 **조르당 기저**라고 한다. 이런 행렬을 $T$의 **조르당 형식**이라고 부른다.

**8.45 모든 멱영 연산자는 조르당 기저를 가진다**

$T\in\mathcal{L}(V)$가 멱영이면 $T$는 조르당 기저를 가진다.

**증명**

$\dim V$에 대한 귀납법을 사용한다. $\dim V=1$이면 명백하다.

$T^m=0$이 되는 가장 작은 양의 정수를 $m$이라고 하자. 그러면 어떤 $u\in V$에 대해 $T^{m-1}u\ne 0$이다. 8A의 연습문제 2에 의해

$$
u,\ Tu,\ \ldots,\ T^{m-1}u
$$

는 일차독립이다. $U=\text{span}(u,Tu,\ldots,T^{m-1}u)$라고 하자. $U$는 $T$에 대해 불변이다.

만약 $U=V$이면

$$
T^{m-1}u,\ T^{m-2}u,\ \ldots,\ Tu,\ u
$$

가 조르당 기저이다.

이제 $U\ne V$라고 하자. $\varphi(T^{m-1}u)\ne 0$인 $\varphi\in V'$를 택한다. 다음 부분공간을 정의한다.

$$
W=\{v\in V:\varphi(v)=\varphi(Tv)=\cdots=\varphi(T^{m-1}v)=0\}.
$$

그러면 $W$는 $T$에 대해 불변이다. 또한 $U\cap W=\{0\}$이다. 실제로 $U$의 벡터

$$
a_0u+a_1Tu+\cdots+a_{m-1}T^{m-1}u
$$

가 $W$에 속하고, $a_j$ 가운데 처음으로 영이 아닌 계수가 $a_j$라면 $T^{m-1-j}$를 적용한 뒤 $\varphi$를 적용하여 모순을 얻는다.

선형사상 $S:V\to\mathbb{F}^m$를

$$
Sv=\bigl(\varphi(v),\varphi(Tv),\ldots,\varphi(T^{m-1}v)\bigr)
$$

로 정의하면 $\text{null}S=W$이다. 따라서

$$
\dim W\ge \dim V-m.
$$

한편 $\dim U=m$이고 $U\cap W=\{0\}$이므로

$$
\dim(U+W)\ge m+(\dim V-m)=\dim V.
$$

따라서 $V=U\oplus W$이다.

$T|_U$와 $T|_W$는 모두 멱영이다. 귀납가정에 의해 각각 조르당 기저를 가진다. 두 기저를 합치면 $T$의 조르당 기저를 얻는다.

**8.46 조르당 형식**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $T$는 조르당 기저를 가진다.

**증명**

$T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라고 하자. 8.22에 의해

$$
V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T).
$$

각 $G(\lambda_k,T)$ 위에서

$$
(T-\lambda_k I)|_{G(\lambda_k,T)}
$$

는 멱영이다. 8.45에 의해 이 멱영 연산자는 조르당 기저를 가진다. 같은 기저에 대한 $T|_{G(\lambda_k,T)}$의 행렬은 대각선 성분이 모두 $\lambda_k$이고 초대각선의 일부 위치에 $1$이 있는 조르당 블록들의 블록 대각행렬이다. 각 일반화 고유공간에서 얻은 기저들을 이어 붙이면 $T$의 조르당 기저가 된다.

### 연습문제 8C

1. $T\in\mathcal{L}(\mathbb{C}^3)$를

   $$
   T(z_1,z_2,z_3)=(z_2,z_3,0)
   $$

   로 정의하자. $T$가 제곱근을 가지지 않음을 증명하여라.

2. $T\in\mathcal{L}(\mathbb{F}^5)$를

   $$
   T(x_1,x_2,x_3,x_4,x_5)=(2x_2,3x_3,-x_4,4x_5,0)
   $$

   로 정의하자.

(a) $T$가 멱영임을 증명하여라.

(b) $I+T$의 제곱근을 하나 구하여라.

3. $V$가 복소 벡터공간이면 모든 가역 $T\in\mathcal{L}(V)$가 세제곱근을 가짐을 증명하여라.

4. $V$가 실수 벡터공간이라고 하자. $-I$가 제곱근을 가질 필요충분조건은 $\dim V$가 짝수임을 증명하여라.

5. $T\in\mathcal{L}(\mathbb{C}^2)$를

   $$
   T(w,z)=(-w-z,\;9w+5z)
   $$

   로 정의하자. $T$의 조르당 기저를 찾아라.

6. $\mathcal{P}_4(\mathbb{R})$ 위의 미분 연산자 $D$의 조르당 기저를 찾아라.

7. $T\in\mathcal{L}(V)$가 멱영이고 $T$에 대한 어떤 조르당 기저가 주어졌다고 하자. $T$의 최소다항식은 $z^{m+1}$이다. 여기서 $m$은 $T$의 조르당 형식의 초대각선에서 연속으로 나타나는 $1$들의 가장 긴 길이임을 설명하여라.

8. $T\in\mathcal{L}(V)$가 조르당 기저를 가진다고 하자. 같은 기저에 대한 $T^2$의 행렬이 어떤 모양인지 설명하여라.

9. $T\in\mathcal{L}(V)$가 멱영이라고 하자. $V$에는 어떤 벡터 $v_1,\ldots,v_n$과 음이 아닌 정수 $m_1,\ldots,m_n$이 존재하여

   $$
   T^{m_1}v_1,\ldots,Tv_1,v_1,\quad
   \ldots,\quad
   T^{m_n}v_n,\ldots,Tv_n,v_n
   $$

   가 $V$의 기저가 되고, 각 $j$에 대해 $T^{m_j+1}v_j=0$이 됨을 설명하여라.

10. $T\in\mathcal{L}(V)$가 조르당 기저 $v_1,\ldots,v_n$을 가진다고 하자. 역순 기저 $v_n,\ldots,v_1$에 대한 $T$의 행렬은 어떤 모양인지 설명하여라.

11. 조르당 기저의 모든 벡터가 일반화 고유벡터임을 증명하여라.

12. $T\in\mathcal{L}(V)$가 대각화 가능이면 $T$의 모든 조르당 기저에 대한 행렬이 대각행렬임을 증명하여라.

13. $T\in\mathcal{L}(V)$가 멱영이라고 하자. 연습문제 9의 벡터들이 기저를 이루고 각 $j$에 대해 $T^{m_j+1}v_j=0$이라고 하자. 그러면

    $$
    T^{m_1}v_1,\ldots,T^{m_n}v_n
    $$

    이 $\text{null}T$의 기저임을 증명하여라. 따라서 연습문제 9에서 나타나는 블록의 개수 $n$은 $\dim\text{null}T$와 같다.

14. $\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $V$가 $T$에 대해 불변인 두 개의 영이 아닌 부분공간의 직합으로 분해될 수 없을 필요충분조건은 $T$의 최소다항식이 어떤 $\lambda\in\mathbb{C}$에 대해

    $$
    (z-\lambda)^{\dim V}
    $$

    임을 증명하여라.

## 8D 트레이스: 행렬과 연산자의 연결

**8.47 정의: 행렬의 트레이스**

정사각행렬 $A$의 **트레이스** $\text{tr}A$는 $A$의 대각선 성분들의 합이다.

즉 $A$가 $n\times n$ 행렬이면

$$
\text{tr}A=A_{1,1}+\cdots+A_{n,n}.
$$

**8.48 예: 행렬의 트레이스**

$$
A=
\begin{pmatrix}
3&-1&-2\\
5&2&-3\\
1&6&0
\end{pmatrix}
$$

이면

$$
\text{tr}A=3+2+0=5.
$$

**8.49 $\text{tr}(AB)=\text{tr}(BA)$**

$A$가 $m\times n$ 행렬이고 $B$가 $n\times m$ 행렬이면

$$
\text{tr}(AB)=\text{tr}(BA).
$$

**증명**

$$
\begin{aligned}
\text{tr}(AB)
&=\sum_{j=1}^{m}\sum_{k=1}^{n}A_{j,k}B_{k,j}\\
&=\sum_{k=1}^{n}\sum_{j=1}^{m}B_{k,j}A_{j,k}\\
&=\text{tr}(BA).
\end{aligned}
$$

**8.50 연산자의 행렬의 트레이스는 기저 선택에 의존하지 않는다**

$T\in\mathcal{L}(V)$라고 하자. $T$의 두 기저에 대한 행렬을 각각 $A$와 $B$라고 하면

$$
\text{tr}A=\text{tr}B.
$$

**증명**

두 행렬 $A,B$는 닮음이다. 즉 어떤 가역행렬 $C$에 대해

$$
A=C^{-1}BC
$$

이다. 8.49에 의해

$$
\text{tr}A=\text{tr}(C^{-1}BC)=\text{tr}(BCC^{-1})=\text{tr}B.
$$

**8.51 정의: 연산자의 트레이스**

$T\in\mathcal{L}(V)$라고 하자. $T$의 **트레이스** $\text{tr}T$는 $T$의 임의의 기저에 대한 행렬의 트레이스로 정의한다.

8.50에 의해 이 정의는 기저 선택에 의존하지 않는다.

**8.52 복소공간에서 트레이스는 고윳값들의 합이다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $\text{tr}T$는 중복도를 포함한 $T$의 모든 고윳값들의 합이다.

**증명**

8.37에 의해 $T$의 어떤 기저에 대한 행렬은 블록 대각행렬이고, 각 블록의 대각선 성분은 그 블록에 대응하는 고윳값이다. 따라서 이 행렬의 대각선 성분들의 합은 각 고윳값을 그 중복도만큼 더한 값이다. 이것이 $\text{tr}T$이다.

**8.53 예: 트레이스와 고윳값들의 합**

$T\in\mathcal{L}(\mathbb{C}^3)$를

$$
T(z_1,z_2,z_3)=(3z_1-z_2-2z_3,\;3z_1+2z_2-3z_3,\;z_1+2z_2)
$$

로 정의하자. 표준 기저에 대한 $T$의 행렬은

$$
\begin{pmatrix}
3&-1&-2\\
3&2&-3\\
1&2&0
\end{pmatrix}
$$

이고, 따라서 $\text{tr}T=5$이다. $T$의 고윳값들은

$$
1,\quad 2+3i,\quad 2-3i
$$

이며 이들의 합도 $5$이다.

**8.54 트레이스와 특성다항식**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $n=\dim V$라고 하면 $\text{tr}T$는 $T$의 특성다항식에서 $z^{n-1}$의 계수에 음수를 붙인 값이다.

**증명**

중복도를 포함한 $T$의 고윳값을 $\lambda_1,\ldots,\lambda_n$이라고 하자. 특성다항식은

$$
(z-\lambda_1)\cdots(z-\lambda_n)
$$

이다. 이 다항식에서 $z^{n-1}$의 계수는

$$
-(\lambda_1+\cdots+\lambda_n)
$$

이다. 8.52에 의해 $\lambda_1+\cdots+\lambda_n=\text{tr}T$이다.

**8.55 내적공간에서 트레이스**

$V$가 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교 기저이면

$$
\text{tr}T=\langle Te_1,e_1\rangle+\cdots+\langle Te_n,e_n\rangle.
$$

**증명**

정규직교 기저에 대한 $T$의 행렬의 $j,j$ 성분은 $\langle Te_j,e_j\rangle$이다. 따라서 대각선 성분들을 더하면 위 식을 얻는다.

**8.56 트레이스는 선형이다**

사상

$$
\text{tr}:\mathcal{L}(V)\to\mathbb{F}
$$

는 선형이다. 또한 모든 $S,T\in\mathcal{L}(V)$에 대해

$$
\text{tr}(ST)=\text{tr}(TS).
$$

**증명**

기저 하나를 고정하고 연산자들을 그 기저에 대한 행렬로 나타내면, 첫 문장은 행렬의 대각선 성분의 합이 선형임에서 바로 따른다. 두 번째 문장은 8.49에서 따른다.

**8.57 항등연산자는 교환자의 꼴이 될 수 없다**

$V$가 영공간이 아닌 유한차원 벡터공간이면

$$
ST-TS=I
$$

를 만족하는 $S,T\in\mathcal{L}(V)$는 존재하지 않는다.

**증명**

만약 그런 $S,T$가 존재하면 8.56에 의해

$$
\text{tr}(ST-TS)=\text{tr}(ST)-\text{tr}(TS)=0
$$

이다. 그러나 $\text{tr}I=\dim V\ne 0$이므로 모순이다.

### 연습문제 8D

1. $V$가 내적공간이고 $v,w\in V$라고 하자. $T\in\mathcal{L}(V)$를

   $$
   Tu=\langle u,v\rangle w
   $$

   로 정의한다. $\text{tr}T$의 공식을 구하여라.

2. $P\in\mathcal{L}(V)$가 $P^2=P$를 만족하면

   $$
   \text{tr}P=\dim\text{range}P
   $$

   임을 증명하여라.

3. $T\in\mathcal{L}(V)$가 $T^5=T$를 만족한다고 하자. $\text{tr}T$의 실수부와 허수부가 모두 정수임을 증명하여라.

4. $V$가 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 다음을 증명하여라.

   $$
   \text{tr}T^*=\overline{\text{tr}T}
   $$

5. $V$가 내적공간이고 $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. $\text{tr}T=0$이면 $T=0$임을 증명하여라.

6. $V$가 내적공간이고 $P,Q\in\mathcal{L}(V)$가 정사영이라고 하자. 다음을 증명하여라.

   $$
   \text{tr}(PQ)\ge 0
   $$

7. $T\in\mathcal{L}(\mathbb{C}^3)$의 표준 기저에 대한 행렬이

   $$
   \begin{pmatrix}
   51&-12&-21\\
   60&-40&-28\\
   57&-68&1
   \end{pmatrix}
   $$

   이라고 하자. $T$의 두 고윳값이 $-48$과 $24$임을 알고 있다. 행렬식을 계산하지 않고 세 번째 고윳값을 구하여라.

8. $\text{tr}(ST)=(\text{tr}S)(\text{tr}T)$가 모든 $S,T\in\mathcal{L}(V)$에 대해 성립하는지 증명하거나 반례를 들어라.

9. $T\in\mathcal{L}(V)$가 모든 $S\in\mathcal{L}(V)$에 대해

   $$
   \text{tr}(ST)=0
   $$

   을 만족하면 $T=0$임을 증명하여라.

10. $\tau:\mathcal{L}(V)\to\mathbb{F}$가 선형이고 모든 $S,T\in\mathcal{L}(V)$에 대해 $\tau(ST)=\tau(TS)$를 만족하며 $\tau(I)=\dim V$라고 하자. 그러면 $\tau=\text{tr}$임을 증명하여라.

    힌트: $V$의 기저 $v_1,\ldots,v_n$을 고정하자. $P_{j,k}\in\mathcal{L}(V)$를

    $$
    P_{j,k}v_k=v_j,\qquad P_{j,k}v_\ell=0\quad(\ell\ne k)
    $$

    로 정의하자. $\tau(P_{j,k})$가 $j=k$이면 $1$이고 $j\ne k$이면 $0$임을 보인 뒤,

    $$
    T=\sum_{k=1}^n\sum_{j=1}^n\mathcal{M}(T)_{j,k}P_{j,k}
    $$

    를 사용하여라.

11. $V,W$가 유한차원 내적공간이고 $T\in\mathcal{L}(V,W)$라고 하자. $e_1,\ldots,e_n$이 $V$의 정규직교 기저이고 $f_1,\ldots,f_m$이 $W$의 정규직교 기저이면 다음을 증명하여라.

    $$
    \text{tr}(T^*T)=\sum_{k=1}^{n}\sum_{j=1}^{m}|\langle Te_k,f_j\rangle|^2
    $$

12. $V,W$가 유한차원 내적공간이라고 하자.

    (a) $S,T\in\mathcal{L}(V,W)$에 대해

    $$
    \langle S,T\rangle=\text{tr}(T^*S)
    $$

    로 정의하면 $\mathcal{L}(V,W)$ 위의 내적이 됨을 증명하여라.

    (b) $V$의 정규직교 기저 $e_1,\ldots,e_n$과 $W$의 정규직교 기저 $f_1,\ldots,f_m$을 고정하자. (a)에서 정의한 내적은 $\mathbb  {F}^{m,n}$ 위의 표준 내적에 대응함을 증명하여라. 여기서 각 $T\in\mathcal{L}(V,W)$를 이 기저들에 대한 행렬 $\mathcal{M}(T) \in\mathbb{F}^{m,n}$과 동일시한다.

13. $S,T\in\mathcal{L}(\mathcal{P}(\mathbb{F}))$가

    $$
    ST-TS=I
    $$

    를 만족하는 예를 찾아라. 이는 8.57이 무한차원 벡터공간에서는 성립하지 않을 수 있음을 보인다. 힌트: 3.9를 적절히 수정하여라.
