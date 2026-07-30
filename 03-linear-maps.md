# 3장 선형사상

앞의 두 장에서는 벡터공간 자체를 다루었다. 이제 선형대수의 중심 대상인 **선형사상**으로 옮겨 간다. 선형사상은 한 벡터공간의 벡터를 다른 벡터공간의 벡터로 보내면서 덧셈과 스칼라배를 보존하는 함수이다.

이 장의 핵심은 선형사상의 기본정리이다. 이 정리는 정의역의 차원이 영공간의 차원과 치역의 차원의 합이라는 사실을 말한다. 이어서 행렬, 가역성, 동형, 곱공간, 몫공간, 쌍대공간을 선형사상이라는 관점에서 정리한다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.
- $U,V,W$는 $\mathbb{F}$ 위의 벡터공간을 뜻한다.

그림: 브라운슈바이크에 있는 Dankwarderode 성. 가우스는 이곳에서 태어났다. 가우스는 1809년에 선형방정식계를 푸는 방법을 발표했는데, 오늘날 이 방법은 가우스 소거법이라고 불린다. 같은 방법은 그보다 1600년 이상 앞선 중국 수학서에도 나타난다.

## 3A 선형사상들의 벡터공간

### 선형사상의 정의와 예

**3.1 정의: 선형사상**

$V$에서 $W$로 가는 함수 $T$가 다음 두 조건을 만족하면 $T$를 **선형사상**이라고 한다.

- 덧셈성: 모든 $u,v \in V$에 대해

  $$
  T(u+v)=Tu+Tv.
  $$

- 동차성: 모든 $\lambda \in \mathbb{F}$와 모든 $v \in V$에 대해

  $$
  T(\lambda v)=\lambda(Tv).
  $$

선형사상은 선형변환이라고도 부른다. 보통 $T(v)$ 대신 $Tv$라고 쓴다.

**3.2 표기: $\mathcal{L}(V,W)$와 $\mathcal{L}(V)$**

$V$에서 $W$로 가는 모든 선형사상의 집합을 $\mathcal{L}(V,W)$라고 쓴다. 특히 $V$에서 $V$로 가는 선형사상의 집합은

$$
\mathcal{L}(V)=\mathcal{L}(V,V)
$$

로 쓴다.

**3.3 예: 선형사상**

- 영사상 $0 \in \mathcal{L}(V,W)$는 모든 $v \in V$에 대해 $0v=0$으로 정의된다.
- 항등사상 $I \in \mathcal{L}(V)$는 $Iv=v$로 정의된다.
- 미분사상 $D \in \mathcal{L}(\mathcal{P}(\mathbb{R}))$는 $Dp=p'$로 정의된다.
- 적분으로 정의된 사상 $T \in \mathcal{L}(\mathcal{P}(\mathbb{R}),\mathbb{R})$:

  $$
  Tp=\int_0^1 p(x)\thinspace dx.
  $$

- $x^2$를 곱하는 사상 $T \in \mathcal{L}(\mathcal{P}(\mathbb{R}))$:

  $$
  (Tp)(x)=x^2p(x).
  $$

- 뒤로 한 칸 이동하는 사상 $T \in \mathcal{L}(\mathbb{F}^{\infty})$:

  $$
  T(x_1,x_2,x_3,\ldots)=(x_2,x_3,\ldots).
  $$

- $T \in \mathcal{L}(\mathbb{R}^3,\mathbb{R}^2)$를

  $$
  T(x,y,z)=(2x-y+3z,\thickspace7x+5y-6z)
  $$

  로 정의하면 $T$는 선형사상이다.
- 일반적으로 $A_{j,k} \in \mathbb{F}$가 주어졌을 때

  $$
  T(x_1,\ldots,x_n)
  =\left(
  \sum_{k=1}^n A_{1,k}x_k,\ldots,
  \sum_{k=1}^n A_{m,k}x_k
  \right)
  $$

  로 정의된 $T:\mathbb{F}^n \to \mathbb{F}^m$는 선형사상이다.
- 다항식 $q \in \mathcal{P}(\mathbb{R})$를 고정하고

  $$
  (Tp)(x)=p(q(x))
  $$

  로 정의하면 $T \in \mathcal{L}(\mathcal{P}(\mathbb{R}))$이다.

**3.4 선형사상 보조정리**

$v_1,\ldots,v_n$이 $V$의 기저이고 $w_1,\ldots,w_n \in W$라 하자. 그러면

$$
Tv_k=w_k \quad (k=1,\ldots,n)
$$

을 만족하는 선형사상 $T:V \to W$가 유일하게 존재한다.

증명. $v \in V$는 유일하게

$$
v=c_1v_1+\cdots+c_nv_n
$$

으로 표현된다. 따라서

$$
T(c_1v_1+\cdots+c_nv_n)=c_1w_1+\cdots+c_nw_n
$$

로 정의하면 $T$는 잘 정의된다. 이 정의에서 덧셈성과 동차성이 바로 따라오므로 $T$는 선형이다. 또한 $Tv_k=w_k$를 만족한다. 이런 선형사상이 있다면 기저벡터의 값이 모든 벡터의 값을 결정하므로 유일하다.

### 선형사상에 대한 대수적 연산

**3.5 정의: 선형사상의 덧셈과 스칼라곱**

$S,T \in \mathcal{L}(V,W)$와 $\lambda \in \mathbb{F}$에 대해

$$
(S+T)(v)=Sv+Tv,\qquad
(\lambda T)(v)=\lambda(Tv)
$$

로 정의한다.

**3.6 $\mathcal{L}(V,W)$는 벡터공간이다**

위의 덧셈과 스칼라곱으로 $\mathcal{L}(V,W)$는 $\mathbb{F}$ 위의 벡터공간이다. 영벡터는 영사상이고, $T$의 덧셈 역원은 $-T$이다.

**3.7 정의: 선형사상의 곱**

$T \in \mathcal{L}(U,V)$이고 $S \in \mathcal{L}(V,W)$이면 두 선형사상의 곱 $ST \in \mathcal{L}(U,W)$를

$$
(ST)(u)=S(Tu)
$$

로 정의한다. 즉 $ST$는 $S \circ T$이다.

**3.8 선형사상 곱의 대수적 성질**

- 결합법칙:

  $$
  (T_1T_2)T_3=T_1(T_2T_3)
  $$

  양변의 곱이 의미 있을 때 성립한다.

- 항등원:

  $$
  TI=IT=T
  $$

  가 성립한다. 여기서 두 $I$는 각각 적절한 정의역과 공역의 항등사상이다.

- 분배법칙:

  $$
  (S_1+S_2)T=S_1T+S_2T,\qquad
  S(T_1+T_2)=ST_1+ST_2.
  $$

선형사상의 곱은 일반적으로 교환법칙을 만족하지 않는다.

**3.9 예: 교환하지 않는 두 선형사상**

$D$를 미분사상, $T$를 $x^2$를 곱하는 사상이라고 하자. 그러면

$$
((TD)p)(x)=x^2p'(x),
$$

이지만

$$
((DT)p)(x)=x^2p'(x)+2xp(x).
$$

따라서 $TD \ne DT$이다.

**3.10 선형사상은 $0$을 $0$으로 보낸다**

$T$가 $V$에서 $W$로 가는 선형사상이면

$$
T(0)=0.
$$

증명. 덧셈성에 의해

$$
T(0)=T(0+0)=T(0)+T(0)
$$

이므로 양변에 $T(0)$의 덧셈 역원을 더하면 $T(0)=0$이다.

고등학교에서 말하는 일차함수 $f(x)=mx+b$는 $b=0$일 때만 선형사상이다.

### 연습문제 3A

1. $b,c \in \mathbb{R}$라 하자. $T:\mathbb{R}^3 \to \mathbb{R}^2$를

   $$
   T(x,y,z)=(2x-4y+3z+b,\thickspace6x+cxyz)
   $$

   로 정의한다. $T$가 선형일 필요충분조건이 $b=c=0$임을 보여라.

2. $b,c \in \mathbb{R}$라 하자. $T:\mathcal{P}(\mathbb{R}) \to \mathbb{R}^2$를

   $$
   Tp=\left(3p(4)+5p'(6)+bp(1)p(2),\thickspace
   \int_{-1}^{2} x^3p(x)\thinspace dx+c\sin p(0)\right)
   $$

   로 정의한다. $T$가 선형일 필요충분조건이 $b=c=0$임을 보여라.

3. $T \in \mathcal{L}(\mathbb{F}^n,\mathbb{F}^m)$라 하자. 모든 $(x_1,\ldots,x_n)\in\mathbb{F}^n$에 대해

   $$
   T(x_1,\ldots,x_n) =
   (A_{1,1}x_1+\cdots+A_{1,n}x_n,\ldots,
   A_{m,1}x_1+\cdots+A_{m,n}x_n)
   $$

   이 되도록 하는 스칼라 $A_{j,k}\in\mathbb{F}$가 존재함을 보여라.

4. $T \in \mathcal{L}(V,W)$이고 $Tv_1,\ldots,Tv_m$이 $W$에서 선형독립이면 $v_1,\ldots,v_m$이 $V$에서 선형독립임을 증명하라.

5. 3.6에서 주장한 것처럼 $\mathcal{L}(V,W)$가 벡터공간임을 증명하라.

6. 3.8에서 주장한 선형사상 곱의 결합법칙, 항등원 성질, 분배법칙을 증명하라.

7. $\dim V=1$이고 $T \in \mathcal{L}(V)$이면, 모든 $v\in V$에 대해 $Tv=\lambda v$가 되도록 하는 $\lambda \in \mathbb{F}$가 존재함을 증명하라.

8. 모든 $a\in\mathbb{R}$와 $v\in\mathbb{R}^2$에 대해 $\varphi(av)=a\varphi(v)$이지만 선형은 아닌 함수 $\varphi:\mathbb{R}^2 \to \mathbb{R}$의 예를 들어라.

9. 모든 $w,z\in\mathbb{C}$에 대해 $\varphi(w+z)=\varphi(w)+\varphi(z)$이지만, $\mathbb{C}$를 복소벡터공간으로 볼 때 선형은 아닌 함수 $\varphi:\mathbb{C}\to\mathbb{C}$의 예를 들어라.

10. 참인지 증명하거나 반례를 들어라. $q \in \mathcal{P}(\mathbb{R})$이고 $T:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$가 $Tp=q\circ p$로 정의되면 $T$는 선형사상이다.

11. $V$가 유한차원이고 $T \in \mathcal{L}(V)$라 하자. $T$가 항등사상의 스칼라배일 필요충분조건은 모든 $S \in \mathcal{L}(V)$에 대해 $ST=TS$가 성립하는 것임을 증명하라.

12. $U$가 $V$의 진부분공간이고 $S \in \mathcal{L}(U,W)$, $S\ne0$라 하자. $T:V\to W$를

    $$
    Tv =
    \begin{cases}
    Sv, & v\in U,\cr
    0, & v\in V,\ v\notin U
    \end{cases}
    $$

    로 정의한다. $T$가 $V$ 위의 선형사상이 아님을 증명하라.

13. $V$가 유한차원이라고 하자. $U$가 $V$의 부분공간이고 $S \in \mathcal{L}(U,W)$이면 모든 $u\in U$에 대해 $Tu=Su$를 만족하는 $T \in \mathcal{L}(V,W)$가 존재함을 보여라.

14. $V$가 유한차원이고 $\dim V>0$이며 $W$가 무한차원이라고 하자. $\mathcal{L}(V,W)$가 무한차원임을 증명하라.

15. $v_1,\ldots,v_m$이 $V$에서 선형종속이고 $W\ne\lbrace0\rbrace$라 하자. 어떤 $w_1,\ldots,w_m \in W$가 존재하여 $Tv_k=w_k$를 모든 $k=1,\ldots,m$에 대해 만족하는 $T \in \mathcal{L}(V,W)$가 존재하지 않음을 증명하라.

16. $V$가 유한차원이고 $\dim V>1$이면 $ST\ne TS$인 $S,T\in\mathcal{L}(V)$가 존재함을 증명하라.

17. $V$가 유한차원이라고 하자. $\mathcal{L}(V)$의 양쪽 아이디얼은 $\lbrace0\rbrace$와 $\mathcal{L}(V)$뿐임을 보여라. 여기서 부분공간 $\mathcal{E}$가 양쪽 아이디얼이라는 것은 모든 $E\in\mathcal{E}$와 모든 $T\in\mathcal{L}(V)$에 대해 $TE\in\mathcal{E}$이고 $ET\in\mathcal{E}$라는 뜻이다.

## 3B 영공간과 치역

### 영공간과 단사성

**3.11 정의: 영공간**

$T \in \mathcal{L}(V,W)$라 하자. $T$의 영공간은

$$
\text{null}T=\lbrace v\in V:Tv=0\rbrace
$$

으로 정의된다.

**3.12 예: 영공간**

- 영사상의 영공간은 $V$ 전체이다.
- $\varphi:\mathbb{C}^3\to\mathbb{C}$를 $\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3$로 정의하면

  $$
  \text{null}\varphi =
  \lbrace(z_1,z_2,z_3)\in\mathbb{C}^3:z_1+2z_2+3z_3=0\rbrace.
  $$

- 미분사상 $D:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$의 영공간은 상수다항식들의 집합이다.
- $x^2$를 곱하는 사상의 영공간은 $\lbrace0\rbrace$이다.
- 뒤로 이동하는 사상 $T:\mathbb{F}^{\infty}\to\mathbb{F}^{\infty}$의 영공간은

  $$
  \lbrace(a,0,0,\ldots):a\in\mathbb{F}\rbrace
  $$

  이다.

영공간은 kernel이라고도 부른다.

**3.13 영공간은 부분공간이다**

$T \in \mathcal{L}(V,W)$이면 $\text{null}T$는 $V$의 부분공간이다.

증명. $T0=0$이므로 $0\in\text{null}T$이다. $u,v\in\text{null}T$이면

$$
T(u+v)=Tu+Tv=0
$$

이므로 $u+v\in\text{null}T$이다. $\lambda\in\mathbb{F}$이면

$$
T(\lambda u)=\lambda Tu=0
$$

이므로 $\lambda u\in\text{null}T$이다.

**3.14 정의: 단사**

함수 $T:V\to W$가 서로 다른 벡터를 서로 다른 벡터로 보내면 $T$를 **단사**라고 한다. 즉 $u,v\in V$에 대해 $Tu=Tv$이면 $u=v$가 되어야 한다.

**3.15 단사성과 영공간**

$T \in \mathcal{L}(V,W)$라 하자. 그러면

$$
T\text{가 단사} \quad \Longleftrightarrow \quad \text{null}T=\lbrace0\rbrace.
$$

증명. $T$가 단사이면 $Tv=0=T0$에서 $v=0$이므로 영공간은 $\lbrace0\rbrace$이다. 반대로 $\text{null}T=\lbrace0\rbrace$이고 $Tu=Tv$이면 $T(u-v)=0$이므로 $u-v=0$, 따라서 $u=v$이다.

### 치역과 전사성

**3.16 정의: 치역**

$T:V\to W$의 치역은

$$
\text{range}T=\lbrace Tv:v\in V\rbrace
$$

이다.

**3.17 예: 치역**

- 영사상의 치역은 $\lbrace0\rbrace$이다.
- $T:\mathbb{R}^2\to\mathbb{R}^3$가 $T(x,y)=(2x,5y,x+y)$이면 치역은

  $$
  \lbrace(2x,5y,x+y):x,y\in\mathbb{R}\rbrace
  $$

  이다.
- 미분사상 $D:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$의 치역은 $\mathcal{P}(\mathbb{R})$이다.

**3.18 치역은 부분공간이다**

$T \in \mathcal{L}(V,W)$이면 $\text{range}T$는 $W$의 부분공간이다.

증명. $T0=0$이므로 $0$은 치역에 속한다. $w_1=Tv_1$, $w_2=Tv_2$이면 $w_1+w_2=T(v_1+v_2)$이고, $\lambda w_1=T(\lambda v_1)$이다. 따라서 치역은 덧셈과 스칼라곱에 닫혀 있다.

**3.19 정의: 전사**

$T:V\to W$의 치역이 $W$ 전체이면 $T$를 **전사**라고 한다. 즉 $\text{range}T=W$이다.

**3.20 예: 전사성은 공역에 의존한다**

$D \in \mathcal{L}(\mathcal{P}_5(\mathbb{R}))$를 미분사상이라 하자. 이때 $x^5$는 치역에 없으므로 $D:\mathcal{P}_5(\mathbb{R})\to\mathcal{P}_5(\mathbb{R})$는 전사가 아니다. 그러나 같은 규칙으로 정의한

$$
S \in \mathcal{L}(\mathcal{P}_5(\mathbb{R}),\mathcal{P}_4(\mathbb{R}))
$$

는 전사이다.

### 선형사상의 기본정리

**3.21 선형사상의 기본정리**

$V$가 유한차원이고 $T \in \mathcal{L}(V,W)$라 하자. 그러면 $\text{range}T$는 유한차원이고

$$
\dim V=\dim\text{null}T+\dim\text{range}T.
$$

증명. $\text{null}T$의 기저 $u_1,\ldots,u_m$을 $V$의 기저

$$
u_1,\ldots,u_m,v_1,\ldots,v_n
$$

으로 확장한다. 그러면 $Tv_1,\ldots,Tv_n$이 $\text{range}T$의 기저임을 보이면 된다.

먼저 $w\in\text{range}T$라 하자. $w=Tv$이고

$$
v=a_1u_1+\cdots+a_mu_m+b_1v_1+\cdots+b_nv_n
$$

로 쓸 수 있다. $Tu_j=0$이므로

$$
w=b_1Tv_1+\cdots+b_nTv_n.
$$

따라서 $Tv_1,\ldots,Tv_n$은 치역을 생성한다. 또한

$$
c_1Tv_1+\cdots+c_nTv_n=0
$$

이면 $T(c_1v_1+\cdots+c_nv_n)=0$이므로 $c_1v_1+\cdots+c_nv_n\in\text{null}T$이다. 기저의 선형독립성 때문에 모든 $c_j=0$이다. 따라서 $Tv_1,\ldots,Tv_n$은 선형독립이다. 그러므로 $\dim\text{range}T=n$이고 $\dim V=m+n$이다.

**3.22 낮은 차원으로 가는 선형사상은 단사일 수 없다**

$V$와 $W$가 유한차원이고 $\dim V>\dim W$이며 $T \in \mathcal{L}(V,W)$이면 $T$는 단사가 아니다.

증명. 만약 $T$가 단사이면 $\dim\text{null}T=0$이다. 기본정리에 의해 $\dim V=\dim\text{range}T\le \dim W$가 되어 모순이다.

**3.23 예**

$T:\mathbb{F}^4\to\mathbb{F}^3$가 선형이면 $T$는 단사가 아니다. 예를 들어

$$
T(w,x,y,z) =
(w+\sqrt{7}x+5y+\pi z,\thickspace2w+6x-y+3z,\thickspace w+x+y+z)
$$

도 단사가 아니다.

**3.24 높은 차원으로 가는 선형사상은 전사일 수 없다**

$V$와 $W$가 유한차원이고 $\dim V<\dim W$이며 $T \in \mathcal{L}(V,W)$이면 $T$는 전사가 아니다.

증명. $\dim\text{range}T\le \dim V<\dim W$이므로 $\text{range}T\ne W$이다.

선형방정식계를 생각하자. 스칼라 $A_{j,k}\in\mathbb{F}$가 주어졌을 때

$$
\sum_{k=1}^n A_{1,k}x_k=0,\quad
\ldots,\quad
\sum_{k=1}^n A_{m,k}x_k=0
$$

꼴의 방정식계를 동차 선형방정식계라고 한다. 여기에 대응하는 선형사상 $T:\mathbb{F}^n\to\mathbb{F}^m$는

$$
T(x_1,\ldots,x_n)=
\left(
\sum_{k=1}^n A_{1,k}x_k,\ldots,
\sum_{k=1}^n A_{m,k}x_k
\right)
$$

이다.

**3.26 미지수가 방정식보다 많은 동차계**

동차 선형방정식계가 방정식보다 미지수를 더 많이 가지면 $0$이 아닌 해가 존재한다.

증명. 위의 $T:\mathbb{F}^n\to\mathbb{F}^m$에서 $n>m$이면 3.22에 의해 $T$는 단사가 아니므로 $\text{null}T$에 $0$이 아닌 벡터가 있다.

일반 선형방정식계는

$$
\sum_{k=1}^n A_{1,k}x_k=c_1,\quad
\ldots,\quad
\sum_{k=1}^n A_{m,k}x_k=c_m
$$

꼴이다.

**3.28 방정식이 미지수보다 많은 계**

선형방정식계가 미지수보다 방정식을 더 많이 가지면, 어떤 우변 $c_1,\ldots,c_m$에 대해서는 해가 존재하지 않는다.

증명. $m>n$이면 대응하는 $T:\mathbb{F}^n\to\mathbb{F}^m$는 3.24에 의해 전사가 아니다. 따라서 어떤 $c=(c_1,\ldots,c_m)$는 치역에 속하지 않고, 그 우변에 대해서는 해가 없다.

### 연습문제 3B

1. $\dim\text{null}T=3$이고 $\dim\text{range}T=2$인 선형사상 $T$의 예를 들어라.

2. $S,T \in \mathcal{L}(V)$이고 $\text{range}S \subseteq \text{null}T$라 하자. $(ST)^2=0$임을 증명하라.

3. $v_1,\ldots,v_m$이 $V$의 벡터들의 리스트라고 하자. $T\in\mathcal{L}(\mathbb{F}^m,V)$를

   $$
   T(z_1,\ldots,z_m)=z_1v_1+\cdots+z_mv_m
   $$

   로 정의한다.

   (a) $v_1,\ldots,v_m$이 $V$를 생성한다는 것은 $T$의 어떤 성질에 대응하는가?

   (b) $v_1,\ldots,v_m$이 선형독립이라는 것은 $T$의 어떤 성질에 대응하는가?

4. $\lbrace T\in\mathcal{L}(\mathbb{R}^5,\mathbb{R}^4):\dim\text{null}T>2\rbrace$가 $\mathcal{L}(\mathbb{R}^5,\mathbb{R}^4)$의 부분공간이 아님을 보여라.

5. $\text{range}T=\text{null}T$인 $T\in\mathcal{L}(\mathbb{R}^4)$의 예를 들어라.

6. $\text{range}T=\text{null}T$인 $T\in\mathcal{L}(\mathbb{R}^5)$가 존재하지 않음을 증명하라.

7. $V,W$가 유한차원이고 $2\le \dim V\le \dim W$라 하자. 단사가 아닌 $T\in\mathcal{L}(V,W)$들의 집합이 $\mathcal{L}(V,W)$의 부분공간이 아님을 보여라.

8. $V,W$가 유한차원이고 $\dim V\ge \dim W\ge2$라 하자. 전사가 아닌 $T\in\mathcal{L}(V,W)$들의 집합이 $\mathcal{L}(V,W)$의 부분공간이 아님을 보여라.

9. $T\in\mathcal{L}(V,W)$가 단사이고 $v_1,\ldots,v_n$이 $V$에서 선형독립이면 $Tv_1,\ldots,Tv_n$이 $W$에서 선형독립임을 증명하라.

10. $v_1,\ldots,v_n$이 $V$를 생성하고 $T\in\mathcal{L}(V,W)$라 하자. $Tv_1,\ldots,Tv_n$이 $\text{range}T$를 생성함을 보여라.

11. $V$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 다음을 만족하는 $V$의 부분공간 $U$가 존재함을 증명하라.

    $$
    U\cap\text{null}T=\lbrace0\rbrace,
    \qquad
    \text{range}T=\lbrace Tu:u\in U\rbrace.
    $$

12. $T:\mathbb{F}^4\to\mathbb{F}^2$가 선형이고

    $$
    \text{null}T =
    \lbrace(x_1,x_2,x_3,x_4)\in\mathbb{F}^4:x_1=5x_2,\ x_3=7x_4\rbrace
    $$

    라 하자. $T$가 전사임을 증명하라.

13. $U$가 $\mathbb{R}^8$의 3차원 부분공간이고 $T:\mathbb{R}^8\to\mathbb{R}^5$가 선형이며 $\text{null}T=U$라 하자. $T$가 전사임을 증명하라.

14. 영공간이

    $$
    \lbrace(x_1,x_2,x_3,x_4,x_5)\in\mathbb{F}^5:x_1=3x_2,\ x_3=x_4=x_5\rbrace
    $$

    인 $\mathbb{F}^5$에서 $\mathbb{F}^2$로 가는 선형사상은 존재하지 않음을 증명하라.

15. $V$ 위에 영공간과 치역이 모두 유한차원인 선형사상이 존재한다고 하자. $V$가 유한차원임을 증명하라.

16. $V,W$가 모두 유한차원이라고 하자. $V$에서 $W$로 가는 단사 선형사상이 존재할 필요충분조건은 $\dim V\le\dim W$임을 증명하라.

17. $V,W$가 모두 유한차원이라고 하자. $V$에서 $W$로 가는 전사 선형사상이 존재할 필요충분조건은 $\dim V\ge\dim W$임을 증명하라.

18. $V,W$가 유한차원이고 $U$가 $V$의 부분공간이라고 하자. $\text{null}T=U$인 $T\in\mathcal{L}(V,W)$가 존재할 필요충분조건은

    $$
    \dim U\ge \dim V-\dim W
    $$

    임을 증명하라.

19. $W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. $T$가 단사일 필요충분조건은 $ST$가 $V$ 위의 항등연산자가 되도록 하는 $S\in\mathcal{L}(W,V)$가 존재하는 것임을 증명하라.

20. $W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. $T$가 전사일 필요충분조건은 $TS$가 $W$ 위의 항등연산자가 되도록 하는 $S\in\mathcal{L}(W,V)$가 존재하는 것임을 증명하라.

21. $V$가 유한차원이고 $T\in\mathcal{L}(V,W)$이며 $U$가 $W$의 부분공간이라고 하자. $\lbrace v\in V:Tv\in U\rbrace$가 $V$의 부분공간임을 증명하고,

    $$
    \dim\lbrace v\in V:Tv\in U\rbrace =
    \dim\text{null}T+\dim(U\cap\text{range}T)
    $$

    임을 증명하라.

22. $U,V$가 유한차원 벡터공간이고 $S\in\mathcal{L}(V,W)$, $T\in\mathcal{L}(U,V)$라 하자. 다음을 증명하라.

    $$
    \dim\text{null}ST
    \le
    \dim\text{null}S+\dim\text{null}T.
    $$

23. $U,V$가 유한차원 벡터공간이고 $S\in\mathcal{L}(V,W)$, $T\in\mathcal{L}(U,V)$라 하자. 다음을 증명하라.

    $$
    \dim\text{range}ST
    \le
    \min\lbrace\dim\text{range}S,\dim\text{range}T\rbrace.
    $$

24. (a) $\dim V=5$이고 $S,T\in\mathcal{L}(V)$이며 $ST=0$이라 하자. $\dim\text{range}TS\le2$임을 증명하라.

    (b) $ST=0$이고 $\dim\text{range}TS=2$인 $S,T\in\mathcal{L}(\mathbb{F}^5)$의 예를 들어라.

25. $W$가 유한차원이고 $S,T\in\mathcal{L}(V,W)$라 하자. $\text{null}S\subseteq\text{null}T$일 필요충분조건은 $T=ES$가 되도록 하는 $E\in\mathcal{L}(W)$가 존재하는 것임을 증명하라.

26. $V$가 유한차원이고 $S,T\in\mathcal{L}(V,W)$라 하자. $\text{range}S\subseteq\text{range}T$일 필요충분조건은 $S=TE$가 되도록 하는 $E\in\mathcal{L}(V)$가 존재하는 것임을 증명하라.

27. $P\in\mathcal{L}(V)$이고 $P^2=P$라 하자. 다음을 증명하라.

    $$
    V=\text{null}P\oplus\text{range}P.
    $$

28. $D\in\mathcal{L}(\mathcal{P}(\mathbb{R}))$가 모든 비상수 다항식 $p$에 대해 $\deg Dp=(\deg p)-1$을 만족한다고 하자. $D$가 전사임을 증명하라.

29. $p\in\mathcal{P}(\mathbb{R})$라 하자. 다음을 만족하는 $q\in\mathcal{P}(\mathbb{R})$가 존재함을 증명하라.

    $$
    5q''+3q'=p.
    $$

30. $\varphi\in\mathcal{L}(V,\mathbb{F})$이고 $\varphi\ne0$라 하자. $u\in V$가 $\text{null}\varphi$에 속하지 않으면

    $$
    V=\text{null}\varphi\oplus\lbrace au:a\in\mathbb{F}\rbrace
    $$

    임을 증명하라.

31. $V$가 유한차원이고 $X$가 $V$의 부분공간이며 $Y$가 $W$의 유한차원 부분공간이라고 하자. $\text{null}T=X$이고 $\text{range}T=Y$인 $T\in\mathcal{L}(V,W)$가 존재할 필요충분조건은

    $$
    \dim X+\dim Y=\dim V
    $$

    임을 증명하라.

32. $V$가 유한차원이고 $\dim V>1$이라 하자. 선형사상 $\varphi:\mathcal{L}(V)\to\mathbb{F}$가 모든 $S,T\in\mathcal{L}(V)$에 대해

    $$
    \varphi(ST)=\varphi(S)\varphi(T)
    $$

    를 만족하면 $\varphi=0$임을 보여라.

33. $V,W$가 실벡터공간이고 $T\in\mathcal{L}(V,W)$라 하자. 모든 $u,v\in V$에 대해

    $$
    T_{\mathbb{C}}(u+iv)=Tu+iTv
    $$

    로 $T_{\mathbb{C}}:V_{\mathbb{C}}\to W_{\mathbb{C}}$를 정의한다.

    (a) $T_{\mathbb{C}}$가 $V_{\mathbb{C}}$에서 $W_{\mathbb{C}}$로 가는 복소 선형사상임을 보여라.

    (b) $T_{\mathbb{C}}$가 단사일 필요충분조건은 $T$가 단사인 것임을 보여라.

    (c) $\text{range}T_{\mathbb{C}}=W_{\mathbb{C}}$일 필요충분조건은 $\text{range}T=W$인 것임을 보여라.

## 3C 행렬

### 선형사상을 행렬로 나타내기

**3.29 정의: 행렬**

$m$행 $n$열 행렬은 $\mathbb{F}$의 원소들이 직사각형 모양으로 배열된 것이다.

$$
A =
\begin{pmatrix}
A_{1,1} & \cdots & A_{1,n}\cr
\vdots & & \vdots\cr
A_{m,1} & \cdots & A_{m,n}
\end{pmatrix}.
$$

$j$행 $k$열의 원소를 $A_{j,k}$라고 쓴다.

**3.30 예**

$$
A =
\begin{pmatrix}
8 & 4 & 5-3i\cr
1 & 9 & 7
\end{pmatrix}
$$

이면 $A_{2,3}=7$이다.

**3.31 정의: 선형사상의 행렬 $\mathcal{M}(T)$**

$T\in\mathcal{L}(V,W)$이고 $v_1,\ldots,v_n$이 $V$의 기저, $w_1,\ldots,w_m$이 $W$의 기저라고 하자. $T$의 행렬 $\mathcal{M}(T)$는 각 $k=1,\ldots,n$에 대해

$$
Tv_k=A_{1,k}w_1+\cdots+A_{m,k}w_m
$$

이 되도록 하는 $m$행 $n$열 행렬 $A$이다. 필요하면

$$
\mathcal{M}(T,(v_1,\ldots,v_n),(w_1,\ldots,w_m))
$$

로 기저를 명시한다.

즉 $\mathcal{M}(T)$의 $k$번째 열은 $Tv_k$를 $w_1,\ldots,w_m$에 대해 표현한 좌표들이다.

**3.32 예**

$T:\mathbb{F}^2\to\mathbb{F}^3$를

$$
T(x,y)=(x+3y,\thickspace2x+5y,\thickspace7x+9y)
$$

로 정의하고 표준기저를 쓰면

$$
\mathcal{M}(T)=
\begin{pmatrix}
1 & 3\cr
2 & 5\cr
7 & 9
\end{pmatrix}.
$$

**3.33 예: 미분사상의 행렬**

$D:\mathcal{P}_3(\mathbb{R})\to\mathcal{P}_2(\mathbb{R})$를 $Dp=p'$로 정의하고 표준기저를 쓰면

$$
\mathcal{M}(D)=
\begin{pmatrix}
0 & 1 & 0 & 0\cr
0 & 0 & 2 & 0\cr
0 & 0 & 0 & 3
\end{pmatrix}.
$$

### 행렬의 덧셈과 스칼라곱

**3.34 행렬의 덧셈**

크기가 같은 두 행렬 $A,C$의 합은 같은 위치의 성분을 더해 정의한다.

$$
(A+C)_{j,k}=A_{j,k}+C_{j,k}.
$$

**3.35 선형사상 합의 행렬**

$S,T\in\mathcal{L}(V,W)$이면

$$
\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T).
$$

**3.36 행렬의 스칼라곱**

스칼라 $\lambda\in\mathbb{F}$와 행렬 $A$에 대해

$$
(\lambda A)_{j,k}=\lambda A_{j,k}
$$

로 정의한다.

**3.37 예**

$$
2
\begin{pmatrix}
3 & 1\cr
-1 & 5
\end{pmatrix} +
\begin{pmatrix}
4 & 2\cr
1 & 6
\end{pmatrix} =
\begin{pmatrix}
10 & 4\cr
-1 & 16
\end{pmatrix}.
$$

**3.38 스칼라배 선형사상의 행렬**

$$
\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T).
$$

**3.39 표기: $\mathbb{F}^{m,n}$**

$\mathbb{F}$의 원소를 성분으로 가지는 모든 $m$행 $n$열 행렬의 벡터공간을 $\mathbb{F}^{m,n}$이라고 쓴다.

**3.40 행렬공간의 차원**

$$
\dim\mathbb{F}^{m,n}=mn.
$$

### 행렬의 곱

선형사상의 합과 스칼라곱에 맞추어 행렬의 합과 스칼라곱을 정의했다. 이제 선형사상 합성의 행렬이 행렬 곱이 되도록 행렬 곱을 정의한다.

**3.41 행렬 곱**

$A$가 $m$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이면 $AB$는 $m$행 $p$열 행렬이며

$$
(AB)_{j,k}=\sum_{r=1}^n A_{j,r}B_{r,k}
$$

로 정의된다.

**3.42 예**

$$
\begin{pmatrix}
1 & 2\cr
3 & 4\cr
5 & 6
\end{pmatrix}
\begin{pmatrix}
6 & 5 & 4 & 3\cr
2 & 1 & 0 & -1
\end{pmatrix} =
\begin{pmatrix}
10 & 7 & 4 & 1\cr
26 & 19 & 12 & 5\cr
42 & 31 & 20 & 9
\end{pmatrix}.
$$

**3.43 합성의 행렬**

$T\in\mathcal{L}(U,V)$이고 $S\in\mathcal{L}(V,W)$이면

$$
\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)
$$

이다. 이 등식에서 각 행렬은 해당 공간들에 선택된 기저에 대해 계산한다.

**3.44 행과 열 표기**

$A_{j,\cdot}$는 $A$의 $j$번째 행을 뜻하고, $A_{\cdot,k}$는 $A$의 $k$번째 열을 뜻한다.

**3.45 예**

$$
A=
\begin{pmatrix}
8 & 4 & 5\cr
1 & 9 & 7
\end{pmatrix}
$$

이면

$$
A_{2,\cdot}=\begin{pmatrix}1&9&7\end{pmatrix},
\qquad
A_{\cdot,3}=\begin{pmatrix}5\cr7\end{pmatrix}.
$$

**3.46 행렬 곱의 성분은 행과 열의 곱이다**

$A$가 $m$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이면

$$
(AB)_{j,k}=A_{j,\cdot}B_{\cdot,k}.
$$

**3.48 곱의 열**

$A$가 $m$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이면

$$
(AB)_{\cdot,k}=AB_{\cdot,k}.
$$

즉 $AB$의 $k$번째 열은 $A$와 $B$의 $k$번째 열의 곱이다.

**3.49 예**

$$
\begin{pmatrix} 1 & 2\cr 3 & 4\cr 5 & 6 \end{pmatrix}
\begin{pmatrix} 5\cr 1 \end{pmatrix} =
\begin{pmatrix} 7\cr 19\cr 31 \end{pmatrix} =
5
\begin{pmatrix} 1\cr 3\cr 5 \end{pmatrix} +
\begin{pmatrix} 2\cr 4\cr 6 \end{pmatrix}.
$$

**3.50 행렬과 열벡터의 곱**

$A$가 $m$행 $n$열 행렬이고

$$
b= \begin{pmatrix} b_1\cr \vdots\cr b_n \end{pmatrix}
$$

이면

$$
Ab=b_1A_{\cdot,1}+\cdots+b_nA_{\cdot,n}.
$$

즉 $Ab$는 $A$의 열들의 선형결합이다.

**3.51 행렬 곱을 열 또는 행의 선형결합으로 보기**

$A$가 $m$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이면 다음이 성립한다.

(a) $AB$의 $k$번째 열은 $A$의 열들의 선형결합이고, 그 계수는 $B$의 $k$번째 열에서 온다.

(b) $AB$의 $j$번째 행은 $B$의 행들의 선형결합이고, 그 계수는 $A$의 $j$번째 행에서 온다.

### 열-행 분해와 계수

**3.52 정의: 열계수와 행계수**

행렬 $A$의 열계수는 $A$의 열들이 생성하는 공간의 차원이다. 행계수는 $A$의 행들이 생성하는 공간의 차원이다.

**3.53 예**

$$
\begin{pmatrix} 4 & 7 & 1 & 8\cr 3 & 5 & 2 & 9 \end{pmatrix}
$$

의 열계수와 행계수는 모두 $2$이다.

**3.54 정의: 전치행렬**

$A$의 전치행렬 $A^t$는 행과 열을 바꾼 행렬이다. 즉

$$
(A^t)_{k,j}=A_{j,k}.
$$

**3.55 예와 성질**

$$
\begin{pmatrix} 5 & -7\cr 3 & 8\cr -4 & 2 \end{pmatrix}^t =
\begin{pmatrix} 5 & 3 & -4\cr -7 & 8 & 2 \end{pmatrix}.
$$

또한 적절한 크기의 행렬에 대해

$$
(A+B)^t = A^t+B^t,\qquad
(\lambda A)^t = \lambda A^t,\qquad
(AC)^t = C^tA^t.
$$

**3.56 열-행 분해**

$A$가 열계수 $c\ge1$인 $m$행 $n$열 행렬이면, 어떤 $m$행 $c$열 행렬 $C$와 $c$행 $n$열 행렬 $R$가 존재하여

$$
A=CR
$$

이 된다.

증명. $A$의 열공간의 기저가 되는 $c$개의 열을 $C$의 열로 삼는다. 그러면 $A$의 각 열은 $C$의 열들의 선형결합이므로, 그 계수들을 $R$의 대응하는 열로 두면 $A=CR$이다.

**3.57 열계수는 행계수와 같다**

모든 행렬에서 열계수와 행계수는 같다.

증명. $A=CR$라는 열-행 분해를 쓰면 $A$의 행들은 $R$의 행들의 선형결합이므로 행계수는 열계수 이하이다. 같은 논리를 $A^t$에 적용하면 반대 부등식도 얻는다.

**3.58 정의: 계수**

행렬 $A\in\mathbb{F}^{m,n}$의 **계수** 또는 **rank**는 $A$의 열계수이다. 3.57에 의해 이는 행계수와 같다.

### 연습문제 3C

1. $T\in\mathcal{L}(V,W)$라 하자. $V$와 $W$의 어떤 기저를 선택하더라도 $T$의 행렬은 적어도 $\dim\text{range}T$개의 $0$이 아닌 성분을 가짐을 보여라.

2. $V,W$가 유한차원이고 $0$이 아니며 $T\in\mathcal{L}(V,W)$라 하자. $\dim\text{range}T=1$일 필요충분조건은 어떤 $V$의 기저와 $W$의 기저가 존재하여 그 기저들에 대한 $\mathcal{M}(T)$의 모든 성분이 $1$이 되는 것임을 증명하라.

3. $v_1,\ldots,v_n$이 $V$의 기저이고 $w_1,\ldots,w_m$이 $W$의 기저라고 하자.

   (a) $S,T\in\mathcal{L}(V,W)$이면 $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$임을 보여라.

   (b) $\lambda\in\mathbb{F}$이고 $T\in\mathcal{L}(V,W)$이면 $\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T)$임을 보여라.

4. $D\in\mathcal{L}(\mathcal{P}_3(\mathbb{R}),\mathcal{P}_2(\mathbb{R}))$가 $Dp=p'$인 미분사상이라고 하자. 어떤 $\mathcal{P}_3(\mathbb{R})$의 기저와 $\mathcal{P}_2(\mathbb{R})$의 기저를 골라 $D$의 행렬이

   $$
   \begin{pmatrix}
   1 & 0 & 0 & 0\cr
   0 & 1 & 0 & 0\cr
   0 & 0 & 1 & 0
   \end{pmatrix}
   $$

   이 되게 하라.

5. $V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 어떤 $V$의 기저와 $W$의 기저를 고르면 $\mathcal{M}(T)$의 성분 중 $1\le k\le\dim\text{range}T$에 대해 $k$행 $k$열 성분만 $1$이고 나머지는 모두 $0$이 되도록 할 수 있음을 증명하라.

6. $v_1,\ldots,v_m$이 $V$의 기저이고 $W$가 유한차원이며 $T\in\mathcal{L}(V,W)$라 하자. $W$의 어떤 기저 $w_1,\ldots,w_n$을 골라, 주어진 $V$의 기저와 이 $W$의 기저에 대한 $\mathcal{M}(T)$의 첫 번째 열 성분들이 첫 번째 행의 $1$일 가능성을 제외하고 모두 $0$이 되도록 할 수 있음을 증명하라.

7. $w_1,\ldots,w_n$이 $W$의 기저이고 $V$가 유한차원이며 $T\in\mathcal{L}(V,W)$라 하자. $V$의 어떤 기저 $v_1,\ldots,v_m$을 골라, $\mathcal{M}(T)$의 첫 번째 행 성분들이 첫 번째 행 첫 번째 열의 $1$일 가능성을 제외하고 모두 $0$이 되도록 할 수 있음을 증명하라.

8. $A$가 $m$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이라 하자. 모든 $1\le j\le m$에 대해

   $$
   (AB)_{j,\cdot}=A_{j,\cdot}B
   $$

   임을 증명하라.

9. $a=(a_1\ \cdots\ a_n)$가 $1$행 $n$열 행렬이고 $B$가 $n$행 $p$열 행렬이라 하자. 다음을 증명하라.

   $$
   aB=a_1B_{1,\cdot}+\cdots+a_nB_{n,\cdot}.
   $$

10. $AB\ne BA$인 $2$행 $2$열 행렬 $A,B$의 예를 들어라.

11. 행렬 덧셈과 행렬 곱셈에 대한 분배법칙을 증명하라. 즉 크기가 맞을 때

    $$
    A(B+C)=AB+AC,\qquad
    (D+E)F=DF+EF
    $$

    를 증명하라.

12. 행렬 곱셈의 결합법칙을 증명하라. 즉 $(AB)C$가 의미 있으면 $A(BC)$도 의미 있고

    $$
    (AB)C=A(BC)
    $$

    임을 증명하라.

13. $A$가 $n$행 $n$열 행렬이고 $1\le j,k\le n$이라 하자. $A^3$의 $j$행 $k$열 성분이

    $$
    \sum_{p=1}^n\sum_{r=1}^n A_{j,p}A_{p,r}A_{r,k}
    $$

    임을 보여라.

14. $m,n$이 양의 정수라고 하자. $A\mapsto A^t$가 $\mathbb{F}^{m,n}$에서 $\mathbb{F}^{n,m}$으로 가는 선형사상임을 증명하라.

15. $A$가 $m$행 $n$열 행렬이고 $C$가 $n$행 $p$열 행렬이면

    $$
    (AC)^t=C^tA^t
    $$

    임을 증명하라.

16. $A$가 $0$이 아닌 $m$행 $n$열 행렬이라고 하자. $A$의 계수가 $1$일 필요충분조건은 모든 $j=1,\ldots,m$과 $k=1,\ldots,n$에 대해

    $$
    A_{j,k}=c_jd_k
    $$

    가 되도록 하는 $(c_1,\ldots,c_m)\in\mathbb{F}^m$와 $(d_1,\ldots,d_n)\in\mathbb{F}^n$가 존재하는 것임을 증명하라.

17. $T\in\mathcal{L}(V)$이고 $u_1,\ldots,u_n$과 $v_1,\ldots,v_n$이 $V$의 기저라고 하자. 다음 조건들이 서로 동치임을 증명하라.

    (a) $T$는 단사이다.

    (b) $\mathcal{M}(T)$의 열들이 $\mathbb{F}^{n,1}$에서 선형독립이다.

    (c) $\mathcal{M}(T)$의 열들이 $\mathbb{F}^{n,1}$을 생성한다.

    (d) $\mathcal{M}(T)$의 행들이 $\mathbb{F}^{1,n}$을 생성한다.

    (e) $\mathcal{M}(T)$의 행들이 $\mathbb{F}^{1,n}$에서 선형독립이다.

    여기서 $\mathcal{M}(T)$는 $\mathcal{M}(T,(u_1,\ldots,u_n),(v_1,\ldots,v_n))$를 뜻한다.

## 3D 가역성과 동형

### 가역 선형사상

**3.59 정의: 가역, 역**

- $T\in\mathcal{L}(V,W)$에 대해 어떤 $S\in\mathcal{L}(W,V)$가 존재하여 $ST$가 $V$ 위의 항등연산자이고 $TS$가 $W$ 위의 항등연산자이면 $T$를 **가역**이라고 한다.
- $ST=I$이고 $TS=I$를 만족하는 $S$를 $T$의 **역**이라고 한다.

**3.60 역은 유일하다**

가역 선형사상의 역은 유일하다.

증명. $S_1,S_2$가 모두 $T$의 역이면

$$
S_1=S_1I=S_1(TS_2)=(S_1T)S_2=IS_2=S_2.
$$

**3.61 표기: $T^{-1}$**

$T$가 가역이면 그 유일한 역을 $T^{-1}$로 쓴다. 즉

$$
T^{-1}T=I,\qquad TT^{-1}=I.
$$

**3.62 예**

$T\in\mathcal{L}(\mathbb{R}^3)$를

$$
T(x,y,z)=(-y,x,4z)
$$

로 정의하자. 이는 $xy$-평면에서 반시계 방향 $90^\circ$ 회전하고 $z$축 방향으로 $4$배 늘리는 사상이다. 역사상은

$$
T^{-1}(x,y,z)=\left(y,-x,\frac14 z\right)
$$

이다.

**3.63 가역성 $\Longleftrightarrow$ 단사성과 전사성**

선형사상이 가역일 필요충분조건은 단사이고 전사인 것이다.

증명. $T$가 가역이면 $Tu=Tv$에서 $u=T^{-1}Tu=T^{-1}Tv=v$이므로 단사이다. 또한 임의의 $w\in W$에 대해 $w=T(T^{-1}w)$이므로 전사이다.

반대로 $T$가 단사이고 전사라고 하자. 각 $w\in W$에 대해 $T(Sw)=w$가 되도록 하는 유일한 $Sw\in V$를 정의한다. 단사성과 전사성 때문에 이런 $S$가 잘 정의된다. 그러면 $TS=I$이고, 단사성을 이용하면 $ST=I$도 얻는다. 덧셈성과 동차성은 $T$를 적용해 확인하면 되므로 $S$는 선형이다. 따라서 $T$는 가역이다.

**3.64 예: 단사성 또는 전사성 하나만으로는 가역성이 따라오지 않는다**

- $x^2$를 곱하는 $\mathcal{P}(\mathbb{R})$ 위의 선형사상은 단사이지만 전사가 아니므로 가역이 아니다.
- $\mathbb{F}^{\infty}$에서 뒤로 이동하는 사상은 전사이지만 단사가 아니므로 가역이 아니다.

**3.65 단사성은 전사성과 동치이다: $\dim V=\dim W<\infty$인 경우**

$V,W$가 유한차원이고 $\dim V=\dim W$, $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
T\text{가 가역}
\quad\Longleftrightarrow\quad
T\text{가 단사}
\quad\Longleftrightarrow\quad
T\text{가 전사}.
$$

증명. 기본정리에 의해

$$
\dim V=\dim\text{null}T+\dim\text{range}T.
$$

$T$가 단사이면 $\dim\text{null}T=0$이므로 $\dim\text{range}T=\dim V=\dim W$이고, 따라서 $T$는 전사이다. 반대로 $T$가 전사이면 $\dim\text{range}T=\dim W=\dim V$이므로 $\dim\text{null}T=0$이고, 따라서 $T$는 단사이다. 3.63에 의해 가역성과도 동치이다.

**3.67 예: $((x^2+5x+7)p)''=q$를 만족하는 다항식 $p$의 존재**

$q\in\mathcal{P}(\mathbb{R})$라 하자. 어떤 $m\ge0$에 대해 $q\in\mathcal{P}_m(\mathbb{R})$이다. $T:\mathcal{P}_m(\mathbb{R})\to\mathcal{P}_m(\mathbb{R})$를

$$
Tp=((x^2+5x+7)p)''
$$

로 정의한다. $0$이 아닌 $p$에 대해 $(x^2+5x+7)p$의 차수는 $p$의 차수보다 $2$ 크고, 두 번 미분하면 다시 $p$의 차수가 된다. 따라서 $T$는 $\mathcal{P}_m(\mathbb{R})$에서 자기 자신으로 가는 선형사상이다. $Tp=0$이면 $(x^2+5x+7)p$의 두 번째 미분이 $0$이므로 $(x^2+5x+7)p$는 일차 이하의 다항식이어야 한다. 이는 $p=0$일 때만 가능하다. 따라서 $T$는 단사이고, 3.65에 의해 전사이다. 그러므로 원하는 $p$가 존재한다.

**3.68 같은 차원 공간에서 $ST=I \Longleftrightarrow TS=I$**

$V,W$가 같은 차원의 유한차원 벡터공간이고 $S\in\mathcal{L}(W,V)$, $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
ST=I \quad\Longleftrightarrow\quad TS=I.
$$

증명. $ST=I$라고 하자. $Tv=0$이면 $v=STv=S0=0$이므로 $T$는 단사이다. 3.65에 의해 $T$는 가역이다. $ST=I$의 오른쪽에 $T^{-1}$을 곱하면 $S=T^{-1}$이고, 따라서 $TS=I$이다. 반대 방향도 $S,T$의 역할을 바꾸면 같다.

### 동형인 벡터공간

**3.69 정의: 동형사상, 동형**

- **동형사상**은 가역 선형사상이다.
- 두 벡터공간 사이에 동형사상이 존재하면 두 벡터공간은 **동형**이라고 한다.

동형사상 $T:V\to W$는 $V$의 벡터 $v$에 $W$의 이름 $Tv$를 붙이는 재명명으로 볼 수 있다. 따라서 동형인 벡터공간은 벡터공간으로서 본질적으로 같은 성질을 가진다.

**3.70 차원은 유한차원 벡터공간의 동형 여부를 결정한다**

$\mathbb{F}$ 위의 두 유한차원 벡터공간은 차원이 같을 필요충분조건으로 동형이다.

증명. $V$와 $W$가 동형이면 어떤 동형사상 $T:V\to W$가 존재한다. 그러면 $\text{null}T=\lbrace0\rbrace$이고 $\text{range}T=W$이므로 기본정리에 의해 $\dim V=\dim W$이다.

반대로 $\dim V=\dim W=n$이라 하자. $V$의 기저 $v_1,\ldots,v_n$과 $W$의 기저 $w_1,\ldots,w_n$을 잡고

$$
T(c_1v_1+\cdots+c_nv_n)=c_1w_1+\cdots+c_nw_n
$$

로 정의하면 $T$는 단사이고 전사인 선형사상이다. 따라서 동형사상이다.

모든 유한차원 벡터공간 $V$는 $\mathbb{F}^{\dim V}$와 동형이다. 그러나 실제 연구에서는 영공간, 치역, 다항식공간 등 자연스럽게 생기는 벡터공간을 그대로 다루는 것이 더 명료한 경우가 많다.

**3.71 $\mathcal{L}(V,W)$와 $\mathbb{F}^{m,n}$은 동형이다**

$v_1,\ldots,v_n$이 $V$의 기저이고 $w_1,\ldots,w_m$이 $W$의 기저라 하자. 그러면

$$
T\mapsto\mathcal{M}(T)
$$

는 $\mathcal{L}(V,W)$에서 $\mathbb{F}^{m,n}$으로 가는 동형사상이다.

증명. 3.35와 3.38에 의해 이 사상은 선형이다. $\mathcal{M}(T)=0$이면 모든 기저벡터 $v_k$에 대해 $Tv_k=0$이므로 $T=0$이고, 따라서 단사이다. 임의의 행렬 $A\in\mathbb{F}^{m,n}$에 대해 선형사상 보조정리를 사용하면

$$
Tv_k=\sum_{j=1}^m A_{j,k}w_j
$$

가 되도록 하는 $T$가 존재한다. 이때 $\mathcal{M}(T)=A$이므로 전사이다.

**3.72 선형사상공간의 차원**

$V,W$가 유한차원이면 $\mathcal{L}(V,W)$도 유한차원이고

$$
\dim\mathcal{L}(V,W)=(\dim V)(\dim W).
$$

### 행렬곱으로 생각한 선형사상

**3.73 정의: 벡터의 행렬 $\mathcal{M}(v)$**

$v\in V$이고 $v_1,\ldots,v_n$이 $V$의 기저라고 하자. $v$를

$$
v=b_1v_1+\cdots+b_nv_n
$$

으로 쓸 때, 이 기저에 대한 $v$의 행렬은

$$
\mathcal{M}(v)= \begin{pmatrix} b_1\cr \vdots\cr b_n \end{pmatrix}
$$

이다.

**3.74 예**

표준기저에 대한 $2-7x+5x^3+x^4\in\mathcal{P}_4(\mathbb{R})$의 행렬은

$$
\begin{pmatrix} 2\cr -7\cr 0\cr 5\cr 1 \end{pmatrix}
$$

이다. 또한 $x=(x_1,\ldots,x_n)\in\mathbb{F}^n$의 표준기저에 대한 행렬은

$$
\mathcal{M}(x)= \begin{pmatrix} x_1\cr \vdots\cr x_n \end{pmatrix}
$$

이다.

**3.75 $\mathcal{M}(T)_{\cdot,k}=\mathcal{M}(Tv_k)$**

$T\in\mathcal{L}(V,W)$이고 $v_1,\ldots,v_n$이 $V$의 기저, $w_1,\ldots,w_m$이 $W$의 기저라 하자. 그러면 $\mathcal{M}(T)$의 $k$번째 열은 $\mathcal{M}(Tv_k)$이다.

**3.76 선형사상은 행렬곱처럼 작용한다**

$T\in\mathcal{L}(V,W)$이고 $v\in V$라 하자. $V$와 $W$의 기저가 고정되어 있으면

$$
\mathcal{M}(Tv)=\mathcal{M}(T)\mathcal{M}(v).
$$

증명. $v=b_1v_1+\cdots+b_nv_n$이라 하면

$$
Tv=b_1Tv_1+\cdots+b_nTv_n.
$$

따라서

$$
\mathcal{M}(Tv) =b_1\mathcal{M}(Tv_1)+\cdots+b_n\mathcal{M}(Tv_n) =b_1\mathcal{M}(T)_{\cdot,1}+\cdots+b_n\mathcal{M}(T)_{\cdot,n} =\mathcal{M}(T)\mathcal{M}(v).
$$

**3.78 $\dim\text{range}T$는 $\mathcal{M}(T)$의 열계수와 같다**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
\dim\text{range}T = \text{$\mathcal{M}(T)$의 열계수}.
$$

### 기저변환

선형사상 $T\in\mathcal{L}(V)$에 대해 같은 기저를 정의역과 공역에 모두 사용할 때는

$$
\mathcal{M}(T,(v_1,\ldots,v_n)) = \mathcal{M}(T,(v_1,\ldots,v_n),(v_1,\ldots,v_n))
$$

처럼 쓴다.

**3.79 정의: 항등행렬 $I$**

대각성분이 모두 $1$이고 나머지 성분이 모두 $0$인 $n$행 $n$열 행렬을 항등행렬이라고 하며 $I$로 쓴다.

$$
I =
\begin{pmatrix}
1 & 0 & \cdots & 0\cr
0 & 1 & \cdots & 0\cr
\vdots & \vdots & \ddots & \vdots\cr
0 & 0 & \cdots & 1
\end{pmatrix}.
$$

**3.80 정의: 가역행렬, 역행렬**

정사각행렬 $A$에 대해 같은 크기의 정사각행렬 $B$가 존재하여

$$
AB=BA=I
$$

이면 $A$를 가역이라고 한다. 이때 $B$를 $A$의 역행렬이라고 하며 $A^{-1}$로 쓴다. 가역행렬을 nonsingular, 가역이 아닌 행렬을 singular라고도 한다.

가역행렬에 대해

$$
(A^{-1})^{-1}=A
$$

이고, 같은 크기의 가역행렬 $A,C$에 대해

$$
(AC)^{-1}=C^{-1}A^{-1}
$$

이다.

**3.81 선형사상 곱의 행렬**

$T\in\mathcal{L}(U,V)$이고 $S\in\mathcal{L}(V,W)$라 하자. $u_1,\ldots,u_m$이 $U$의 기저, $v_1,\ldots,v_n$이 $V$의 기저, $w_1,\ldots,w_p$가 $W$의 기저이면

$$
\mathcal{M}(ST,(u_1,\ldots,u_m),(w_1,\ldots,w_p)) =
\mathcal{M}(S,(v_1,\ldots,v_n),(w_1,\ldots,w_p))
\mathcal{M}(T,(u_1,\ldots,u_m),(v_1,\ldots,v_n)).
$$

**3.82 두 기저에 대한 항등연산자의 행렬**

$u_1,\ldots,u_n$과 $v_1,\ldots,v_n$이 $V$의 기저라고 하자. 그러면

$$
\mathcal{M}(I,(u_1,\ldots,u_n),(v_1,\ldots,v_n))
$$

과

$$
\mathcal{M}(I,(v_1,\ldots,v_n),(u_1,\ldots,u_n))
$$

은 서로의 역행렬이다.

**3.83 예**

$\mathbb{F}^2$의 기저 $(4,2),(5,3)$와 표준기저 $(1,0),(0,1)$에 대해

$$
\mathcal{M}(I,((4,2),(5,3)),((1,0),(0,1))) =
\begin{pmatrix} 4 & 5\cr 2 & 3 \end{pmatrix}.
$$

그 역행렬은

$$
\begin{pmatrix} \frac32 & -\frac52\cr -1 & 2 \end{pmatrix}
$$

이므로

$$
\mathcal{M}(I,((1,0),(0,1)),((4,2),(5,3))) =
\begin{pmatrix} \frac32 & -\frac52\cr -1 & 2 \end{pmatrix}.
$$

**3.84 기저변환 공식**

$T\in\mathcal{L}(V)$이고 $u_1,\ldots,u_n$과 $v_1,\ldots,v_n$이 $V$의 기저라고 하자.

$$
A = \mathcal{M}(T,(u_1,\ldots,u_n)),\qquad
B = \mathcal{M}(T,(v_1,\ldots,v_n)),
$$

그리고

$$
C=\mathcal{M}(I,(u_1,\ldots,u_n),(v_1,\ldots,v_n))
$$

라 하면

$$
A=C^{-1}BC.
$$

**3.86 역사상의 행렬은 행렬의 역이다**

$v_1,\ldots,v_n$이 $V$의 기저이고 $T\in\mathcal{L}(V)$가 가역이면

$$
\mathcal{M}(T^{-1})=(\mathcal{M}(T))^{-1}
$$

이다. 두 행렬은 모두 같은 기저 $v_1,\ldots,v_n$에 대해 계산한다.

### 연습문제 3D

1. $T\in\mathcal{L}(V,W)$가 가역이라고 하자. $T^{-1}$도 가역이고 $(T^{-1})^{-1}=T$임을 보여라.

2. $T\in\mathcal{L}(U,V)$와 $S\in\mathcal{L}(V,W)$가 모두 가역이면 $ST\in\mathcal{L}(U,W)$도 가역이고 $(ST)^{-1}=T^{-1}S^{-1}$임을 증명하라.

3. $V$가 유한차원이고 $T\in\mathcal{L}(V)$라 하자. 다음 조건들이 서로 동치임을 증명하라.

   (a) $T$는 가역이다.

   (b) $V$의 모든 기저 $v_1,\ldots,v_n$에 대해 $Tv_1,\ldots,Tv_n$은 $V$의 기저이다.

   (c) $V$의 어떤 기저 $v_1,\ldots,v_n$에 대해 $Tv_1,\ldots,Tv_n$은 $V$의 기저이다.

4. $V$가 유한차원이고 $\dim V>1$이라 하자. $V$에서 자기 자신으로 가는 가역이 아닌 선형사상들의 집합이 $\mathcal{L}(V)$의 부분공간이 아님을 증명하라.

5. $V$가 유한차원이고 $U$가 $V$의 부분공간이며 $S\in\mathcal{L}(U,V)$라 하자. 모든 $u\in U$에 대해 $Tu=Su$를 만족하는 가역 선형사상 $T:V\to V$가 존재할 필요충분조건은 $S$가 단사인 것임을 증명하라.

6. $W$가 유한차원이고 $S,T\in\mathcal{L}(V,W)$라 하자. $\text{null}S=\text{null}T$일 필요충분조건은 $S=ET$가 되도록 하는 가역 $E\in\mathcal{L}(W)$가 존재하는 것임을 증명하라.

7. $V$가 유한차원이고 $S,T\in\mathcal{L}(V,W)$라 하자. $\text{range}S=\text{range}T$일 필요충분조건은 $S=TE$가 되도록 하는 가역 $E\in\mathcal{L}(V)$가 존재하는 것임을 증명하라.

8. $V,W$가 유한차원이고 $S,T\in\mathcal{L}(V,W)$라 하자. 가역 $E_1\in\mathcal{L}(V)$와 $E_2\in\mathcal{L}(W)$가 존재하여 $S=E_2TE_1$가 될 필요충분조건은

   $$
   \dim\text{null}S=\dim\text{null}T
   $$

   임을 증명하라.

9. $V$가 유한차원이고 $T:V\to W$가 $W$ 위로의 전사 선형사상이라고 하자. $T|_U$가 $U$에서 $W$로의 동형사상이 되도록 하는 $V$의 부분공간 $U$가 존재함을 증명하라.

10. $V,W$가 유한차원이고 $U$가 $V$의 부분공간이라고 하자.

    $$
    \mathcal{E}=\lbrace T\in\mathcal{L}(V,W):U\subseteq\text{null}T\rbrace
    $$

    라고 둔다.

    (a) $\mathcal{E}$가 $\mathcal{L}(V,W)$의 부분공간임을 보여라.

    (b) $\dim V$, $\dim W$, $\dim U$로 $\dim\mathcal{E}$의 공식을 찾아라.

11. $V$가 유한차원이고 $S,T\in\mathcal{L}(V)$라 하자. 다음을 증명하라.

    $$
    ST\text{가 가역}
    \quad\Longleftrightarrow\quad
    S,T\text{가 모두 가역}.
    $$

12. $V$가 유한차원이고 $S,T,U\in\mathcal{L}(V)$이며 $STU=I$라 하자. $T$가 가역이고 $T^{-1}=US$임을 보여라.

13. 연습문제 12의 결론이 $V$가 유한차원이라는 가정 없이 실패할 수 있음을 보여라.

14. 참인지 증명하거나 반례를 들어라. $V$가 유한차원이고 $R,S,T\in\mathcal{L}(V)$이며 $RST$가 전사이면 $S$는 단사이다.

15. $T\in\mathcal{L}(V)$이고 $Tv_1,\ldots,Tv_m$이 $V$를 생성한다고 하자. 그러면 $v_1,\ldots,v_m$이 $V$를 생성함을 증명하라.

16. $\mathbb{F}^{n,1}$에서 $\mathbb{F}^{m,1}$로 가는 모든 선형사상은 행렬곱으로 주어짐을 증명하라. 즉 $T\in\mathcal{L}(\mathbb{F}^{n,1},\mathbb{F}^{m,1})$이면 어떤 $m$행 $n$열 행렬 $A$가 존재하여 모든 $x\in\mathbb{F}^{n,1}$에 대해 $Tx=Ax$임을 증명하라.

17. $V$가 유한차원이고 $S\in\mathcal{L}(V)$라 하자. $\mathcal{A}\in\mathcal{L}(\mathcal{L}(V))$를

    $$
    \mathcal{A}(T)=ST
    $$

    로 정의한다.

    (a) $\dim\text{null}\mathcal{A}=(\dim V)(\dim\text{null}S)$임을 보여라.

    (b) $\dim\text{range}\mathcal{A}=(\dim V)(\dim\text{range}S)$임을 보여라.

18. $V$와 $\mathcal{L}(\mathbb{F},V)$가 동형인 벡터공간임을 보여라.

19. $V$가 유한차원이고 $T\in\mathcal{L}(V)$라 하자. $T$가 $V$의 모든 기저에 대해 같은 행렬을 가질 필요충분조건은 $T$가 항등연산자의 스칼라배인 것임을 증명하라.

20. $q\in\mathcal{P}(\mathbb{R})$라 하자. 모든 $x\in\mathbb{R}$에 대해

    $$
    q(x)=(x^2+x)p''(x)+2xp'(x)+p(3)
    $$

    을 만족하는 $p\in\mathcal{P}(\mathbb{R})$가 존재함을 증명하라.

21. $n$이 양의 정수이고 모든 $j,k=1,\ldots,n$에 대해 $A_{j,k}\in\mathbb{F}$라 하자. 다음 두 조건이 동치임을 증명하라.

    (a) 동차계

    $$
    \sum_{k=1}^n A_{1,k}x_k=0,\quad
    \ldots,\quad
    \sum_{k=1}^n A_{n,k}x_k=0
    $$

    의 해는 자명한 해 $x_1=\cdots=x_n=0$뿐이다.

    (b) 모든 $c_1,\ldots,c_n\in\mathbb{F}$에 대해

    $$
    \sum_{k=1}^n A_{1,k}x_k=c_1,\quad
    \ldots,\quad
    \sum_{k=1}^n A_{n,k}x_k=c_n
    $$

    을 만족하는 해가 존재한다.

22. $T\in\mathcal{L}(V)$이고 $v_1,\ldots,v_n$이 $V$의 기저라고 하자. 다음을 증명하라.

    $$
    \mathcal{M}(T,(v_1,\ldots,v_n))\text{가 가역}
    \quad\Longleftrightarrow\quad
    T\text{가 가역}.
    $$

23. $u_1,\ldots,u_n$과 $v_1,\ldots,v_n$이 $V$의 기저라고 하자. $T\in\mathcal{L}(V)$가 각 $k=1,\ldots,n$에 대해 $Tv_k=u_k$를 만족하면

    $$
    \mathcal{M}(T,(v_1,\ldots,v_n)) =
    \mathcal{M}(I,(u_1,\ldots,u_n),(v_1,\ldots,v_n))
    $$

    임을 증명하라.

24. 같은 크기의 정사각행렬 $A,B$가 $AB=I$를 만족하면 $BA=I$임을 증명하라.

## 3E 벡터공간의 곱과 몫

### 곱공간

**3.87 정의: 곱공간**

$V_1,\ldots,V_m$이 벡터공간이면 곱공간

$$
V_1\times\cdots\times V_m
$$

은 모든 순서쌍 또는 순서 $m$-튜플 $(v_1,\ldots,v_m)$의 집합이다. 덧셈과 스칼라곱은 성분별로 정의한다.

$$
(u_1,\ldots,u_m)+(v_1,\ldots,v_m) = (u_1+v_1,\ldots,u_m+v_m),
$$

$$
\lambda(v_1,\ldots,v_m) = (\lambda v_1,\ldots,\lambda v_m).
$$

**3.88 예**

$\mathcal{P}_5(\mathbb{R})\times\mathbb{R}^3$에서

$$
(p,(x_1,x_2,x_3))+(q,(y_1,y_2,y_3)) = (p+q,(x_1+y_1,x_2+y_2,x_3+y_3))
$$

이고

$$
\lambda(p,(x_1,x_2,x_3)) = (\lambda p,(\lambda x_1,\lambda x_2,\lambda x_3)).
$$

**3.89 곱공간은 벡터공간이다**

$V_1,\ldots,V_m$이 $\mathbb{F}$ 위의 벡터공간이면 $V_1\times\cdots\times V_m$도 위 연산으로 $\mathbb{F}$ 위의 벡터공간이다.

**3.90 예**

$\mathbb{R}^2\times\mathbb{R}^3$은 $\mathbb{R}^5$와 같은 집합은 아니지만 동형이다. 예를 들어

$$
((x_1,x_2),(y_1,y_2,y_3)) \mapsto (x_1,x_2,y_1,y_2,y_3)
$$

는 동형사상이다.

**3.91 예: 곱공간의 기저**

다음 리스트는 $\mathcal{P}_2(\mathbb{R})\times\mathbb{R}^2$의 기저이다.

$$
(1,(0,0)),\quad
(x,(0,0)),\quad
(x^2,(0,0)),\quad
(0,(1,0)),\quad
(0,(0,1)).
$$

**3.92 곱공간의 차원**

$V_1,\ldots,V_m$이 유한차원이면

$$
\dim(V_1\times\cdots\times V_m) = \dim V_1+\cdots+\dim V_m.
$$

**3.93 곱공간과 직합**

$V_1,\ldots,V_m$이 같은 벡터공간의 부분공간이라고 하자. 선형사상

$$
\Gamma:V_1\times\cdots\times V_m\to V_1+\cdots+V_m
$$

을

$$
\Gamma(v_1,\ldots,v_m)=v_1+\cdots+v_m
$$

로 정의한다. 그러면

$$
V_1+\cdots+V_m\text{이 직합} \quad\Longleftrightarrow\quad \Gamma\text{가 단사}.
$$

**3.94 직합의 차원 조건**

$V_1,\ldots,V_m$이 유한차원인 부분공간이면

$$
V_1+\cdots+V_m\text{이 직합} \quad\Longleftrightarrow\quad \dim(V_1+\cdots+V_m)=\dim V_1+\cdots+\dim V_m.
$$

### 몫공간

**3.95 표기: $v+U$**

$U$가 $V$의 부분공간이고 $v\in V$이면

$$
v+U=\lbrace v+u:u\in U\rbrace
$$

라고 쓴다. 이를 $U$의 평행이동이라고 한다.

**3.96 예**

$U=\lbrace(x,2x):x\in\mathbb{R}\rbrace$가 $\mathbb{R}^2$의 직선이라고 하자. 그러면 $(17,20)+U$는 $(17,20)$을 지나고 기울기가 $2$인 직선이다.

**3.97 정의: 평행이동**

부분공간 $U$와 벡터 $v$에 대해 $v+U$를 $U$의 평행이동이라고 부른다.

**3.98 예**

$\mathbb{R}^2$에서 원점을 지나는 직선의 평행이동은 그 직선과 평행인 직선이다. $\mathbb{R}^3$에서 원점을 지나는 평면의 평행이동은 그 평면과 평행인 평면이다.

**3.99 정의: 몫공간 $V/U$**

$U$가 $V$의 부분공간일 때

$$
V/U=\lbrace v+U:v\in V\rbrace
$$

를 $V$의 $U$에 의한 몫공간이라고 한다.

**3.100 예**

- $V/\lbrace0\rbrace$는 $V$와 자연스럽게 같은 정보를 가진다.
- $V/V$는 하나의 원소만 가진다.
- $\mathbb{R}^2$를 원점을 지나는 직선 $U$로 나눈 몫공간은 그 직선과 평행한 모든 직선들의 집합이다.

**3.101 두 평행이동은 같거나 서로소이다**

$U$가 $V$의 부분공간이고 $v,w\in V$라 하자. 그러면 다음 조건들이 서로 동치이다.

$$
v-w\in U, \qquad v+U=w+U, \qquad (v+U)\cap(w+U)\ne\varnothing.
$$

증명. $v-w\in U$이면 $v+U=w+U$이다. 두 집합이 같으면 교집합은 비어 있지 않다. 반대로 교집합에 어떤 원소가 있으면 $v+u_1=w+u_2$인 $u_1,u_2\in U$가 존재하고, 따라서 $v-w=u_2-u_1\in U$이다.

**3.102 몫공간의 덧셈과 스칼라곱**

$V/U$에서

$$
(v+U)+(w+U)=(v+w)+U,
$$

$$
\lambda(v+U)=(\lambda v)+U
$$

로 정의한다.

**3.103 몫공간은 벡터공간이다**

$U$가 $V$의 부분공간이면 $V/U$는 3.102의 연산으로 벡터공간이다. 3.101은 위 연산들이 대표원 선택에 의존하지 않음을 보장한다.

**3.104 정의: 몫사상**

$U$가 $V$의 부분공간일 때 몫사상 $\pi:V\to V/U$를

$$
\pi(v)=v+U
$$

로 정의한다. 이 사상은 선형이고 전사이다.

**3.105 몫공간의 차원**

$V$가 유한차원이고 $U$가 $V$의 부분공간이면

$$
\dim V/U=\dim V-\dim U.
$$

증명. 몫사상 $\pi$의 영공간은 $U$이고 치역은 $V/U$이다. 선형사상의 기본정리를 $\pi$에 적용하면 결론이 나온다.

**3.106 표기: $\widetilde{T}$**

$T\in\mathcal{L}(V,W)$라 하자. $\text{null}T$에 의한 몫공간에서 $W$로 가는 사상

$$
\widetilde{T}:V/\text{null}T\to W
$$

를

$$
\widetilde{T}(v+\text{null}T)=Tv
$$

로 정의한다.

**3.107 $\widetilde{T}$의 영공간과 치역**

$T\in\mathcal{L}(V,W)$이고 $\pi$가 $V$에서 $V/\text{null}T$로 가는 몫사상이라고 하자. 그러면 다음이 성립한다.

(a) $\widetilde{T}\circ\pi=T$.

(b) $\widetilde{T}$는 단사이다.

(c) $\text{range}\widetilde{T}=\text{range}T$.

(d) $V/\text{null}T$와 $\text{range}T$는 동형이다.

증명. (a)는 정의에서 바로 나온다. (b)는 $\widetilde{T}(v+\text{null}T)=0$이면 $Tv=0$이고, 따라서 $v\in\text{null}T$이므로 $v+\text{null}T=\text{null}T$라는 사실에서 따른다. (c)도 정의에서 바로 나오며, (b)와 (c)가 (d)를 준다.

### 연습문제 3E

1. 함수 $T:V\to W$의 그래프를

   $$
   \text{graph}T=\lbrace(v,Tv)\in V\times W:v\in V\rbrace
   $$

   로 정의한다. $T$가 선형사상일 필요충분조건은 $\text{graph}T$가 $V\times W$의 부분공간인 것임을 증명하라.

2. $V_1,\ldots,V_m$이 벡터공간이고 $V_1\times\cdots\times V_m$이 유한차원이라고 하자. 각 $k=1,\ldots,m$에 대해 $V_k$가 유한차원임을 증명하라.

3. $V_1,\ldots,V_m$이 벡터공간이라고 하자. $\mathcal{L}(V_1\times\cdots\times V_m,W)$와

   $$
   \mathcal{L}(V_1,W)\times\cdots\times\mathcal{L}(V_m,W)
   $$

   가 동형인 벡터공간임을 증명하라.

4. $W_1,\ldots,W_m$이 벡터공간이라고 하자. $\mathcal{L}(V,W_1\times\cdots\times W_m)$와

   $$
   \mathcal{L}(V,W_1)\times\cdots\times\mathcal{L}(V,W_m)
   $$

   가 동형인 벡터공간임을 증명하라.

5. 양의 정수 $m$에 대해

   $$
   V^m=\underbrace{V\times\cdots\times V}_{m\text{번}}
   $$

   라고 정의한다. $V^m$과 $\mathcal{L}(\mathbb{F}^m,V)$가 동형임을 증명하라.

6. $v,x\in V$이고 $U,W$가 $V$의 부분공간이며 $v+U=x+W$라고 하자. $U=W$임을 증명하라.

7. $U=\lbrace(x,y,z)\in\mathbb{R}^3:2x+3y+5z=0\rbrace$라 하자. $A\subseteq\mathbb{R}^3$에 대해 $A$가 $U$의 평행이동일 필요충분조건은 어떤 $c\in\mathbb{R}$가 존재하여

   $$
   A=\lbrace(x,y,z)\in\mathbb{R}^3:2x+3y+5z=c\rbrace
   $$

   가 되는 것임을 증명하라.

8. (a) $T\in\mathcal{L}(V,W)$이고 $c\in W$라 하자. $\lbrace x\in V:Tx=c\rbrace$는 공집합이거나 $\text{null}T$의 평행이동임을 증명하라.

   (b) 3.27과 같은 선형방정식계의 해집합은 공집합이거나 $\mathbb{F}^n$의 어떤 부분공간의 평행이동임을 설명하라.

9. $V$의 공집합이 아닌 부분집합 $A$가 어떤 부분공간의 평행이동일 필요충분조건은 모든 $v,w\in A$와 모든 $\lambda\in\mathbb{F}$에 대해

   $$
   \lambda v+(1-\lambda)w\in A
   $$

   가 성립하는 것임을 증명하라.

10. $A_1=v+U_1$, $A_2=w+U_2$라고 하자. 여기서 $v,w\in V$이고 $U_1,U_2$는 $V$의 부분공간이다. $A_1\cap A_2$는 공집합이거나 $V$의 어떤 부분공간의 평행이동임을 증명하라.

11. $U=\lbrace(x_1,x_2,\ldots)\in\mathbb{F}^{\infty}:x_k\ne0\text{인 }k\text{가 유한 개뿐}\rbrace$라고 하자.

    (a) $U$가 $\mathbb{F}^{\infty}$의 부분공간임을 보여라.

    (b) $\mathbb{F}^{\infty}/U$가 무한차원임을 증명하라.

12. $v_1,\ldots,v_m\in V$라 하자.

    $$
    A=\lbrace\lambda_1v_1+\cdots+\lambda_mv_m:\lambda_1,\ldots,\lambda_m\in\mathbb{F},\ \lambda_1+\cdots+\lambda_m=1\rbrace
    $$

    라고 둔다.

    (a) $A$가 $V$의 어떤 부분공간의 평행이동임을 증명하라.

    (b) $B$가 $V$의 어떤 부분공간의 평행이동이고 $\lbrace v_1,\ldots,v_m\rbrace\subseteq B$이면 $A\subseteq B$임을 증명하라.

    (c) $A$가 차원이 $m$보다 작은 어떤 부분공간의 평행이동임을 증명하라.

13. $U$가 $V$의 부분공간이고 $V/U$가 유한차원이라고 하자. $V$가 $U\times(V/U)$와 동형임을 증명하라.

14. $U,W$가 $V$의 부분공간이고 $V=U\oplus W$라 하자. $w_1,\ldots,w_m$이 $W$의 기저이면 $w_1+U,\ldots,w_m+U$가 $V/U$의 기저임을 증명하라.

15. $U$가 $V$의 부분공간이고 $v_1+U,\ldots,v_m+U$가 $V/U$의 기저이며 $u_1,\ldots,u_n$이 $U$의 기저라고 하자. 그러면 $v_1,\ldots,v_m,u_1,\ldots,u_n$이 $V$의 기저임을 증명하라.

16. $\varphi\in\mathcal{L}(V,\mathbb{F})$이고 $\varphi\ne0$라 하자. 다음을 증명하라.

    $$
    \dim V/\text{null}\varphi=1.
    $$

17. $U$가 $V$의 부분공간이고 $\dim V/U=1$이라 하자. $\text{null}\varphi=U$가 되도록 하는 $\varphi\in\mathcal{L}(V,\mathbb{F})$가 존재함을 증명하라.

18. $U$가 $V$의 부분공간이고 $V/U$가 유한차원이라고 하자.

    (a) $W$가 $V$의 유한차원 부분공간이고 $V=U+W$이면 $\dim W\ge\dim V/U$임을 보여라.

    (b) $\dim W=\dim V/U$이고 $V=U\oplus W$가 되도록 하는 $V$의 유한차원 부분공간 $W$가 존재함을 증명하라.

19. $T\in\mathcal{L}(V,W)$이고 $U$가 $V$의 부분공간이라고 하자. $\pi$를 $V$에서 $V/U$로 가는 몫사상이라 하자. $T=S\circ\pi$가 되도록 하는 $S\in\mathcal{L}(V/U,W)$가 존재할 필요충분조건은 $U\subseteq\text{null}T$임을 증명하라.

## 3F 쌍대성

### 쌍대공간과 쌍대사상

스칼라체 $\mathbb{F}$로 가는 선형사상은 선형대수에서 특별한 역할을 하므로 별도의 이름을 가진다.

**3.108 정의: 선형함수**

$V$ 위의 **선형함수**는 $V$에서 $\mathbb{F}$로 가는 선형사상이다. 즉 선형함수는 $\mathcal{L}(V,\mathbb{F})$의 원소이다.

**3.109 예: 선형함수**

- $\varphi:\mathbb{R}^3\to\mathbb{R}$를

  $$
  \varphi(x,y,z)=4x-5y+2z
  $$

  로 정의하면 $\varphi$는 $\mathbb{R}^3$ 위의 선형함수이다.

- $(c_1,\ldots,c_n)\in\mathbb{F}^n$를 고정하고

  $$
  \varphi(x_1,\ldots,x_n)=c_1x_1+\cdots+c_nx_n
  $$

  로 정의하면 $\varphi:\mathbb{F}^n\to\mathbb{F}$는 선형함수이다.

- $\varphi:\mathcal{P}(\mathbb{R})\to\mathbb{R}$를

  $$
  \varphi(p)=3p''(5)+7p(4)
  $$

  로 정의하면 선형함수이다.

- $\varphi:\mathcal{P}(\mathbb{R})\to\mathbb{R}$를

  $$
  \varphi(p)=\int_0^1 p
  $$

  로 정의하면 선형함수이다.

**3.110 정의: 쌍대공간 $V'$**

$V$의 **쌍대공간**은 $V$ 위의 모든 선형함수들의 벡터공간이며 $V'$로 쓴다. 즉

$$
V'=\mathcal{L}(V,\mathbb{F}).
$$

**3.111 $\dim V'=\dim V$**

$V$가 유한차원이면 $V'$도 유한차원이고

$$
\dim V'=\dim V.
$$

증명. 3.72에 의해

$$
\dim V' =\dim\mathcal{L}(V,\mathbb{F}) =(\dim V)(\dim\mathbb{F}) =\dim V.
$$

**3.112 정의: 쌍대기저**

$v_1,\ldots,v_n$이 $V$의 기저라고 하자. 이 기저의 **쌍대기저**는 $V'$의 원소 $\varphi_1,\ldots,\varphi_n$의 리스트로, 각 $\varphi_j$는 다음을 만족하는 선형함수이다.

$$
\varphi_j(v_k)= \begin{cases} 1, & k=j,\cr 0, & k\ne j. \end{cases}
$$

**3.113 예: $\mathbb{F}^n$의 표준기저의 쌍대기저**

$1\le j\le n$에 대해 $\varphi_j:\mathbb{F}^n\to\mathbb{F}$를 $j$번째 좌표를 뽑는 함수로 정의하자.

$$
\varphi_j(x_1,\ldots,x_n)=x_j.
$$

$e_1,\ldots,e_n$이 표준기저이면

$$
\varphi_j(e_k)=
\begin{cases}
1, & k=j,\cr
0, & k\ne j.
\end{cases}
$$

따라서 $\varphi_1,\ldots,\varphi_n$은 표준기저의 쌍대기저이다.

**3.114 쌍대기저는 선형결합의 계수를 준다**

$v_1,\ldots,v_n$이 $V$의 기저이고 $\varphi_1,\ldots,\varphi_n$이 그 쌍대기저라 하자. 그러면 모든 $v\in V$에 대해

$$
v=\varphi_1(v)v_1+\cdots+\varphi_n(v)v_n.
$$

증명. $v=c_1v_1+\cdots+c_nv_n$이라 쓰고 양변에 $\varphi_j$를 적용하면 $\varphi_j(v)=c_j$이다.

**3.116 쌍대기저는 쌍대공간의 기저이다**

$V$가 유한차원이라고 하자. $V$의 한 기저의 쌍대기저는 $V'$의 기저이다.

증명. $v_1,\ldots,v_n$의 쌍대기저를 $\varphi_1,\ldots,\varphi_n$이라 하자. 만약

$$
a_1\varphi_1+\cdots+a_n\varphi_n=0
$$

이면 양변을 $v_k$에 적용하여 $a_k=0$을 얻는다. 따라서 쌍대기저는 선형독립이다. 길이가 $\dim V'=\dim V=n$이므로 $V'$의 기저이다.

**3.118 정의: 쌍대사상 $T'$**

$T\in\mathcal{L}(V,W)$라 하자. $T$의 **쌍대사상**은 $T'\in\mathcal{L}(W',V')$로, 각 $\varphi\in W'$에 대해

$$
T'(\varphi)=\varphi\circ T
$$

로 정의된다.

$T'$는 $W'$에서 $V'$로 간다는 점에 주의하라. 방향이 $T$와 반대로 바뀐다.

**3.119 예: 미분사상의 쌍대사상**

$D:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$를 $Dp=p'$로 정의하자.

- $\varphi(p)=p(3)$이면

  $$
  (D'(\varphi))(p)=(\varphi\circ D)(p)=\varphi(p')=p'(3).
  $$

- $\varphi(p) = \int_0^1 p$이면

  $$
  (D'(\varphi))(p) = \int_0^1 p' = p(1)-p(0).
  $$

**3.120 쌍대사상의 대수적 성질**

$T\in\mathcal{L}(V,W)$라 하자. 그러면 다음이 성립한다.

(a) 모든 $S\in\mathcal{L}(V,W)$에 대해

$$
(S+T)'=S'+T'.
$$

(b) 모든 $\lambda\in\mathbb{F}$에 대해

$$
(\lambda T)'=\lambda T'.
$$

(c) 모든 $S\in\mathcal{L}(W,U)$에 대해

$$
(ST)'=T'S'.
$$

증명. (a), (b)는 정의에서 바로 따른다. (c)는 $\varphi\in U'$에 대해

$$
(ST)'(\varphi)
=\varphi\circ(ST)
=(\varphi\circ S)\circ T
=T'(S'(\varphi))
=(T'S')(\varphi)
$$

이므로 성립한다. 합성 순서가 뒤집힌다는 점이 중요하다.

일부 책은 쌍대공간과 쌍대사상에 $V^*$와 $T^*$를 쓰지만, 여기서는 이후 내적공간에서 도입할 수반(adjoint)을 위해 $T^*$ 표기를 남겨 둔다.

### 쌍대사상의 영공간과 치역

**3.121 정의: 소멸자 $U^0$**

$U\subseteq V$에 대해 $U$의 **소멸자**는

$$
U^0=\lbrace\varphi\in V':\text{모든 }u\in U\text{에 대해 }\varphi(u)=0\rbrace
$$

로 정의된다.

**3.122 예**

$U$가 $\mathcal{P}(\mathbb{R})$에서 $x^2$의 다항식배들로 이루어진 부분공간이라고 하자. $\varphi(p)=p'(0)$이면 모든 $u\in U$에 대해 $\varphi(u)=0$이므로 $\varphi\in U^0$이다.

**3.123 예: $\mathbb{R}^5$의 2차원 부분공간의 소멸자**

$e_1,\ldots,e_5$를 $\mathbb{R}^5$의 표준기저라 하고, $\varphi_1,\ldots,\varphi_5$를 그 쌍대기저라 하자.

$$
U=\text{span}(e_1,e_2) = \lbrace(x_1,x_2,0,0,0)\in\mathbb{R}^5:x_1,x_2\in\mathbb{R}\rbrace
$$

이면

$$
U^0=\text{span}(\varphi_3,\varphi_4,\varphi_5).
$$

실제로 $\varphi_3,\varphi_4,\varphi_5$의 선형결합은 $U$의 모든 벡터에서 $0$이 된다. 반대로 $\varphi\in U^0$이고

$$
\varphi=c_1\varphi_1+\cdots+c_5\varphi_5
$$

라 쓰면 $\varphi(e_1)=0$, $\varphi(e_2)=0$이므로 $c_1=c_2=0$이다.

**3.124 소멸자는 부분공간이다**

$U\subseteq V$이면 $U^0$는 $V'$의 부분공간이다.

증명. 영선형함수는 $U^0$에 속한다. $\varphi,\psi\in U^0$이면 모든 $u\in U$에 대해

$$
(\varphi+\psi)(u)=\varphi(u)+\psi(u)=0
$$

이고, 스칼라배에 대해서도 같은 방식으로 닫혀 있다.

**3.125 소멸자의 차원**

$V$가 유한차원이고 $U$가 $V$의 부분공간이면

$$
\dim U^0=\dim V-\dim U.
$$

증명. 포함사상 $i:U\to V$를 $i(u)=u$로 정의하자. 그러면 $i':V'\to U'$이다. 선형사상의 기본정리에 의해

$$
\dim\text{range}i'+\dim\text{null}i'=\dim V'.
$$

여기서 $\text{null}i'=U^0$이고 $\dim V'=\dim V$이다. 또한 $U$ 위의 모든 선형함수는 $V$ 위의 선형함수로 확장될 수 있으므로 $\text{range}i'=U'$이다. 따라서

$$
\dim U+\dim U^0=\dim V.
$$

**3.127 소멸자가 $\lbrace0\rbrace$ 또는 전체 공간이 되는 조건**

$V$가 유한차원이고 $U$가 $V$의 부분공간이면 다음이 성립한다.

(a) $U^0=\lbrace0\rbrace$일 필요충분조건은 $U=V$이다.

(b) $U^0=V'$일 필요충분조건은 $U=\lbrace0\rbrace$이다.

증명. (a)는 $\dim U^0=0 \Longleftrightarrow \dim U=\dim V$와 동치이고, (b)는 $\dim U^0=\dim V' \Longleftrightarrow \dim U=0$과 동치이다.

**3.128 $T'$의 영공간**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

(a)

$$
\text{null}T'=(\text{range}T)^0.
$$

(b)

$$
\dim\text{null}T' = \dim\text{null}T+\dim W-\dim V.
$$

증명. (a) $\varphi\in\text{null}T'$이면 $\varphi\circ T=0$이므로 $\varphi$는 $\text{range}T$의 모든 벡터에서 $0$이 된다. 따라서 $\varphi\in(\text{range}T)^0$이다. 반대 포함도 같은 문장을 거꾸로 읽으면 된다.

(b)

$$
\dim\text{null}T' =\dim(\text{range}T)^0 =\dim W-\dim\text{range}T =\dim W-(\dim V-\dim\text{null}T).
$$

**3.129 $T$가 전사 $\Longleftrightarrow$ $T'$가 단사**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
T\text{가 전사}
\quad\Longleftrightarrow\quad
T'\text{가 단사}.
$$

증명.

$$
T\text{ 전사}
\Longleftrightarrow
\text{range}T=W
\Longleftrightarrow
(\text{range}T)^0=\lbrace0\rbrace
\Longleftrightarrow
\text{null}T'=\lbrace0\rbrace.
$$

**3.130 $T'$의 치역**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

(a)

$$
\dim\text{range}T'=\dim\text{range}T.
$$

(b)

$$
\text{range}T'=(\text{null}T)^0.
$$

증명. (a)는 기본정리와 3.128에서 바로 나온다.

(b) 먼저 $\varphi=T'(\psi)$라 하자. $v\in\text{null}T$이면

$$
\varphi(v)=(T'\psi)(v)=(\psi\circ T)(v)=\psi(0)=0
$$

이므로 $\text{range}T'\subseteq(\text{null}T)^0$이다. 두 공간의 차원은

$$
\dim\text{range}T'
=\dim\text{range}T
=\dim V-\dim\text{null}T
=\dim(\text{null}T)^0
$$

으로 같으므로 등호가 성립한다.

**3.131 $T$가 단사 $\Longleftrightarrow$ $T'$가 전사**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
T\text{가 단사}
\quad\Longleftrightarrow\quad
T'\text{가 전사}.
$$

증명.

$$
T\text{ 단사}
\Longleftrightarrow
\text{null}T=\lbrace0\rbrace
\Longleftrightarrow
(\text{null}T)^0=V'
\Longleftrightarrow
\text{range}T'=V'.
$$

### 쌍대사상의 행렬

$v_1,\ldots,v_n$을 $V$의 기저, $\varphi_1,\ldots,\varphi_n$을 그 쌍대기저라고 하자. 또한 $w_1,\ldots,w_m$을 $W$의 기저, $\psi_1,\ldots,\psi_m$을 그 쌍대기저라고 하자. 이 기저들에 대해 $T$와 $T'$의 행렬을 계산하면 다음 결과가 나온다.

**3.132 $T'$의 행렬은 $T$의 행렬의 전치이다**

$V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 그러면

$$
\mathcal{M}(T')=(\mathcal{M}(T))^t.
$$

증명. $A=\mathcal{M}(T)$, $C=\mathcal{M}(T')$라고 하자. 정의에 의해

$$
T'(\psi_j)=\sum_{r=1}^n C_{r,j}\varphi_r.
$$

양변을 $v_k$에 적용하면 왼쪽은 $(\psi_j\circ T)(v_k)$이고 오른쪽은 $C_{k,j}$이다. 한편

$$
(\psi_j\circ T)(v_k) =\psi_j(Tv_k) =\psi_j\left(\sum_{r=1}^m A_{r,k}w_r\right) =A_{j,k}.
$$

따라서 $C_{k,j}=A_{j,k}$이고 $C=A^t$이다.

**3.133 열계수는 행계수와 같다**

$A\in\mathbb{F}^{m,n}$라 하자. 그러면 $A$의 열계수는 $A$의 행계수와 같다.

증명. $T:\mathbb{F}^{n,1}\to\mathbb{F}^{m,1}$를 $Tx=Ax$로 정의한다. 표준기저에 대해 $\mathcal{M}(T)=A$이다. 그러면

$$
\text{$A$의 열계수} =\dim\text{range}T =\dim\text{range}T' =\text{$\mathcal{M}(T')$의 열계수} =\text{$A^t$의 열계수} =\text{$A$의 행계수}.
$$

### 연습문제 3F

1. 모든 선형함수가 전사이거나 영사상인 이유를 설명하라.

2. $\mathbb{R}^{[0,1]}$ 위의 서로 다른 세 선형함수의 예를 들어라.

3. $V$가 유한차원이고 $v\in V$, $v\ne0$라 하자. $\varphi(v)=1$인 $\varphi\in V'$가 존재함을 증명하라.

4. $V$가 유한차원이고 $U$가 $V$의 진부분공간이라고 하자. 모든 $u\in U$에 대해 $\varphi(u)=0$이지만 $\varphi\ne0$인 $\varphi\in V'$가 존재함을 증명하라.

5. $T\in\mathcal{L}(V,W)$이고 $w_1,\ldots,w_m$이 $\text{range}T$의 기저라고 하자. 각 $v\in V$에 대해

   $$
   Tv=\varphi_1(v)w_1+\cdots+\varphi_m(v)w_m
   $$

   가 되는 유일한 수 $\varphi_1(v),\ldots,\varphi_m(v)$가 존재하여 함수 $\varphi_1,\ldots,\varphi_m:V\to\mathbb{F}$를 정의한다. 각 $\varphi_j$가 $V$ 위의 선형함수임을 보여라.

6. $\varphi,\beta\in V'$라 하자. $\text{null}\varphi\subseteq\text{null}\beta$일 필요충분조건은 $\beta=c\varphi$가 되도록 하는 $c\in\mathbb{F}$가 존재하는 것임을 증명하라.

7. $V_1,\ldots,V_m$이 벡터공간이라고 하자. $(V_1\times\cdots\times V_m)'$와 $V_1'\times\cdots\times V_m'$가 동형인 벡터공간임을 증명하라.

8. $v_1,\ldots,v_n$이 $V$의 기저이고 $\varphi_1,\ldots,\varphi_n$이 $V'$의 쌍대기저라고 하자. $\Gamma:V\to\mathbb{F}^n$와 $\Lambda:\mathbb{F}^n\to V$를

   $$
   \Gamma(v)=(\varphi_1(v),\ldots,\varphi_n(v)),
   \qquad
   \Lambda(a_1,\ldots,a_n)=a_1v_1+\cdots+a_nv_n
   $$

   로 정의한다. $\Gamma$와 $\Lambda$가 서로의 역임을 설명하라.

9. $m$이 양의 정수라고 하자. $\mathcal{P}_m(\mathbb{R})$의 기저 $1,x,\ldots,x^m$의 쌍대기저가 $\varphi_0,\varphi_1,\ldots,\varphi_m$이며

   $$
   \varphi_k(p)=\frac{p^{(k)}(0)}{k!}
   $$

   임을 보여라. 여기서 $p^{(k)}$는 $p$의 $k$번째 도함수이고, $0$번째 도함수는 $p$ 자신으로 이해한다.

10. $m$이 양의 정수라고 하자.

    (a) $1,x-5,\ldots,(x-5)^m$이 $\mathcal{P}_m(\mathbb{R})$의 기저임을 보여라.

    (b) (a)의 기저의 쌍대기저는 무엇인가?

11. $v_1,\ldots,v_n$이 $V$의 기저이고 $\varphi_1,\ldots,\varphi_n$이 대응하는 $V'$의 쌍대기저라고 하자. $\psi\in V'$이면

    $$
    \psi=\psi(v_1)\varphi_1+\cdots+\psi(v_n)\varphi_n
    $$

    임을 증명하라.

12. $S,T\in\mathcal{L}(V,W)$라 하자.

    (a) $(S+T)'=S'+T'$임을 증명하라.

    (b) 모든 $\lambda\in\mathbb{F}$에 대해 $(\lambda T)'=\lambda T'$임을 증명하라.

13. $V$ 위의 항등연산자의 쌍대사상이 $V'$ 위의 항등연산자임을 보여라.

14. $T:\mathbb{R}^3\to\mathbb{R}^2$를

    $$
    T(x,y,z)=(4x+5y+6z,\thickspace7x+8y+9z)
    $$

    로 정의한다. $\varphi_1,\varphi_2$를 $\mathbb{R}^2$의 표준기저의 쌍대기저, $\psi_1,\psi_2,\psi_3$를 $\mathbb{R}^3$의 표준기저의 쌍대기저라고 하자.

    (a) 선형함수 $T'(\varphi_1)$와 $T'(\varphi_2)$를 설명하라.

    (b) $T'(\varphi_1)$와 $T'(\varphi_2)$를 $\psi_1,\psi_2,\psi_3$의 선형결합으로 써라.

15. $T:\mathcal{P}(\mathbb{R})\to\mathcal{P}(\mathbb{R})$를 각 $x\in\mathbb{R}$에 대해

    $$
    (Tp)(x)=x^2p(x)+p''(x)
    $$

    로 정의한다.

    (a) $\varphi\in\mathcal{P}(\mathbb{R})'$가 $\varphi(p)=p'(4)$로 정의되었다고 하자. $\mathcal{P}(\mathbb{R})$ 위의 선형함수 $T'(\varphi)$를 설명하라.

    (b) $\varphi\in\mathcal{P}(\mathbb{R})'$가 $\varphi(p)=\int_0^1p$로 정의되었다고 하자. $(T'(\varphi))(x^3)$을 계산하라.

16. $W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. 다음을 증명하라.

    $$
    T'=0 \quad\Longleftrightarrow\quad T=0.
    $$

17. $V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자. $T$가 가역일 필요충분조건은 $T'\in\mathcal{L}(W',V')$가 가역인 것임을 증명하라.

18. $V,W$가 유한차원이라고 하자. $T\in\mathcal{L}(V,W)$를 $T'\in\mathcal{L}(W',V')$로 보내는 사상이 $\mathcal{L}(V,W)$에서 $\mathcal{L}(W',V')$ 위로의 동형사상임을 증명하라.

19. $U\subseteq V$라 하자. 다음 등식이 성립하는 이유를 설명하라.

    $$
    U^0=\lbrace\varphi\in V':U\subseteq\text{null}\varphi\rbrace.
    $$

20. $V$가 유한차원이고 $U$가 $V$의 부분공간이라고 하자. 다음을 보여라.

    $$
    U=\lbrace v\in V:\text{모든 }\varphi\in U^0\text{에 대해 }\varphi(v)=0\rbrace.
    $$

21. $V$가 유한차원이고 $U,W$가 $V$의 부분공간이라고 하자.

    (a) $W^0\subseteq U^0$일 필요충분조건은 $U\subseteq W$임을 증명하라.

    (b) $W^0=U^0$일 필요충분조건은 $U=W$임을 증명하라.

22. $V$가 유한차원이고 $U,W$가 $V$의 부분공간이라고 하자.

    (a) $(U+W)^0=U^0\cap W^0$임을 보여라.

    (b) $(U\cap W)^0=U^0+W^0$임을 보여라.

23. $V$가 유한차원이고 $\varphi_1,\ldots,\varphi_m\in V'$라 하자. 다음 세 집합이 서로 같음을 증명하라.

    (a) $\text{span}(\varphi_1,\ldots,\varphi_m)$

    (b) $((\text{null}\varphi_1)\cap\cdots\cap(\text{null}\varphi_m))^0$

    (c) $\lbrace\varphi\in V':(\text{null}\varphi_1)\cap\cdots\cap(\text{null}\varphi_m)\subseteq\text{null}\varphi\rbrace$

24. $V$가 유한차원이고 $v_1,\ldots,v_m\in V$라 하자. 선형사상 $\Gamma:V'\to\mathbb{F}^m$를

    $$
    \Gamma(\varphi)=(\varphi(v_1),\ldots,\varphi(v_m))
    $$

    로 정의한다.

    (a) $v_1,\ldots,v_m$이 $V$를 생성할 필요충분조건은 $\Gamma$가 단사인 것임을 증명하라.

    (b) $v_1,\ldots,v_m$이 선형독립일 필요충분조건은 $\Gamma$가 전사인 것임을 증명하라.

25. $V$가 유한차원이고 $\varphi_1,\ldots,\varphi_m\in V'$라 하자. 선형사상 $\Gamma:V\to\mathbb{F}^m$를

    $$
    \Gamma(v)=(\varphi_1(v),\ldots,\varphi_m(v))
    $$

    로 정의한다.

    (a) $\varphi_1,\ldots,\varphi_m$이 $V'$를 생성할 필요충분조건은 $\Gamma$가 단사인 것임을 증명하라.

    (b) $\varphi_1,\ldots,\varphi_m$이 선형독립일 필요충분조건은 $\Gamma$가 전사인 것임을 증명하라.

26. $V$가 유한차원이고 $\Omega$가 $V'$의 부분공간이라고 하자. 다음을 증명하라.

    $$
    \Omega=\lbrace v\in V:\text{모든 }\varphi\in\Omega\text{에 대해 }\varphi(v)=0\rbrace^0.
    $$

27. $T\in\mathcal{L}(\mathcal{P}_5(\mathbb{R}))$이고 $\text{null}T'=\text{span}(\varphi)$라고 하자. 여기서 $\varphi$는 $\varphi(p)=p(8)$로 정의된 $\mathcal{P}_5(\mathbb{R})$ 위의 선형함수이다. 다음을 증명하라.

    $$
    \text{range}T = \lbrace p\in\mathcal{P}_5(\mathbb{R}):p(8)=0\rbrace.
    $$

28. $V$가 유한차원이고 $\varphi_1,\ldots,\varphi_m$이 $V'$에서 선형독립인 리스트라고 하자. 다음을 증명하라.

    $$
    \dim((\text{null}\varphi_1)\cap\cdots\cap(\text{null}\varphi_m)) = (\dim V)-m.
    $$

29. $V,W$가 유한차원이고 $T\in\mathcal{L}(V,W)$라 하자.

    (a) $\varphi\in W'$이고 $\text{null}T'=\text{span}(\varphi)$이면 $\text{range}T=\text{null}\varphi$임을 증명하라.

    (b) $\psi\in V'$이고 $\text{range}T'=\text{span}(\psi)$이면 $\text{null}T=\text{null}\psi$임을 증명하라.

30. $V$가 유한차원이고 $\varphi_1,\ldots,\varphi_n$이 $V'$의 기저라고 하자. 이들의 쌍대기저가 $\varphi_1,\ldots,\varphi_n$이 되는 $V$의 기저가 존재함을 보여라.

31. $U$가 $V$의 부분공간이라고 하자. 포함사상 $i:U\to V$를 $i(u)=u$로 정의한다. 그러면 $i'\in\mathcal{L}(V',U')$이다.

    (a) $\text{null}i'=U^0$임을 보여라.

    (b) $V$가 유한차원이면 $\text{range}i'=U'$임을 증명하라.

    (c) $V$가 유한차원이면 $\widetilde{i'}$가 $V'/U^0$에서 $U'$ 위로의 동형사상임을 증명하라.

32. $V$의 이중쌍대공간을 $V''=(V')'$로 정의한다. $\Lambda:V\to V''$를 각 $v\in V$와 $\varphi\in V'$에 대해

    $$
    (\Lambda v)(\varphi)=\varphi(v)
    $$

    로 정의한다.

    (a) $\Lambda$가 $V$에서 $V''$로 가는 선형사상임을 보여라.

    (b) $T\in\mathcal{L}(V)$이면 $T''\circ\Lambda=\Lambda\circ T$임을 보여라. 여기서 $T''=(T')'$이다.

    (c) $V$가 유한차원이면 $\Lambda$가 $V$에서 $V''$ 위로의 동형사상임을 보여라.

33. $U$가 $V$의 부분공간이라고 하자. $\pi:V\to V/U$를 보통의 몫사상이라 하자. 그러면 $\pi'\in\mathcal{L}((V/U)',V')$이다.

    (a) $\pi'$가 단사임을 보여라.

    (b) $\text{range}\pi'=U^0$임을 보여라.

    (c) $\pi'$가 $(V/U)'$에서 $U^0$ 위로의 동형사상임을 결론 내려라.
