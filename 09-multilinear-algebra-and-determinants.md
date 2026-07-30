# 9장 다중선형 대수와 행렬식

이 장은 벡터공간 위의 쌍선형 형식과 이차형식을 살펴보며 시작한다. 그다음 다중선형 형식으로 넘어간다. $\dim V=n$인 벡터공간 위에서 교대 $n$-선형 형식들의 벡터공간이 $1$차원임을 보일 것이다. 이 결과를 통해 연산자의 행렬식을 기저에 의존하지 않고 깔끔하게 정의할 수 있다.

교대 다중선형 형식을 통해 행렬식에 접근하면 행렬식의 핵심 성질들이 자연스럽게 증명된다. 예를 들어 같은 벡터공간 위의 모든 연산자 $S,T$에 대해
$$
\det(ST)=(\det S)(\det T)
$$
가 성립함을 보일 것이다. 또한 $T$가 가역일 필요충분조건은 $\det T\ne 0$임을 보게 된다. 복소 벡터공간 위의 연산자의 행렬식은 그 연산자의 고윳값들을 중복도만큼 곱한 것과 같다는 중요한 결과도 얻는다.

이 장은 텐서곱의 소개로 끝난다.

**이 장에서 계속 사용하는 가정**

- $\mathbb{F}$는 $\mathbb{R}$ 또는 $\mathbb{C}$를 뜻한다.
- $V$와 $W$는 $\mathbb{F}$ 위의 유한차원 비영 벡터공간이다.

그림: 괴팅겐 대학교 수학연구소. 이 건물은 에미 뇌터(1882-1935)가 이미 15년 동안 그 대학에서 연구 수학자이자 교수진으로 활동한 뒤인 1930년에 문을 열었다. 뇌터는 1933년에 나치 정부에 의해 해고되었다. 그때까지 뇌터와 그의 협력자들은 선형대수의 발전에도 기여한 추상대수적 관점을 포함하여 현대 대수학의 많은 기초를 세웠다.

## 9A 쌍선형 형식과 이차형식

### 쌍선형 형식

$V$ 위의 쌍선형 형식은 $V\times V$에서 $\mathbb{F}$로 가는 함수로, 각 자리를 따로 보면 선형이다. 즉 한 자리를 고정하면 다른 자리의 함수는 선형함수가 된다.

**9.1 정의: 쌍선형 형식**

$V$ 위의 **쌍선형 형식**은 함수 $\beta:V\times V\to\mathbb{F}$로서 모든 $u\in V$에 대해
$$
v\mapsto \beta(v,u),\qquad v\mapsto \beta(u,v)
$$
가 둘 다 $V$ 위의 선형범함수인 것이다.

위 정의에서 쓰인 선형범함수는 스칼라체 $\mathbb{F}$로 가는 선형함수를 뜻한다. 따라서 용어만 놓고 보면 "쌍선형 범함수"가 더 일관적이지만, 표준 용어는 쌍선형 형식이다.

예를 들어 $V$가 실 내적공간이면 $(u,v)\mapsto \langle u,v\rangle$는 $V$ 위의 쌍선형 형식이다. 그러나 $V$가 비영 복소 내적공간이면 이 함수는 쌍선형 형식이 아니다. 복소 내적은 둘째 자리에서 선형이 아니라 켤레선형이기 때문이다.

$\mathbb{F}=\mathbb{R}$일 때 쌍선형 형식은 내적과 다르다. 내적은 대칭성
$$
\beta(v,w)=\beta(w,v)
$$
과 양의 정부호성
$$
\beta(v,v)>0\qquad (v\in V\setminus\{0\})
$$
을 요구하지만, 쌍선형 형식에는 이런 조건이 필요 없다.

**9.2 예: 쌍선형 형식**

- 함수 $\beta:\mathbb{F}^3\times\mathbb{F}^3\to\mathbb{F}$를

  $$
  \beta((x_1,x_2,x_3),(y_1,y_2,y_3))
  =x_1y_2-5x_2y_3+2x_3y_1
  $$
  로 정의하면 $\beta$는 $\mathbb{F}^3$ 위의 쌍선형 형식이다.

- $A$가 $n\times n$ 행렬이고 $A_{j,k}\in\mathbb{F}$가 $j$행 $k$열의 성분이라고 하자. $\mathbb{F}^n$ 위의 쌍선형 형식 $\beta_A$를

  $$
  \beta_A((x_1,\ldots,x_n),(y_1,\ldots,y_n))
  =\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jy_k
  $$
  로 정의할 수 있다. 앞의 예는 $n=3$이고

  $$
  A=
  \begin{pmatrix}
  0&1&0\\
  0&0&-5\\
  2&0&0
  \end{pmatrix}
  $$
  인 특수한 경우이다.

- $V$가 실 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 함수 $\beta:V\times V\to\mathbb{R}$를
  $$
  \beta(u,v)=\langle u,Tv\rangle
  $$
  로 정의하면 $\beta$는 $V$ 위의 쌍선형 형식이다.

- $n$이 양의 정수이면, 함수 $\beta:\mathcal{P}_n(\mathbb{R})\times\mathcal{P}_n(\mathbb{R})\to\mathbb{R}$를
  $$
  \beta(p,q)=p(2)q'(3)
  $$
  로 정의할 수 있다. 이는 $\mathcal{P}_n(\mathbb{R})$ 위의 쌍선형 형식이다.

- $\varphi,\tau\in V'$라고 하자. 함수 $\beta:V\times V\to\mathbb{F}$를
  $$
  \beta(u,v)=\varphi(u)\tau(v)
  $$
  로 정의하면 $\beta$는 $V$ 위의 쌍선형 형식이다.

- 더 일반적으로 $\varphi_1,\ldots,\varphi_n,\tau_1,\ldots,\tau_n\in V'$라고 하자. 함수 $\beta:V\times V\to\mathbb{F}$를
  $$
  \beta(u,v)=\varphi_1(u)\tau_1(v)+\cdots+\varphi_n(u)\tau_n(v)
  $$
  로 정의하면 $\beta$는 $V$ 위의 쌍선형 형식이다.

$V$ 위의 쌍선형 형식은 $V\times V$에서 $\mathbb{F}$로 가는 함수이다. $V\times V$ 자체도 벡터공간이므로, 쌍선형 형식이 동시에 $V\times V$ 위의 선형함수일 수 있는지 물을 수 있다. 9.2의 쌍선형 형식들은 특별히 영함수가 되는 경우를 제외하면 $V\times V$ 위의 선형사상이 아니다. 연습문제 3에서 $V$ 위의 쌍선형 형식 $\beta$가 $V\times V$ 위의 선형함수라면 $\beta=0$이어야 함을 보인다.

**9.3 정의: $V^{(2)}$**

$V$ 위의 쌍선형 형식들의 집합을 $V^{(2)}$로 나타낸다.

함수의 일반적인 덧셈과 스칼라곱을 사용하면 $V^{(2)}$는 벡터공간이다.

**9.4 정의: 쌍선형 형식의 행렬, $\mathcal{M}(\beta)$**

$\beta$가 $V$ 위의 쌍선형 형식이고 $e_1,\ldots,e_n$이 $V$의 기저라고 하자. 이 기저에 대한 $\beta$의 행렬은 $n\times n$ 행렬 $\mathcal{M}(\beta)$이며, 그 $j$행 $k$열 성분은
$$
\mathcal{M}(\beta)_{j,k}=\beta(e_j,e_k)
$$
로 정의된다.

기저가 문맥에서 명확하지 않으면
$$
\mathcal{M}(\beta,(e_1,\ldots,e_n))
$$
라고 쓴다.

**9.5 $\dim V^{(2)}=(\dim V)^2$**

$e_1,\ldots,e_n$이 $V$의 기저라고 하자. 그러면 사상
$$
\beta\mapsto \mathcal{M}(\beta)
$$
는 $V^{(2)}$에서 $\mathbb{F}^{n,n}$으로 가는 동형사상이다. 특히
$$
\dim V^{(2)}=(\dim V)^2.
$$

**증명**

$\beta\mapsto \mathcal{M}(\beta)$는 분명히 $V^{(2)}$에서 $\mathbb{F}^{n,n}$으로 가는 선형사상이다. $A\in\mathbb{F}^{n,n}$에 대해 $V$ 위의 쌍선형 형식 $\beta_A$를

$$
\beta_A(x_1e_1+\cdots+x_ne_n,\;y_1e_1+\cdots+y_ne_n)
=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jy_k
$$
로 정의한다.

$V^{(2)}$에서 $\mathbb{F}^{n,n}$으로 가는 선형사상 $\beta\mapsto\mathcal{M}(\beta)$와 $\mathbb{F}^{n,n}$에서 $V^{(2)}$로 가는 선형사상 $A\mapsto\beta_A$는 서로 역이다. 실제로 모든 $\beta\in V^{(2)}$에 대해 $\beta_{\mathcal{M}(\beta)}=\beta$이고, 모든 $A\in\mathbb{F}^{n,n}$에 대해 $\mathcal{M}(\beta_A)=A$이다.

따라서 두 사상은 모두 동형사상이고, 두 벡터공간은 같은 차원을 가진다. 그러므로
$$
\dim V^{(2)}=\dim\mathbb{F}^{n,n}=n^2=(\dim V)^2.
$$

행렬 $C$의 전치행렬을 $C^{\mathrm{t}}$로 나타낸다. 이는 $C$의 행과 열을 서로 바꾸어 얻는 행렬이다.

**9.6 쌍선형 형식과 연산자의 합성**

$\beta$가 $V$ 위의 쌍선형 형식이고 $T\in\mathcal{L}(V)$라고 하자. $V$ 위의 쌍선형 형식 $\alpha,\rho$를
$$
\alpha(u,v)=\beta(u,Tv),\qquad \rho(u,v)=\beta(Tu,v)
$$
로 정의하자. $e_1,\ldots,e_n$이 $V$의 기저이면

$$
\mathcal{M}(\alpha)=\mathcal{M}(\beta)\mathcal{M}(T),
\qquad
\mathcal{M}(\rho)=\mathcal{M}(T)^{\mathrm{t}}\mathcal{M}(\beta).
$$

**증명**

$j,k\in\{1,\ldots,n\}$이면

$$
\begin{aligned}
\mathcal{M}(\alpha)_{j,k}
&=\alpha(e_j,e_k)\\
&=\beta(e_j,Te_k)\\
&=\beta\left(e_j,\sum_{m=1}^n \mathcal{M}(T)_{m,k}e_m\right)\\
&=\sum_{m=1}^n \beta(e_j,e_m)\mathcal{M}(T)_{m,k}\\
&=(\mathcal{M}(\beta)\mathcal{M}(T))_{j,k}.
\end{aligned}
$$

따라서 $\mathcal{M}(\alpha)=\mathcal{M}(\beta)\mathcal{M}(T)$이다. $\mathcal{M}(\rho)=\mathcal{M}(T)^{\mathrm{t}}\mathcal{M}(\beta)$도 비슷하게 증명된다.

**9.7 기저변환 공식**

$\beta\in V^{(2)}$라고 하자. $e_1,\ldots,e_n$과 $f_1,\ldots,f_n$이 $V$의 기저라고 하자. 또한

$$
A=\mathcal{M}(\beta,(e_1,\ldots,e_n)),\qquad
B=\mathcal{M}(\beta,(f_1,\ldots,f_n))
$$
이고
$$
C=\mathcal{M}(I,(e_1,\ldots,e_n),(f_1,\ldots,f_n))
$$
라고 하자. 그러면
$$
A=C^{\mathrm{t}}BC.
$$

**증명**

선형사상 보조정리(3.4)에 의해 각 $k=1,\ldots,n$에 대해 $Tf_k=e_k$가 되는 연산자 $T\in\mathcal{L}(V)$가 존재한다. 연산자의 행렬 정의에 의해
$$
\mathcal{M}(T,(f_1,\ldots,f_n))=C.
$$

$V$ 위의 쌍선형 형식 $\alpha,\rho$를

$$
\alpha(u,v)=\beta(u,Tv),\qquad
\rho(u,v)=\alpha(Tu,v)=\beta(Tu,Tv)
$$
로 정의한다. 그러면 모든 $j,k$에 대해
$$
\beta(e_j,e_k)=\beta(Tf_j,Tf_k)=\rho(f_j,f_k).
$$

따라서

$$
\begin{aligned}
A
&=\mathcal{M}(\rho,(f_1,\ldots,f_n))\\
&=C^{\mathrm{t}}\mathcal{M}(\alpha,(f_1,\ldots,f_n))\\
&=C^{\mathrm{t}}BC,
\end{aligned}
$$
이며 둘째 줄과 셋째 줄은 각각 9.6에서 따른다.

**9.8 예: $\mathcal{P}_2(\mathbb{R})$ 위의 쌍선형 형식의 행렬**

$\mathcal{P}_2(\mathbb{R})$ 위의 쌍선형 형식 $\beta$를 $\beta(p,q)=p(2)q'(3)$로 정의하자. 다음과 같이 두자.
$$
A=\mathcal{M}(\beta,(1,x-2,(x-3)^2)),
$$
$$
B=\mathcal{M}(\beta,(1,x,x^2)),
$$
$$
C=\mathcal{M}(I,(1,x-2,(x-3)^2),(1,x,x^2)).
$$

그러면

$$
A=
\begin{pmatrix}
0&1&0\\
0&0&0\\
0&1&0
\end{pmatrix},\qquad
B=
\begin{pmatrix}
0&1&6\\
0&2&12\\
0&4&24
\end{pmatrix},
$$

$$
C=
\begin{pmatrix}
1&-2&9\\
0&1&-6\\
0&0&1
\end{pmatrix}.
$$

기저변환 공식 9.7은 $A=C^{\mathrm{t}}BC$라고 말한다. 위 행렬들로 직접 곱셈하여 확인할 수 있다.

### 대칭 쌍선형 형식

**9.9 정의: 대칭 쌍선형 형식, $V_{\text{sym}}^{(2)}$**

쌍선형 형식 $\rho\in V^{(2)}$가 모든 $u,w\in V$에 대해
$$
\rho(u,w)=\rho(w,u)
$$
를 만족하면 $\rho$를 **대칭**이라고 한다. $V$ 위의 대칭 쌍선형 형식들의 집합을 $V_{\text{sym}}^{(2)}$로 나타낸다.

**9.10 예: 대칭 쌍선형 형식**

- $V$가 실 내적공간이고 $\rho\in V^{(2)}$를
  $$
  \rho(u,w)=\langle u,w\rangle
  $$
  로 정의하면 $\rho$는 $V$ 위의 대칭 쌍선형 형식이다.

- $V$가 실 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. $\rho\in V^{(2)}$를
  $$
  \rho(u,w)=\langle u,Tw\rangle
  $$
  로 정의하면, $\rho$가 $V$ 위의 대칭 쌍선형 형식일 필요충분조건은 $T$가 자기수반 연산자인 것이다.

- $\rho:\mathcal{L}(V)\times\mathcal{L}(V)\to\mathbb{F}$를
  $$
  \rho(S,T)=\text{tr}(ST)
  $$
  로 정의하면 $\rho$는 $\mathcal{L}(V)$ 위의 대칭 쌍선형 형식이다. 이는 트레이스가 $\mathcal{L}(V)$ 위의 선형범함수이고 모든 $S,T\in\mathcal{L}(V)$에 대해 $\text{tr}(ST)=\text{tr}(TS)$이기 때문이다.

**9.11 정의: 대칭 행렬**

정사각행렬 $A$가 자신의 전치행렬과 같으면 $A$를 **대칭 행렬**이라고 한다.

$V$ 위의 연산자는 어떤 기저에 대해서는 대칭 행렬을 가지지만 다른 기저에 대해서는 그렇지 않을 수 있다. 반면 다음 결과는 $V$ 위의 쌍선형 형식은 모든 기저에 대해 대칭 행렬을 가지거나, 어떤 기저에 대해서도 대칭 행렬을 가지지 않는다는 것을 보여 준다.

**9.12 대칭 쌍선형 형식은 대각화 가능하다**

$\rho\in V^{(2)}$라고 하자. 다음은 서로 동치이다.

(a) $\rho$는 $V$ 위의 대칭 쌍선형 형식이다.

(b) $V$의 모든 기저 $e_1,\ldots,e_n$에 대해 $\mathcal{M}(\rho,(e_1,\ldots,e_n))$는 대칭 행렬이다.

(c) $V$의 어떤 기저 $e_1,\ldots,e_n$에 대해 $\mathcal{M}(\rho,(e_1,\ldots,e_n))$는 대칭 행렬이다.

(d) $V$의 어떤 기저 $e_1,\ldots,e_n$에 대해 $\mathcal{M}(\rho,(e_1,\ldots,e_n))$는 대각행렬이다.

**증명**

(a)가 성립한다고 하자. $e_1,\ldots,e_n$이 $V$의 기저이고 $j,k\in\{1,\ldots,n\}$이면 $\rho(e_j,e_k)=\rho(e_k,e_j)$이다. 따라서 $\mathcal{M}(\rho,(e_1,\ldots,e_n))$는 대칭 행렬이다. 그러므로 (a)는 (b)를 함의한다.

(b)가 (c)를 함의함은 명백하다.

이제 (c)가 성립한다고 하자. 즉 어떤 기저 $e_1,\ldots,e_n$에 대해 $\mathcal{M}(\rho,(e_1,\ldots,e_n))$가 대칭 행렬이라고 하자. $u,w\in V$라 하자. 어떤 $a_1,\ldots,a_n,b_1,\ldots,b_n\in\mathbb{F}$가 존재하여

$$
u=a_1e_1+\cdots+a_ne_n,\qquad
w=b_1e_1+\cdots+b_ne_n
$$
이다. 그러면

$$
\begin{aligned}
\rho(u,w)
&=\rho\left(\sum_{j=1}^n a_je_j,\sum_{k=1}^n b_ke_k\right)\\
&=\sum_{j=1}^n\sum_{k=1}^n a_jb_k\rho(e_j,e_k)\\
&=\sum_{j=1}^n\sum_{k=1}^n a_jb_k\rho(e_k,e_j)\\
&=\rho\left(\sum_{k=1}^n b_ke_k,\sum_{j=1}^n a_je_j\right)\\
&=\rho(w,u).
\end{aligned}
$$

따라서 $\rho$는 대칭 쌍선형 형식이다. 그러므로 (c)는 (a)를 함의한다.

이제 (a), (b), (c)가 서로 동치임을 보였다. 모든 대각행렬은 대칭 행렬이므로 (d)는 (c)를 함의한다. 남은 것은 (a)가 (d)를 함의함을 보이는 것이다. 이를 $n=\dim V$에 대한 귀납법으로 증명한다.

$n=1$이면 모든 $1\times 1$ 행렬이 대각행렬이므로 명백하다. 이제 $n>1$이고 차원이 하나 작은 경우에 대해 결론이 성립한다고 가정하자. $\rho$가 대칭 쌍선형 형식이라고 하자. $\rho=0$이면 모든 기저에 대한 행렬이 영행렬이므로 대각행렬이다. 따라서 $\rho\ne 0$이라고 가정할 수 있다.

그러면 어떤 $u,w\in V$에 대해 $\rho(u,w)\ne 0$이다. 또한
$$
2\rho(u,w)=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w).
$$

왼쪽이 영이 아니므로 오른쪽의 세 항이 모두 $0$일 수 없다. 따라서 어떤 $v\in V$에 대해 $\rho(v,v)\ne 0$이다.

다음 부분공간을 정의하자.
$$
U=\{u\in V:\rho(u,v)=0\}.
$$

이는 선형범함수 $u\mapsto \rho(u,v)$의 영공간이다. 이 선형범함수는 영범함수가 아니다. 왜냐하면 $v\notin U$이기 때문이다. 따라서 $\dim U=n-1$이다. 귀납가정에 의해 $U$에는 $\rho|_{U\times U}$의 행렬을 대각행렬로 만드는 기저 $e_1,\ldots,e_{n-1}$이 존재한다.

$v\notin U$이므로 $e_1,\ldots,e_{n-1},v$는 $V$의 기저이다. 각 $k=1,\ldots,n-1$에 대해 $\rho(e_k,v)=0$이고, $\rho$가 대칭이므로 $\rho(v,e_k)=0$이다. 따라서 이 기저에 대한 $\rho$의 행렬은 대각행렬이다.

**9.13 실 내적공간에서 정규직교 기저에 의한 대칭 쌍선형 형식의 대각화**

$V$가 실 내적공간이고 $\rho$가 $V$ 위의 대칭 쌍선형 형식이라고 하자. 그러면 $\rho$는 $V$의 어떤 정규직교 기저에 대해 대각행렬을 가진다.

**증명**

$f_1,\ldots,f_n$을 $V$의 정규직교 기저라고 하자. $B=\mathcal{M}(\rho,(f_1,\ldots,f_n))$라고 두자. 9.12에 의해 $B$는 대칭 행렬이다. $\mathcal{M}(T,(f_1,\ldots,f_n))=B$가 되는 연산자 $T\in\mathcal{L}(V)$를 잡으면 $T$는 자기수반이다.

실 스펙트럼 정리(7.29)에 의해 $T$는 $V$의 어떤 정규직교 기저 $e_1,\ldots,e_n$에 대해 대각행렬을 가진다. $C=\mathcal{M}(I,(e_1,\ldots,e_n),(f_1,\ldots,f_n))$라고 하자. 그러면 3.84에 의해 $C^{-1}BC$는 기저 $e_1,\ldots,e_n$에 대한 $T$의 행렬이므로 대각행렬이다. 또한
$$
\mathcal{M}(\rho,(e_1,\ldots,e_n))=C^{\mathrm{t}}BC=C^{-1}BC,
$$

여기서 첫 등식은 9.7에서 나오고, 둘째 등식은 $C$가 실수 성분을 가진 유니터리 행렬이어서 $C^{-1}=C^{\mathrm{t}}$이기 때문이다.

### 교대 쌍선형 형식

**9.14 정의: 교대 쌍선형 형식, $V_{\text{alt}}^{(2)}$**

쌍선형 형식 $\alpha\in V^{(2)}$가 모든 $v\in V$에 대해
$$
\alpha(v,v)=0
$$
을 만족하면 $\alpha$를 **교대**라고 한다. $V$ 위의 교대 쌍선형 형식들의 집합을 $V_{\text{alt}}^{(2)}$로 나타낸다.

**9.15 예: 교대 쌍선형 형식**

- $n\ge 3$이고 $\alpha:\mathbb{F}^n\times\mathbb{F}^n\to\mathbb{F}$를

  $$
  \alpha((x_1,\ldots,x_n),(y_1,\ldots,y_n))
  =x_1y_2-x_2y_1+x_1y_3-x_3y_1
  $$
  로 정의하면 $\alpha$는 $\mathbb{F}^n$ 위의 교대 쌍선형 형식이다.

- $\varphi,\tau\in V'$라고 하자. $V$ 위의 쌍선형 형식 $\alpha$를
  $$
  \alpha(u,w)=\varphi(u)\tau(w)-\varphi(w)\tau(u)
  $$
  로 정의하면 $\alpha$는 교대이다.

**9.16 교대 쌍선형 형식의 특징**

$V$ 위의 쌍선형 형식 $\alpha$가 교대일 필요충분조건은 모든 $u,w\in V$에 대해
$$
\alpha(u,w)=-\alpha(w,u)
$$
가 성립하는 것이다.

**증명**

먼저 $\alpha$가 교대라고 하자. $u,w\in V$이면

$$
\begin{aligned}
0
&=\alpha(u+w,u+w)\\
&=\alpha(u,u)+\alpha(u,w)+\alpha(w,u)+\alpha(w,w)\\
&=\alpha(u,w)+\alpha(w,u).
\end{aligned}
$$

따라서 $\alpha(u,w)=-\alpha(w,u)$이다.

반대로 모든 $u,w\in V$에 대해 $\alpha(u,w)=-\alpha(w,u)$라고 하자. 그러면 모든 $v\in V$에 대해 $\alpha(v,v)=-\alpha(v,v)$이고, 따라서 $\alpha(v,v)=0$이다. 그러므로 $\alpha$는 교대이다.

**9.17 $V^{(2)}=V_{\text{sym}}^{(2)}\oplus V_{\text{alt}}^{(2)}$**

$V_{\text{sym}}^{(2)}$와 $V_{\text{alt}}^{(2)}$는 $V^{(2)}$의 부분공간이다. 또한
$$
V^{(2)}=V_{\text{sym}}^{(2)}\oplus V_{\text{alt}}^{(2)}.
$$

**증명**

대칭 쌍선형 형식들의 합과 스칼라배는 다시 대칭 쌍선형 형식이고, 영 쌍선형 형식도 대칭이다. 따라서 $V_{\text{sym}}^{(2)}$는 $V^{(2)}$의 부분공간이다. 마찬가지로 $V_{\text{alt}}^{(2)}$도 $V^{(2)}$의 부분공간이다.

이제 임의의 $\beta\in V^{(2)}$에 대해 $\rho,\alpha\in V^{(2)}$를

$$
\rho(u,w)=\frac{\beta(u,w)+\beta(w,u)}{2},\qquad
\alpha(u,w)=\frac{\beta(u,w)-\beta(w,u)}{2}
$$
로 정의한다. 그러면 $\rho\in V_{\text{sym}}^{(2)}$, $\alpha\in V_{\text{alt}}^{(2)}$이고 $\beta=\rho+\alpha$이다. 따라서
$$
V^{(2)}=V_{\text{sym}}^{(2)}+V_{\text{alt}}^{(2)}.
$$

마지막으로 두 부분공간의 교집합이 $\{0\}$임을 보이자. $\beta\in V_{\text{sym}}^{(2)}\cap V_{\text{alt}}^{(2)}$라고 하자. $u,w\in V$이면 9.16에 의해
$$
\beta(u,w)=-\beta(w,u)=-\beta(u,w)
$$
이므로 $\beta(u,w)=0$이다. 따라서 $\beta=0$이고, 합은 직합이다.

### 이차형식

**9.18 정의: 쌍선형 형식에 대응하는 이차형식, $q_\beta$**

$\beta$가 $V$ 위의 쌍선형 형식일 때 함수 $q_\beta:V\to\mathbb{F}$를
$$
q_\beta(v)=\beta(v,v)
$$
로 정의한다. 함수 $q:V\to\mathbb{F}$가 어떤 쌍선형 형식 $\beta$에 대해 $q=q_\beta$를 만족하면 $q$를 $V$ 위의 **이차형식**이라고 한다.

$\beta$가 쌍선형 형식이면 $q_\beta=0$일 필요충분조건은 $\beta$가 교대인 것이다.

**9.19 예: 이차형식**

$\mathbb{R}^3$ 위의 쌍선형 형식 $\beta$를

$$
\beta((x_1,x_2,x_3),(y_1,y_2,y_3))
=x_1y_1-4x_1y_2+8x_1y_3-3x_3y_3
$$
로 정의하자. 그러면 $q_\beta$는 다음 공식으로 주어지는 $\mathbb{R}^3$ 위의 이차형식이다.
$$
q_\beta(x_1,x_2,x_3)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2.
$$

**9.20 $\mathbb{F}^n$ 위의 이차형식**

$n$이 양의 정수이고 $q$가 $\mathbb{F}^n$에서 $\mathbb{F}$로 가는 함수라고 하자. 그러면 $q$가 $\mathbb{F}^n$ 위의 이차형식일 필요충분조건은 어떤 $A_{j,k}\in\mathbb{F}$가 존재하여 모든 $(x_1,\ldots,x_n)\in\mathbb{F}^n$에 대해
$$
q(x_1,\ldots,x_n)=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jx_k
$$
가 성립하는 것이다.

**증명**

먼저 $q$가 $\mathbb{F}^n$ 위의 이차형식이라고 하자. 그러면 어떤 쌍선형 형식 $\beta$에 대해 $q=q_\beta$이다. $\mathbb{F}^n$의 표준 기저에 대한 $\beta$의 행렬을 $A$라고 하자. 그러면 모든 $(x_1,\ldots,x_n)\in\mathbb{F}^n$에 대해

$$
\begin{aligned}
q(x_1,\ldots,x_n)
&=\beta((x_1,\ldots,x_n),(x_1,\ldots,x_n))\\
&=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jx_k.
\end{aligned}
$$

반대로 위 꼴의 수 $A_{j,k}$가 존재한다고 하자. $\mathbb{F}^n$ 위의 쌍선형 형식 $\beta$를

$$
\beta((x_1,\ldots,x_n),(y_1,\ldots,y_n))
=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jy_k
$$
로 정의하면 $q=q_\beta$이다.

**9.21 이차형식의 특징**

$q:V\to\mathbb{F}$가 함수라고 하자. 다음은 서로 동치이다.

(a) $q$는 이차형식이다.

(b) $q=q_\rho$가 되는 $V$ 위의 대칭 쌍선형 형식 $\rho$가 유일하게 존재한다.

(c) 모든 $\lambda\in\mathbb{F}$와 $v\in V$에 대해
$$
q(\lambda v)=\lambda^2q(v)
$$
가 성립하고, 함수
$$
(u,w)\mapsto q(u+w)-q(u)-q(w)
$$
가 $V$ 위의 대칭 쌍선형 형식이다.

(d) 모든 $v\in V$에 대해
$$
q(2v)=4q(v)
$$
가 성립하고, 함수
$$
(u,w)\mapsto q(u+w)-q(u)-q(w)
$$
가 $V$ 위의 대칭 쌍선형 형식이다.

**증명**

먼저 (a)가 성립한다고 하자. 그러면 어떤 쌍선형 형식 $\beta$에 대해 $q=q_\beta$이다. 9.17에 의해 $\beta=\rho+\alpha$가 되도록 대칭 쌍선형 형식 $\rho$와 교대 쌍선형 형식 $\alpha$를 잡을 수 있다. 따라서
$$
q=q_\beta=q_\rho+q_\alpha=q_\rho.
$$

또 $\rho'\in V_{\text{sym}}^{(2)}$가 $q_{\rho'}=q$를 만족하면 $q_{\rho'-\rho}=0$이다. 따라서 $\rho'-\rho$는 동시에 대칭이고 교대이므로 9.17에 의해 $\rho'=\rho$이다. 그러므로 (a)는 (b)를 함의한다.

이제 (b)가 성립한다고 하자. 즉 $q=q_\rho$가 되는 대칭 쌍선형 형식 $\rho$가 존재한다고 하자. $\lambda\in\mathbb{F}$, $v\in V$이면
$$
q(\lambda v)=\rho(\lambda v,\lambda v)=\lambda^2\rho(v,v)=\lambda^2q(v).
$$

또 $u,w\in V$이면

$$
\begin{aligned}
q(u+w)-q(u)-q(w)
&=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w)\\
&=2\rho(u,w).
\end{aligned}
$$

따라서 위 함수는 $2\rho$와 같으므로 대칭 쌍선형 형식이다. 그러므로 (b)는 (c)를 함의한다.

(c)가 (d)를 함의함은 명백하다.

마지막으로 (d)가 성립한다고 하자. 대칭 쌍선형 형식 $\rho$를
$$
\rho(u,w)=\frac{q(u+w)-q(u)-q(w)}{2}
$$
로 정의하자. 그러면 $v\in V$에 대해

$$
\rho(v,v)=\frac{q(2v)-q(v)-q(v)}{2}
=\frac{4q(v)-2q(v)}{2}=q(v).
$$

따라서 $q=q_\rho$이고, (d)는 (a)를 함의한다.

**9.22 예: 이차형식에 대응하는 대칭 쌍선형 형식**

$q$가 다음 공식으로 주어지는 $\mathbb{R}^3$ 위의 이차형식이라고 하자.
$$
q(x_1,x_2,x_3)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2.
$$

9.19의 쌍선형 형식 $\beta$는 $q=q_\beta$를 만족하지만 대칭은 아니다. 그러나 $\mathbb{R}^3$ 위의 쌍선형 형식 $\rho$를

$$
\begin{aligned}
\rho((x_1,x_2,x_3),(y_1,y_2,y_3))
&=x_1y_1-2x_1y_2-2x_2y_1\\
&\quad +4x_1y_3+4x_3y_1-3x_3y_3
\end{aligned}
$$
로 정의하면 $\rho$는 대칭이고 $q=q_\rho$를 만족한다.

**9.23 이차형식의 대각화**

$q$가 $V$ 위의 이차형식이라고 하자.

(a) $V$의 어떤 기저 $e_1,\ldots,e_n$과 $\lambda_1,\ldots,\lambda_n\in\mathbb{F}$가 존재하여 모든 $x_1,\ldots,x_n\in\mathbb{F}$에 대해
$$
q(x_1e_1+\cdots+x_ne_n)=\lambda_1x_1^2+\cdots+\lambda_nx_n^2
$$
가 성립한다.

(b) $\mathbb{F}=\mathbb{R}$이고 $V$가 내적공간이면, (a)의 기저를 $V$의 정규직교 기저로 선택할 수 있다.

**증명**

(a) 9.21에 의해 $q=q_\rho$가 되는 $V$ 위의 대칭 쌍선형 형식 $\rho$가 존재한다. 9.12에 의해 어떤 기저 $e_1,\ldots,e_n$에 대한 $\rho$의 행렬은 대각행렬이다. 이 대각선 성분을 $\lambda_1,\ldots,\lambda_n$이라고 하자. 그러면

$$
\rho(e_j,e_k)=
\begin{cases}
\lambda_j,& j=k,\\
0,& j\ne k
\end{cases}
$$
이다. 따라서

$$
\begin{aligned}
q(x_1e_1+\cdots+x_ne_n)
&=\rho(x_1e_1+\cdots+x_ne_n,\;x_1e_1+\cdots+x_ne_n)\\
&=\sum_{k=1}^n\sum_{j=1}^n x_jx_k\rho(e_j,e_k)\\
&=\lambda_1x_1^2+\cdots+\lambda_nx_n^2.
\end{aligned}
$$

(b) $\mathbb{F}=\mathbb{R}$이고 $V$가 내적공간이면, 9.13에 의해 (a)의 기저를 정규직교 기저로 선택할 수 있다.

### 연습문제 9A

1. $\beta$가 $\mathbb{F}$ 위의 쌍선형 형식이면 어떤 $c\in\mathbb{F}$가 존재하여 모든 $x,y\in\mathbb{F}$에 대해
  $$
  \beta(x,y)=cxy
  $$
  가 성립함을 증명하여라.

2. $n=\dim V$라고 하자. $\beta$가 $V$ 위의 쌍선형 형식이라고 하자. 그러면 어떤 $\varphi_1,\ldots,\varphi_n,\tau_1,\ldots,\tau_n\in V'$가 존재하여 모든 $u,v\in V$에 대해
  $$
  \beta(u,v)=\varphi_1(u)\tau_1(v)+\cdots+\varphi_n(u)\tau_n(v)
  $$
  가 성립함을 증명하여라. 이 연습문제는 $\dim V=n$이면 $V$ 위의 모든 쌍선형 형식이 9.2의 마지막 항목에 나타난 꼴임을 보여 준다.

3. $\beta:V\times V\to\mathbb{F}$가 $V$ 위의 쌍선형 형식이면서 동시에 $V\times V$ 위의 선형범함수라고 하자. $\beta=0$임을 증명하여라.

4. $V$가 실 내적공간이고 $\beta$가 $V$ 위의 쌍선형 형식이라고 하자. 모든 $u,v\in V$에 대해
  $$
  \beta(u,v)=\langle u,Tv\rangle
  $$
  가 되게 하는 유일한 연산자 $T\in\mathcal{L}(V)$가 존재함을 보여라.

5. $\beta$가 실 내적공간 $V$ 위의 쌍선형 형식이고, $T$가 연습문제 4에서 얻은 유일한 연산자라고 하자. 즉 모든 $u,v\in V$에 대해 $\beta(u,v)=\langle u,Tv\rangle$이다. $\beta$가 $V$ 위의 내적일 필요충분조건은 $T$가 $V$ 위의 가역 양의 연산자인 것임을 보여라.

6. 증명하거나 반례를 들어라. $\rho$가 $V$ 위의 대칭 쌍선형 형식이면
  $$
  \{v\in V:\rho(v,v)=0\}
  $$
  은 $V$의 부분공간이다.

7. 9.13의 증명, 즉 실 내적공간 위의 대칭 쌍선형 형식이 정규직교 기저에 의해 대각화된다는 증명이 $\mathbb{F}=\mathbb{R}$이라는 가정을 빼면 왜 실패하는지 설명하여라.

8. $\dim V$를 사용하여 $\dim V_{\text{sym}}^{(2)}$와 $\dim V_{\text{alt}}^{(2)}$의 공식을 찾아라.

9. $n$이 양의 정수이고
  $$
  V=\{p\in\mathcal{P}_n(\mathbb{R}):p(0)=p(1)\}
  $$
  라고 하자. $\alpha:V\times V\to\mathbb{R}$를
  $$
  \alpha(p,q)=\int_0^1 pq'
  $$
  로 정의한다. $\alpha$가 $V$ 위의 교대 쌍선형 형식임을 보여라.

10. $n$이 양의 정수이고
  $$
  V=\{p\in\mathcal{P}_n(\mathbb{R}):p(0)=p(1)\text{이고 }p'(0)=p'(1)\}
  $$
  라고 하자. $\rho:V\times V\to\mathbb{R}$를
  $$
  \rho(p,q)=\int_0^1 pq''
  $$
  로 정의한다. $\rho$가 $V$ 위의 대칭 쌍선형 형식임을 보여라.

## 9B 교대 다중선형 형식

### 다중선형 형식

**9.24 정의: $V^m$**

$m$이 양의 정수일 때
$$
V^m=\underbrace{V\times\cdots\times V}_{m\text{번}}
$$
으로 정의한다.

이제 앞 절에서 다룬 쌍선형 형식을 일반화하여 $m$-선형 형식을 정의한다.

**9.25 정의: $m$-선형 형식, $V^{(m)}$, 다중선형 형식**

- $m$이 양의 정수일 때, $V$ 위의 **$m$-선형 형식**은 함수 $\beta:V^m\to\mathbb{F}$로서 다른 자리들을 고정하면 각 자리에서 선형인 함수이다. 즉 각 $k\in\{1,\ldots,m\}$와 모든 $u_1,\ldots,u_m\in V$에 대해
  $$
  v\mapsto \beta(u_1,\ldots,u_{k-1},v,u_{k+1},\ldots,u_m)
  $$
  가 $V$에서 $\mathbb{F}$로 가는 선형사상이다.

- $V$ 위의 $m$-선형 형식들의 집합을 $V^{(m)}$로 나타낸다.

- 어떤 양의 정수 $m$에 대해 $m$-선형 형식인 함수를 $V$ 위의 **다중선형 형식**이라고 한다.

위 정의에서 $k=1$이면
$$
\beta(u_1,\ldots,u_{k-1},v,u_{k+1},\ldots,u_m)
$$
는 $\beta(v,u_2,\ldots,u_m)$을 뜻하고, $k=m$이면 $\beta(u_1,\ldots,u_{m-1},v)$를 뜻한다.

$V$ 위의 $1$-선형 형식은 $V$ 위의 선형범함수이다. $V$ 위의 $2$-선형 형식은 $V$ 위의 쌍선형 형식이다. 함수의 일반적인 덧셈과 스칼라곱을 사용하면 $V^{(m)}$는 벡터공간이 된다.

**9.26 예: $m$-선형 형식**

- $\alpha,\rho\in V^{(2)}$라고 하자. 함수 $\beta:V^4\to\mathbb{F}$를
  $$
  \beta(v_1,v_2,v_3,v_4)=\alpha(v_1,v_2)\rho(v_3,v_4)
  $$
  로 정의하면 $\beta\in V^{(4)}$이다.

- 함수 $\beta:(\mathcal{L}(V))^m\to\mathbb{F}$를
  $$
  \beta(T_1,\ldots,T_m)=\text{tr}(T_1\cdots T_m)
  $$
  로 정의하면 $\beta$는 $\mathcal{L}(V)$ 위의 $m$-선형 형식이다.

### 교대 다중선형 형식

**9.27 정의: 교대 형식, $V_{\text{alt}}^{(m)}$**

$m$이 양의 정수라고 하자.

- $V$ 위의 $m$-선형 형식 $\alpha$가, $v_1,\ldots,v_m$ 가운데 서로 다른 두 위치 $j,k$에 대해 $v_j=v_k$가 될 때마다
  $$
  \alpha(v_1,\ldots,v_m)=0
  $$
  을 만족하면 $\alpha$를 **교대**라고 한다.

- $V_{\text{alt}}^{(m)}$를 다음과 같이 정의한다.

  $$
  V_{\text{alt}}^{(m)}
  =\{\alpha\in V^{(m)}:\alpha\text{는 }V\text{ 위의 교대 }m\text{-선형 형식}\}.
  $$
  $V_{\text{alt}}^{(m)}$는 $V^{(m)}$의 부분공간이다.

**9.28 교대 다중선형 형식과 일차종속**

$m$이 양의 정수이고 $\alpha$가 $V$ 위의 교대 $m$-선형 형식이라고 하자. $v_1,\ldots,v_m$이 $V$의 일차종속 리스트이면
$$
\alpha(v_1,\ldots,v_m)=0.
$$

**증명**

$v_1,\ldots,v_m$이 일차종속이라고 하자. 일차종속 보조정리(2.19)에 의해 어떤 $v_k$가 $v_1,\ldots,v_{k-1}$의 일차결합이다. 즉 어떤 $b_1,\ldots,b_{k-1}$이 존재하여
$$
v_k=b_1v_1+\cdots+b_{k-1}v_{k-1}
$$
이다. 따라서

$$
\begin{aligned}
\alpha(v_1,\ldots,v_m)
&=\alpha\left(v_1,\ldots,v_{k-1},\sum_{j=1}^{k-1}b_jv_j,v_{k+1},\ldots,v_m\right)\\
&=\sum_{j=1}^{k-1}b_j\alpha(v_1,\ldots,v_{k-1},v_j,v_{k+1},\ldots,v_m)\\
&=0.
\end{aligned}
$$

마지막 등식은 각 항에 같은 벡터가 두 번 나타나기 때문에 성립한다.

**9.29 $m>\dim V$이면 영이 아닌 교대 $m$-선형 형식은 없다**

$m>\dim V$이면 $V$ 위의 교대 $m$-선형 형식은 영함수뿐이다.

**증명**

$\alpha$가 $V$ 위의 교대 $m$-선형 형식이고 $v_1,\ldots,v_m\in V$라고 하자. $m>\dim V$이므로 이 리스트는 일차독립이 아니다. 따라서 9.28에 의해 $\alpha(v_1,\ldots,v_m)=0$이다. 그러므로 $\alpha$는 $V^m$에서 $\mathbb{F}$로 가는 영함수이다.

### 교대 다중선형 형식과 순열

**9.30 교대 다중선형 형식의 입력 벡터 두 개를 바꾸기**

$m$이 양의 정수이고, $\alpha$가 $V$ 위의 교대 $m$-선형 형식이며, $v_1,\ldots,v_m$이 $V$의 벡터 리스트라고 하자. 그러면 $\alpha(v_1,\ldots,v_m)$에서 임의의 두 자리에 있는 벡터를 서로 바꾸면 $\alpha$의 값은 $-1$배가 된다.

**증명**

처음 두 자리에 $v_1+v_2$를 넣으면
$$
0=\alpha(v_1+v_2,v_1+v_2,v_3,\ldots,v_m).
$$

$\alpha$의 다중선형성을 사용하여 오른쪽을 전개하면

$$
\alpha(v_2,v_1,v_3,\ldots,v_m)
=-\alpha(v_1,v_2,v_3,\ldots,v_m)
$$
을 얻는다. 같은 논리로 임의의 두 자리에 있는 벡터를 바꾸면 값은 $-1$배가 된다.

예를 들어 $\alpha$가 $V$ 위의 교대 $3$-선형 형식이고 $v_1,v_2,v_3\in V$라고 하자. $\alpha(v_3,v_1,v_2)$를 $\alpha(v_1,v_2,v_3)$로 표현하려면 먼저 첫째 자리와 셋째 자리를 바꾸어
$$
\alpha(v_3,v_1,v_2)=-\alpha(v_2,v_1,v_3)
$$
을 얻고, 다시 첫째 자리와 둘째 자리를 바꾸어
$$
\alpha(v_3,v_1,v_2)=-\alpha(v_2,v_1,v_3)=\alpha(v_1,v_2,v_3)
$$
을 얻는다. 일반적으로 홀수 번 바꾸면 값은 $-1$배가 되고, 짝수 번 바꾸면 값은 변하지 않는다.

**9.31 정의: 순열, $\text{perm}m$**

$m$이 양의 정수라고 하자.

- $(1,\ldots,m)$의 **순열**은 $1,\ldots,m$을 각각 정확히 한 번씩 포함하는 리스트 $(j_1,\ldots,j_m)$이다.

- $(1,\ldots,m)$의 모든 순열의 집합을 $\text{perm}m$으로 나타낸다.

예를 들어
$$
(2,3,4,5,1)\in\text{perm}5.
$$

$\text{perm}m$의 원소는 처음 $m$개의 양의 정수의 재배열이라고 생각하면 된다.

**9.32 정의: 순열의 부호**

순열 $(j_1,\ldots,j_m)$의 **부호**는
$$
\text{sign}(j_1,\ldots,j_m)=(-1)^N
$$
으로 정의한다. 여기서 $N$은 $1\le k<\ell\le m$이고, 리스트 $(j_1,\ldots,j_m)$에서 $k$가 $\ell$보다 뒤에 나타나는 정수쌍 $(k,\ell)$의 개수이다.

따라서 순열의 부호는 자연스러운 순서가 짝수 번 뒤바뀌었으면 $1$이고, 홀수 번 뒤바뀌었으면 $-1$이다.

**9.33 예: 부호**

- 순열 $(1,\ldots,m)$은 자연스러운 순서가 전혀 바뀌지 않았으므로 부호가 $1$이다.

- 리스트 $(2,1,3,4)$에서 $k<\ell$이면서 $k$가 $\ell$보다 뒤에 나타나는 쌍은 $(1,2)$뿐이다. 따라서 이 순열의 부호는 $-1$이다.

- 순열 $(2,3,\ldots,m,1)$에서 순서가 바뀐 쌍은
  $$
  (1,2),(1,3),\ldots,(1,m)
  $$
  뿐이다. 이런 쌍은 $m-1$개이므로 이 순열의 부호는 $(-1)^{m-1}$이다.

**9.34 순열의 두 항을 바꾸기**

순열에서 두 항을 서로 바꾸면 순열의 부호는 $-1$배가 된다.

**증명**

두 순열이 있고, 둘째 순열이 첫째 순열에서 두 항을 서로 바꾸어 얻어진 것이라고 하자. 서로 바뀐 두 항은 첫째 순열에서 자연스러운 순서였을 필요충분조건이 둘째 순열에서 자연스러운 순서가 아닌 것이다. 따라서 지금까지 순서가 뒤바뀐 쌍의 개수는 $1$ 또는 $-1$만큼 변한다. 둘 다 홀수이다.

이제 서로 바뀐 두 항 사이에 있는 항들을 생각하자. 중간 항 하나가 원래 두 항 각각에 대해 모두 자연스러운 순서였으면, 바꾼 뒤에는 둘 다 자연스러운 순서가 아니다. 원래 둘 다 자연스러운 순서가 아니었으면, 바꾼 뒤에는 둘 다 자연스러운 순서이다. 원래 정확히 하나에 대해서만 자연스러운 순서였으면, 바꾼 뒤에도 그렇다. 따라서 이런 중간 항 하나가 만드는 순서 뒤바뀜 개수의 순변화는 $2$, $-2$, 또는 $0$이다. 모두 짝수이다.

나머지 쌍들에 대해서는 자연스러운 순서인지 여부가 변하지 않는다. 그러므로 순서가 뒤바뀐 쌍의 총개수의 순변화는 홀수이다. 따라서 둘째 순열의 부호는 첫째 순열의 부호의 $-1$배이다.

**9.35 순열과 교대 다중선형 형식**

$m$이 양의 정수이고 $\alpha\in V_{\text{alt}}^{(m)}$라고 하자. 그러면 $V$의 모든 벡터 리스트 $v_1,\ldots,v_m$과 모든 $(j_1,\ldots,j_m)\in\text{perm}m$에 대해

$$
\alpha(v_{j_1},\ldots,v_{j_m})
=\text{sign}(j_1,\ldots,j_m)\alpha(v_1,\ldots,v_m).
$$

**증명**

$(j_1,\ldots,j_m)$에서 시작하여 서로 다른 위치의 항들을 여러 번 바꾸면 $(1,\ldots,m)$에 도달할 수 있다. 각 교환은 9.30에 의해 $\alpha$의 값을 $-1$배로 만들고, 9.34에 의해 남은 순열의 부호도 $-1$배로 만든다. 최종적으로 부호가 $1$인 순열 $(1,\ldots,m)$에 도달한다. 따라서 원래 순열의 부호가 $1$이면 $\alpha$의 값은 짝수 번 부호가 바뀌고, 원래 순열의 부호가 $-1$이면 홀수 번 부호가 바뀐다. 원하는 식이 따른다.

**9.36 $V$ 위의 $(\dim V)$-선형 교대 형식의 공식**

$n=\dim V$라고 하자. $e_1,\ldots,e_n$이 $V$의 기저이고 $v_1,\ldots,v_n\in V$라고 하자. 각 $k\in\{1,\ldots,n\}$에 대해
$$
v_k=\sum_{j=1}^n b_{j,k}e_j
$$
가 되도록 $b_{1,k},\ldots,b_{n,k}\in\mathbb{F}$를 잡는다. 그러면 $V$ 위의 모든 교대 $n$-선형 형식 $\alpha$에 대해

$$
\alpha(v_1,\ldots,v_n)
=\alpha(e_1,\ldots,e_n)
\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)b_{j_1,1}\cdots b_{j_n,n}.
$$

**증명**

$\alpha$가 $V$ 위의 교대 $n$-선형 형식이라고 하자. 그러면

$$
\begin{aligned}
\alpha(v_1,\ldots,v_n)
&=\alpha\left(\sum_{j_1=1}^n b_{j_1,1}e_{j_1},\ldots,
\sum_{j_n=1}^n b_{j_n,n}e_{j_n}\right)\\
&=\sum_{j_1=1}^n\cdots\sum_{j_n=1}^n
b_{j_1,1}\cdots b_{j_n,n}\alpha(e_{j_1},\ldots,e_{j_n})\\
&=\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
b_{j_1,1}\cdots b_{j_n,n}\alpha(e_{j_1},\ldots,e_{j_n})\\
&=\alpha(e_1,\ldots,e_n)
\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)b_{j_1,1}\cdots b_{j_n,n}.
\end{aligned}
$$

셋째 줄은 $j_1,\ldots,j_n$이 서로 다른 정수가 아니면 $\alpha(e_{j_1},\ldots,e_{j_n})=0$이기 때문에 성립하고, 마지막 줄은 9.35에서 따른다.

**9.37 $\dim V_{\text{alt}}^{(\dim V)}=1$**

벡터공간 $V_{\text{alt}}^{(\dim V)}$의 차원은 $1$이다.

**증명**

$n=\dim V$라고 하자. $\alpha,\alpha'$가 $V$ 위의 교대 $n$-선형 형식이고 $\alpha\ne 0$이라고 하자. $\alpha(e_1,\ldots,e_n)\ne 0$이 되도록 $e_1,\ldots,e_n$을 잡는다. 그러면 어떤 $c\in\mathbb{F}$가 존재하여
$$
\alpha'(e_1,\ldots,e_n)=c\alpha(e_1,\ldots,e_n)
$$
이다. 또한 9.28에 의해 $e_1,\ldots,e_n$은 일차독립이고, 따라서 $V$의 기저이다.

$v_1,\ldots,v_n\in V$라고 하자. 9.36에서처럼 $b_{j,k}$를 잡으면

$$
\begin{aligned}
\alpha'(v_1,\ldots,v_n)
&=\alpha'(e_1,\ldots,e_n)
\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)b_{j_1,1}\cdots b_{j_n,n}\\
&=c\alpha(e_1,\ldots,e_n)
\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)b_{j_1,1}\cdots b_{j_n,n}\\
&=c\alpha(v_1,\ldots,v_n).
\end{aligned}
$$

따라서 $\alpha'=c\alpha$이다. 그러므로 $\dim V_{\text{alt}}^{(n)}\le 1$이다.

이제 영이 아닌 교대 $n$-선형 형식이 존재함을 보이면 된다. $e_1,\ldots,e_n$을 $V$의 임의의 기저라고 하고, $\varphi_1,\ldots,\varphi_n\in V'$를 모든 $v\in V$에 대해
$$
v=\sum_{j=1}^n \varphi_j(v)e_j
$$
가 되게 하는 좌표 선형범함수라고 하자. $v_1,\ldots,v_n\in V$에 대해

$$
\alpha(v_1,\ldots,v_n)
=\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)
\varphi_{j_1}(v_1)\cdots\varphi_{j_n}(v_n)
\tag{9.38}
$$
로 정의한다. 그러면 $\alpha$가 $n$-선형 형식임은 곧바로 확인된다.

$\alpha$가 교대임을 보이자. $v_1=v_2$라고 하자. 각 순열 $(j_1,\ldots,j_n)$에 대해 $(j_2,j_1,j_3,\ldots,j_n)$는 반대 부호를 가진다. $v_1=v_2$이므로 이 두 순열이 9.38의 합에 기여하는 값은 서로 상쇄된다. 따라서 $\alpha(v_1,v_1,v_3,\ldots,v_n)=0$이다. 같은 논리로 리스트 $v_1,\ldots,v_n$의 어떤 두 벡터가 같아도 $\alpha(v_1,\ldots,v_n)=0$이다. 그러므로 $\alpha$는 교대이다.

마지막으로 9.38에서 각 $v_k=e_k$라고 하자. $\varphi_j(e_k)$는 $j\ne k$이면 $0$이고 $j=k$이면 $1$이므로, 오른쪽 합에 영이 아닌 기여를 하는 순열은 $(1,\ldots,n)$뿐이다. 따라서
$$
\alpha(e_1,\ldots,e_n)=1.
$$

그러므로 영이 아닌 교대 $n$-선형 형식이 존재한다.

**9.39 교대 $(\dim V)$-선형 형식과 일차독립**

$n=\dim V$라고 하자. $\alpha$가 $V$ 위의 영이 아닌 교대 $n$-선형 형식이고 $e_1,\ldots,e_n$이 $V$의 벡터 리스트라고 하자. 그러면
$$
\alpha(e_1,\ldots,e_n)\ne 0
$$
일 필요충분조건은 $e_1,\ldots,e_n$이 일차독립인 것이다.

**증명**

먼저 $\alpha(e_1,\ldots,e_n)\ne 0$이라고 하자. 그러면 9.28에 의해 $e_1,\ldots,e_n$은 일차독립이다.

반대로 $e_1,\ldots,e_n$이 일차독립이라고 하자. $n=\dim V$이므로 이 리스트는 $V$의 기저이다. $\alpha$가 영 $n$-선형 형식이 아니므로 어떤 $v_1,\ldots,v_n\in V$에 대해
$$
\alpha(v_1,\ldots,v_n)\ne 0
$$
이다. 이제 9.36을 적용하면 $\alpha(e_1,\ldots,e_n)\ne 0$이어야 한다.

### 연습문제 9B

1. $m$이 양의 정수라고 하자. 다음을 보여라.
   $$
   \dim V^{(m)}=(\dim V)^m
   $$

2. $n\ge 3$이고 $\alpha:\mathbb{F}^n\times\mathbb{F}^n\times\mathbb{F}^n\to\mathbb{F}$를

   $$
   \begin{aligned}
   &\alpha((x_1,\ldots,x_n),(y_1,\ldots,y_n),(z_1,\ldots,z_n))\\
   &=x_1y_2z_3-x_2y_1z_3-x_3y_2z_1-x_1y_3z_2+x_3y_1z_2+x_2y_3z_1
   \end{aligned}
   $$
   로 정의한다. $\alpha$가 $\mathbb{F}^n$ 위의 교대 $3$-선형 형식임을 보여라.

3. $m$이 양의 정수이고 $\alpha$가 $V$ 위의 $m$-선형 형식이라고 하자. $v_1,\ldots,v_m$ 가운데 어떤 $j\in\{1,\ldots,m-1\}$에 대해 $v_j=v_{j+1}$이면 항상
   $$
   \alpha(v_1,\ldots,v_m)=0
   $$
   이라고 하자. $\alpha$가 $V$ 위의 교대 $m$-선형 형식임을 증명하여라.

4. 증명하거나 반례를 들어라. $\alpha\in V_{\text{alt}}^{(4)}$이면
   $$
   \{(v_1,v_2,v_3,v_4)\in V^4:\alpha(v_1,v_2,v_3,v_4)=0\}
   $$
   은 $V^4$의 부분공간이다.

5. $m$이 양의 정수이고 $\beta$가 $V$ 위의 $m$-선형 형식이라고 하자. $V$ 위의 $m$-선형 형식 $\alpha$를

   $$
   \alpha(v_1,\ldots,v_m)
   =\sum_{(j_1,\ldots,j_m)\in\text{perm}m}
   \text{sign}(j_1,\ldots,j_m)
   \beta(v_{j_1},\ldots,v_{j_m})
   $$
   로 정의한다. 왜 $\alpha\in V_{\text{alt}}^{(m)}$인지 설명하여라.

6. $m$이 양의 정수이고 $\beta$가 $V$ 위의 $m$-선형 형식이라고 하자. $V$ 위의 $m$-선형 형식 $\alpha$를

   $$
   \alpha(v_1,\ldots,v_m)
   =\sum_{(j_1,\ldots,j_m)\in\text{perm}m}
   \beta(v_{j_1},\ldots,v_{j_m})
   $$
   로 정의한다. 모든 $v_1,\ldots,v_m\in V$와 모든 $(k_1,\ldots,k_m)\in\text{perm}m$에 대해
   $$
   \alpha(v_{k_1},\ldots,v_{k_m})=\alpha(v_1,\ldots,v_m)
   $$
   임을 설명하여라.

7. $\mathbb{R}^3$ 위의 영이 아닌 교대 $2$-선형 형식 $\alpha$와 일차독립 리스트 $v_1,v_2$의 예를 들어
   $$
   \alpha(v_1,v_2)=0
   $$
   이 되게 하여라. 이 연습문제는 $n=\dim V$라는 가정을 빼면 9.39가 실패할 수 있음을 보여 준다.

## 9C 행렬식

### 행렬식의 정의

다음 정의는 연산자의 행렬식을 기저에 의존하지 않고 정의하게 해 준다.

**9.40 정의: $\alpha_T$**

$m$이 양의 정수이고 $T\in\mathcal{L}(V)$라고 하자. $\alpha\in V_{\text{alt}}^{(m)}$에 대해 $\alpha_T\in V_{\text{alt}}^{(m)}$를
$$
\alpha_T(v_1,\ldots,v_m)=\alpha(Tv_1,\ldots,Tv_m)
$$
로 정의한다. 여기서 $v_1,\ldots,v_m$은 $V$의 임의의 벡터 리스트이다.

$\alpha\mapsto\alpha_T$는 $V_{\text{alt}}^{(m)}$에서 자기 자신으로 가는 선형사상이다. 실제로 $v_j=v_k$이면 $Tv_j=Tv_k$이므로 $\alpha_T(v_1,\ldots,v_m)=0$이다.

우리는 9.37에서
$$
\dim V_{\text{alt}}^{(\dim V)}=1
$$
임을 보았다. $1$차원 벡터공간에서 자기 자신으로 가는 모든 선형사상은 어떤 유일한 스칼라를 곱하는 사상이다. 이제 $\alpha\mapsto\alpha_T$에 대해 이 스칼라를 $\det T$로 정의한다.

**9.41 정의: 연산자의 행렬식, $\det T$**

$T\in\mathcal{L}(V)$라고 하자. $T$의 **행렬식** $\det T$는 모든 $\alpha\in V_{\text{alt}}^{(\dim V)}$에 대해
$$
\alpha_T=(\det T)\alpha
$$
가 성립하게 하는 유일한 $\mathbb{F}$의 원소로 정의한다.

**9.42 예: 연산자의 행렬식**

$n=\dim V$라고 하자.

- $I$가 $V$ 위의 항등연산자이면 모든 $\alpha\in V_{\text{alt}}^{(n)}$에 대해 $\alpha_I=\alpha$이다. 따라서 $\det I=1$이다.

- 더 일반적으로 $\lambda\in\mathbb{F}$이면 모든 $\alpha\in V_{\text{alt}}^{(n)}$에 대해 $\alpha_{\lambda I}=\lambda^n\alpha$이다. 따라서
  $$
  \det(\lambda I)=\lambda^n.
  $$

- 더 일반적으로 $T\in\mathcal{L}(V)$이고 $\lambda\in\mathbb{F}$이면 모든 $\alpha\in V_{\text{alt}}^{(n)}$에 대해
  $$
  \alpha_{\lambda T}=\lambda^n\alpha_T=\lambda^n(\det T)\alpha
  $$
  이다. 따라서
  $$
  t(\lambda T)=\lambda^n\det T.
  $$

- $T\in\mathcal{L}(V)$이고 $V$가 $T$의 고유벡터들로 이루어진 기저 $e_1,\ldots,e_n$을 가지며, 대응하는 고윳값이 $\lambda_1,\ldots,\lambda_n$이라고 하자. $\alpha\in V_{\text{alt}}^{(n)}$이면

  $$
  \alpha_T(e_1,\ldots,e_n)
  =\alpha(\lambda_1e_1,\ldots,\lambda_ne_n)
  =(\lambda_1\cdots\lambda_n)\alpha(e_1,\ldots,e_n).
  $$

  $\alpha\ne 0$이면 9.39에 의해 $\alpha(e_1,\ldots,e_n)\ne 0$이다. 따라서
  $$
  \det T=\lambda_1\cdots\lambda_n.
  $$

이제 정사각행렬의 행렬식을 정의하고 공식을 제시한다. 정사각행렬에 연산자를 대응시킨 뒤, 그 행렬의 행렬식을 대응하는 연산자의 행렬식으로 정의한다.

**9.43 정의: 행렬의 행렬식, $\det A$**

$n$이 양의 정수이고 $A$가 $\mathbb{F}$의 성분을 가지는 $n\times n$ 정사각행렬이라고 하자. $\mathbb{F}^n$의 표준 기저에 대한 행렬이 $A$인 연산자 $T\in\mathcal{L}(\mathbb{F}^n)$를 잡는다. $A$의 **행렬식** $\det A$는
$$
\det A=\det T
$$
로 정의한다.

**9.44 예: 행렬의 행렬식**

- $I$가 $n\times n$ 항등행렬이면, 대응하는 $\mathbb{F}^n$ 위의 연산자는 항등연산자이다. 따라서 항등행렬의 행렬식은 $1$이다.

- $A$가 대각선에 $\lambda_1,\ldots,\lambda_n$을 가지는 대각행렬이라고 하자. 대응하는 $\mathbb{F}^n$ 위의 연산자는 표준 기저를 고유벡터로 가지며, 고윳값은 $\lambda_1,\ldots,\lambda_n$이다. 따라서
  $$
  \det A=\lambda_1\cdots\lambda_n.
  $$

다음 결과에서 $v_1,\ldots,v_n$은 $\mathbb{F}^n$의 $n$개의 열벡터로 생각한다. 표기
$$
(v_1\ \cdots\ v_n)
$$
는 $k$번째 열이 $v_k$인 $n\times n$ 정사각행렬을 뜻한다.

**9.45 행렬식은 교대 다중선형 형식이다**

$n$이 양의 정수라고 하자. $\mathbb{F}^n$의 벡터 리스트 $v_1,\ldots,v_n$을
$$
\det(v_1\ \cdots\ v_n)
$$
로 보내는 사상은 $\mathbb{F}^n$ 위의 교대 $n$-선형 형식이다.

**증명**

$e_1,\ldots,e_n$을 $\mathbb{F}^n$의 표준 기저라고 하자. $T\in\mathcal{L}(\mathbb{F}^n)$를 각 $k=1,\ldots,n$에 대해 $Te_k=v_k$가 되게 잡는다. 그러면 $T$의 표준 기저에 대한 행렬은 $(v_1\ \cdots\ v_n)$이다. 따라서 행렬의 행렬식의 정의에 의해
$$
\det(v_1\ \cdots\ v_n)=\det T.
$$

$\alpha$를 $\alpha(e_1,\ldots,e_n)=1$인 $\mathbb{F}^n$ 위의 교대 $n$-선형 형식이라고 하자. 그러면

$$
\begin{aligned}
\det(v_1\ \cdots\ v_n)
&=\det T\\
&=(\det T)\alpha(e_1,\ldots,e_n)\\
&=\alpha(Te_1,\ldots,Te_n)\\
&=\alpha(v_1,\ldots,v_n).
\end{aligned}
$$

따라서 $v_1,\ldots,v_n$을 $\det(v_1\ \cdots\ v_n)$으로 보내는 사상은 교대 $n$-선형 형식 $\alpha$이다.

**9.46 행렬식 공식**

$n$이 양의 정수이고 $A$가 $n\times n$ 정사각행렬이라고 하자. 그러면

$$
\det A=
\sum_{(j_1,\ldots,j_n)\in\text{perm}n}
\text{sign}(j_1,\ldots,j_n)A_{j_1,1}\cdots A_{j_n,n}.
$$

**증명**

9.36을 $V=\mathbb{F}^n$에 적용한다. 여기서 $e_1,\ldots,e_n$은 $\mathbb{F}^n$의 표준 기저이고, $\alpha$는 $v_1,\ldots,v_n$을 $\det(v_1\ \cdots\ v_n)$으로 보내는 교대 $n$-선형 형식이다. 각 $v_k$가 $A$의 $k$번째 열이면 9.36의 $b_{j,k}$는 $A_{j,k}$와 같다. 또한
$$
\alpha(e_1,\ldots,e_n)=\det(e_1\ \cdots\ e_n)=\det I=1.
$$

따라서 9.36의 공식이 바로 위의 공식이 된다.

**9.47 예: 행렬식의 명시적 공식**

- $A$가 $2\times 2$ 행렬이면 9.46의 공식은
  $$
  \det A=A_{1,1}A_{2,2}-A_{2,1}A_{1,2}
  $$
  가 된다.

- $A$가 $3\times 3$ 행렬이면 9.46의 공식은

  $$
  \begin{aligned}
  \det A
  &=A_{1,1}A_{2,2}A_{3,3}
  -A_{2,1}A_{1,2}A_{3,3}
  -A_{3,1}A_{2,2}A_{1,3}\\
  &\quad -A_{1,1}A_{3,2}A_{2,3}
  +A_{3,1}A_{1,2}A_{2,3}
  +A_{2,1}A_{3,2}A_{1,3}.
  \end{aligned}
  $$

9.46의 합에는 $n!$개의 항이 있다. $n!$은 매우 빠르게 증가하므로, 이 공식은 $n$이 조금만 커져도 실제 계산 방법으로는 적합하지 않다.

**9.48 상삼각행렬의 행렬식**

$A$가 대각선 성분이 $\lambda_1,\ldots,\lambda_n$인 상삼각행렬이라고 하자. 그러면
$$
\det A=\lambda_1\cdots\lambda_n.
$$

**증명**

$(j_1,\ldots,j_n)\in\text{perm}n$이고 $(j_1,\ldots,j_n)\ne(1,\ldots,n)$이면 어떤 $k\in\{1,\ldots,n\}$에 대해 $j_k>k$이다. 이때 $A$가 상삼각행렬이므로 $A_{j_k,k}=0$이다. 따라서 9.46의 합에서 영이 아닌 기여를 할 수 있는 순열은 $(1,\ldots,n)$뿐이다. 그러므로 $\det A=\lambda_1\cdots\lambda_n$이다.

### 행렬식의 성질

**9.49 행렬식은 곱셈적이다**

(a) $S,T\in\mathcal{L}(V)$이면
$$
\det(ST)=(\det S)(\det T).
$$

(b) $A$와 $B$가 같은 크기의 정사각행렬이면
$$
\det(AB)=(\det A)(\det B).
$$

**증명**

(a) $n=\dim V$라고 하자. $\alpha\in V_{\text{alt}}^{(n)}$이고 $v_1,\ldots,v_n\in V$라고 하자. 그러면

$$
\begin{aligned}
\alpha_{ST}(v_1,\ldots,v_n)
&=\alpha(STv_1,\ldots,STv_n)\\
&=(\det S)\alpha(Tv_1,\ldots,Tv_n)\\
&=(\det S)(\det T)\alpha(v_1,\ldots,v_n).
\end{aligned}
$$

따라서 $\det(ST)=(\det S)(\det T)$이다.

(b) 모든 행렬은 $\mathbb{F}^n$의 표준 기저에 대한 행렬이라고 하자. $\mathcal{M}(S)=A$, $\mathcal{M}(T)=B$가 되도록 $S,T\in\mathcal{L}(\mathbb{F}^n)$를 잡으면 $\mathcal{M}(ST)=AB$이다. 따라서
$$
\det(AB)=\det(ST)=(\det S)(\det T)=(\det A)(\det B).
$$

**9.50 가역성 $\Longleftrightarrow$ 영이 아닌 행렬식**

$T\in\mathcal{L}(V)$가 가역일 필요충분조건은 $\det T\ne 0$인 것이다. 또한 $T$가 가역이면
$$
\det(T^{-1})=\frac{1}{\det T}.
$$

**증명**

먼저 $T$가 가역이라고 하자. 그러면 $TT^{-1}=I$이다. 9.49에 의해
$$
1=\det I=\det(TT^{-1})=(\det T)(\det(T^{-1})).
$$

따라서 $\det T\ne 0$이고 $\det(T^{-1})$는 $\det T$의 곱셈역원이다.

반대로 $\det T\ne 0$이라고 하자. $v\in V$이고 $v\ne 0$이라고 하자. $v,e_2,\ldots,e_n$을 $V$의 기저로 확장하고, $\alpha\in V_{\text{alt}}^{(n)}$를 $\alpha\ne 0$이 되게 잡는다. 9.39에 의해
$$
\alpha(v,e_2,\ldots,e_n)\ne 0.
$$

따라서

$$
\alpha(Tv,Te_2,\ldots,Te_n)
=(\det T)\alpha(v,e_2,\ldots,e_n)\ne 0.
$$

그러므로 $Tv\ne 0$이다. 즉 $T$는 단사이고, 유한차원이므로 가역이다.

정사각행렬 $A$도 $\det A\ne 0$일 필요충분조건으로 가역이다. 이는 $A$에 대응하는 $\mathbb{F}^n$ 위의 연산자에 9.50을 적용하면 된다.

**9.51 고윳값과 행렬식**

$T\in\mathcal{L}(V)$이고 $\lambda\in\mathbb{F}$라고 하자. 그러면 $\lambda$가 $T$의 고윳값일 필요충분조건은
$$
\det(\lambda I-T)=0
$$
인 것이다.

**증명**

$\lambda$가 $T$의 고윳값일 필요충분조건은 $T-\lambda I$가 가역이 아닌 것이다. 이는 $\lambda I-T$가 가역이 아닌 것과 동치이고, 9.50에 의해 $\det(\lambda I-T)=0$과 동치이다.

**9.52 행렬식은 닮음 불변량이다**

$T\in\mathcal{L}(V)$이고 $S:W\to V$가 가역 선형사상이라고 하자. 그러면
$$
\det(S^{-1}TS)=\det T.
$$

**증명**

$n=\dim W=\dim V$라고 하자. $\tau\in W_{\text{alt}}^{(n)}$라고 하자. $\alpha\in V_{\text{alt}}^{(n)}$를
$$
\alpha(v_1,\ldots,v_n)=\tau(S^{-1}v_1,\ldots,S^{-1}v_n)
$$
로 정의한다. $w_1,\ldots,w_n\in W$이면

$$
\begin{aligned}
\tau_{S^{-1}TS}(w_1,\ldots,w_n)
&=\tau(S^{-1}TSw_1,\ldots,S^{-1}TSw_n)\\
&=\alpha(TSw_1,\ldots,TSw_n)\\
&=\alpha_T(Sw_1,\ldots,Sw_n)\\
&=(\det T)\alpha(Sw_1,\ldots,Sw_n)\\
&=(\det T)\tau(w_1,\ldots,w_n).
\end{aligned}
$$

따라서 $\det(S^{-1}TS)=\det T$이다.

**9.53 연산자의 행렬식은 그 행렬의 행렬식과 같다**

$T\in\mathcal{L}(V)$이고 $e_1,\ldots,e_n$이 $V$의 기저라고 하자. 그러면
$$
\det T=\det\mathcal{M}(T,(e_1,\ldots,e_n)).
$$

**증명**

$f_1,\ldots,f_n$을 $\mathbb{F}^n$의 표준 기저라고 하자. $S:\mathbb{F}^n\to V$를 각 $k=1,\ldots,n$에 대해 $Sf_k=e_k$가 되도록 정의한다. 그러면

$$
\mathcal{M}(S^{-1}TS,(f_1,\ldots,f_n))
=\mathcal{M}(T,(e_1,\ldots,e_n)).
\tag{9.54}
$$

따라서

$$
\begin{aligned}
\det T
&=\det(S^{-1}TS)\\
&=\det\mathcal{M}(S^{-1}TS,(f_1,\ldots,f_n))\\
&=\det\mathcal{M}(T,(e_1,\ldots,e_n)).
\end{aligned}
$$

첫 등식은 9.52에서, 둘째 등식은 행렬의 행렬식 정의에서, 셋째 등식은 (9.54)에서 따른다.

**9.55 $\mathbb{F}=\mathbb{C}$이면 행렬식은 고윳값들의 곱이다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. 그러면 $\det T$는 $T$의 고윳값들을 각 중복도만큼 포함하여 모두 곱한 값이다.

**증명**

8.37에 의해 어떤 기저에 대한 $T$의 행렬은 상삼각행렬이고, 그 대각선 성분들은 $T$의 고윳값들이 각 중복도만큼 나타난 것이다. 따라서 9.53과 9.48에 의해 $\det T$는 이 고윳값들의 곱이다.

**9.56 전치, 쌍대, 수반과 행렬식**

(a) $A$가 정사각행렬이면
$$
\det A^{\mathrm{t}}=\det A.
$$

(b) $T\in\mathcal{L}(V)$이면
$$
\det T'=\det T.
$$

(c) $V$가 내적공간이고 $T\in\mathcal{L}(V)$이면
$$
\det(T^*)=\overline{\det T}.
$$

**증명**

(a) $n$이 양의 정수라고 하자. $\alpha:(\mathbb{F}^n)^n\to\mathbb{F}$를
$$
\alpha(v_1,\ldots,v_n)=\det((v_1\ \cdots\ v_n)^{\mathrm{t}})
$$
로 정의한다. 행렬식 공식 9.46은 $\alpha$가 $\mathbb{F}^n$ 위의 $n$-선형 형식임을 보여 준다.

만약 $v_1,\ldots,v_n\in\mathbb{F}^n$ 가운데 $v_j=v_k$인 서로 다른 두 벡터가 있다면, 임의의 $n\times n$ 행렬 $B$에 대해 $(v_1\ \cdots\ v_n)^{\mathrm{t}}B$의 $j$행과 $k$행이 같다. 따라서 $(v_1\ \cdots\ v_n)^{\mathrm{t}}$는 가역이 아니고, $\alpha(v_1,\ldots,v_n)=0$이다. 그러므로 $\alpha$는 교대 $n$-선형 형식이다.

또 표준 기저에 $\alpha$를 적용하면 값이 $1$이다. $\mathbb{F}^n$ 위의 교대 $n$-선형 형식들의 벡터공간은 $1$차원이므로 $\alpha$는 행렬식 함수와 같다. 따라서 (a)가 성립한다.

(b) 등식 $\det T'=\det T$는 (a), 9.53, 3.132에서 따른다.

(c) $V$의 정규직교 기저를 하나 택한다. 이 기저에 대한 $T^*$의 행렬은 $T$의 행렬의 켤레전치행렬이다. 따라서 9.53, 9.46, (a)에 의해 $\det(T^*)=\overline{\det T}$이다.

**9.57 행렬식 계산에 유용한 결과**

(a) 정사각행렬에서 두 열 또는 두 행이 같으면 행렬식은 $0$이다.

(b) 정사각행렬 $A$에서 두 열 또는 두 행을 서로 바꾸어 행렬 $B$를 얻으면
$$
\det A=-\det B.
$$

(c) 정사각행렬의 한 열 또는 한 행에 스칼라를 곱하면 행렬식도 같은 스칼라만큼 곱해진다.

(d) 정사각행렬의 한 열에 다른 열의 스칼라배를 더해도 행렬식은 변하지 않는다.

(e) 정사각행렬의 한 행에 다른 행의 스칼라배를 더해도 행렬식은 변하지 않는다.

**증명**

모든 주장은
$$
v_1,\ldots,v_n\mapsto \det(v_1\ \cdots\ v_n)
$$
와
$$
v_1,\ldots,v_n\mapsto \det((v_1\ \cdots\ v_n)^{\mathrm{t}})
$$
가 둘 다 $\mathbb{F}^n$ 위의 교대 $n$-선형 형식이라는 사실에서 따른다.

예를 들어 (d)를 증명하자. $v_1,\ldots,v_n\in\mathbb{F}^n$이고 $c\in\mathbb{F}$이면

$$
\begin{aligned}
\det(v_1+cv_2\ v_2\ \cdots\ v_n)
&=\det(v_1\ v_2\ \cdots\ v_n)+c\det(v_2\ v_2\ v_3\ \cdots\ v_n)\\
&=\det(v_1\ v_2\ \cdots\ v_n).
\end{aligned}
$$

첫 등식은 다중선형성에서, 둘째 등식은 교대성에서 나온다. 이는 둘째 열의 스칼라배를 첫째 열에 더해도 행렬식이 변하지 않음을 보여 준다. 임의의 두 열에 대해서도 같은 결론이 성립한다. 따라서 (d)가 성립한다.

(e)는 (d)와 9.56(a)에서 따른다. (a), (b), (c)의 증명도 같은 도구를 사용한다.

구체적인 수로 이루어진 행렬의 행렬식을 계산할 때는 9.57을 사용하여 가우스 소거를 적용하는 것이 9.46의 공식을 직접 사용하는 것보다 훨씬 빠르다. 행 교환은 행렬식에 $-1$을 곱하고, 한 행에 영이 아닌 상수를 곱하면 행렬식도 그 상수만큼 곱해지며, 한 행에 다른 행의 스칼라배를 더하는 것은 행렬식을 바꾸지 않는다. 이렇게 상삼각행렬을 만든 뒤, 9.48에 의해 대각선 성분들을 곱하면 행렬식을 얻을 수 있다.

반면 $\det(\lambda I-A)$처럼 기호 $\lambda$가 들어 있는 행렬식은 이런 방식으로 빠르게 계산하기 어렵다. 소거 과정에서 어떤 식이 $0$인지 아닌지를 판단해야 하는데, 기호가 들어 있으면 이 판단이 복잡해지기 때문이다.

**9.58 모든 유니터리 연산자는 절댓값이 $1$인 행렬식을 가진다**

$V$가 내적공간이고 $S\in\mathcal{L}(V)$가 유니터리 연산자라고 하자. 그러면
$$
|\det S|=1.
$$

**증명**

$S$가 유니터리이므로 $I=S^*S$이다. 따라서
$$
1=\det(S^*S)=(\det S^*)(\det S)=\overline{\det S}\det S=|\det S|^2.
$$

그러므로 $|\det S|=1$이다.

**9.59 모든 양의 연산자는 음이 아닌 행렬식을 가진다**

$V$가 내적공간이고 $T\in\mathcal{L}(V)$가 양의 연산자라고 하자. 그러면
$$
\det T\ge 0.
$$

**증명**

스펙트럼 정리(7.29 또는 7.31)에 의해 $V$에는 $T$의 고유벡터들로 이루어진 정규직교 기저가 존재한다. 따라서 9.42의 마지막 항목에 의해 $\det T$는 $T$의 고윳값들을 중복도만큼 곱한 값이다. 양의 연산자의 모든 고윳값은 음이 아닌 실수이므로 $\det T\ge 0$이다.

**9.60 $|\det T|$는 $T$의 특잇값들의 곱이다**

$V$가 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 그러면
$$
|\det T|=\sqrt{\det(T^*T)}=\text{$T$의 특잇값들의 곱}.
$$

**증명**

9.56(c)와 9.49(a)에 의해
$$
|\det T|^2=\overline{\det T}\det T=(\det T^*)(\det T)=\det(T^*T).
$$

양변의 제곱근을 취하면
$$
|\det T|=\sqrt{\det(T^*T)}
$$
이다.

$s_1,\ldots,s_n$을 $T$의 특잇값들의 리스트라고 하자. 그러면 $s_1^2,\ldots,s_n^2$는 $T^*T$의 고윳값들의 리스트이다. 9.42의 마지막 항목을 $T^*T$에 적용하면
$$
\det(T^*T)=s_1^2\cdots s_n^2.
$$

따라서 $|\det T|=s_1\cdots s_n$이다.

**9.61 $T$는 부피를 $|\det T|$배로 바꾼다**

$T\in\mathcal{L}(\mathbb{R}^n)$이고 $\Omega\subset\mathbb{R}^n$이라고 하자. 그러면
$$
\text{volume}T(\Omega)=|\det T|\,\text{volume}\Omega.
$$

이는 7.111과 9.60에서 바로 따른다. 다변수 미적분의 변수변환 공식에서 행렬식의 절댓값이 나타나는 이유가 여기에 있다.

**9.62 $\mathbb{F}=\mathbb{C}$이면 $T$의 특성다항식은 $\det(zI-T)$이다**

$\mathbb{F}=\mathbb{C}$이고 $T\in\mathcal{L}(V)$라고 하자. $T$의 서로 다른 고윳값을 $\lambda_1,\ldots,\lambda_m$이라 하고, 그 중복도를 각각 $d_1,\ldots,d_m$이라고 하자. 그러면
$$
\det(zI-T)=(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}.
$$

**증명**

8.37에 의해 어떤 기저에 대한 $T$의 행렬은 상삼각행렬이고, 대각선에는 각 $\lambda_k$가 정확히 $d_k$번 나타난다. 같은 기저에 대한 $zI-T$의 행렬도 상삼각행렬이며, 대각선에는 각 $z-\lambda_k$가 정확히 $d_k$번 나타난다. 따라서 9.48에 의해 원하는 식이 성립한다.

**9.63 정의: 특성다항식**

$T\in\mathcal{L}(V)$라고 하자. 다항식
$$
z\mapsto \det(zI-T)
$$

을 $T$의 **특성다항식**이라고 한다.

9.46의 공식은 $T\in\mathcal{L}(V)$의 특성다항식이 차수 $\dim V$인 최고차항 계수 $1$의 다항식임을 보여 준다. 9.51에 의해 이 특성다항식의 $\mathbb{F}$ 안의 영점들은 정확히 $T$의 고윳값들이다.

**9.64 케일리-해밀턴 정리**

$T\in\mathcal{L}(V)$이고 $q$가 $T$의 특성다항식이라고 하자. 그러면
$$
q(T)=0.
$$

**증명**

$\mathbb{F}=\mathbb{C}$이면 9.62와 8.29에 의해 $q(T)=0$이다.

이제 $\mathbb{F}=\mathbb{R}$이라고 하자. $V$의 기저를 하나 고정하고, 이 기저에 대한 $T$의 행렬을 $A$라고 하자. $\mathbb{C}^{\dim V}$ 위의 연산자 $S$를 표준 기저에 대한 행렬이 $A$가 되도록 정의한다. 모든 $z\in\mathbb{R}$에 대해
$$
q(z)=\det(zI-T)=\det(zI-A)=\det(zI-S).
$$

따라서 $q$는 $S$의 특성다항식이다. 복소 경우의 결과에 의해
$$
0=q(S)=q(A)=q(T).
$$

케일리-해밀턴 정리에 의해 $T$의 특성다항식은 $T$의 최소다항식의 다항식배이다. 따라서 $T$의 최소다항식의 차수가 $\dim V$와 같으면, $T$의 특성다항식과 최소다항식은 같다.

**9.65 특성다항식, 트레이스, 행렬식**

$T\in\mathcal{L}(V)$라고 하자. $n=\dim V$이면 $T$의 특성다항식은 다음 꼴로 쓸 수 있다.
$$
z^n-(\text{tr}T)z^{n-1}+\cdots+(-1)^n\det T.
$$

**증명**

다항식의 상수항은 $z=0$에서의 값이다. 따라서 $T$의 특성다항식의 상수항은
$$
\det(-T)=(-1)^n\det T
$$
이다.

$V$의 기저를 하나 고정하고, 그 기저에 대한 $T$의 행렬을 $A$라고 하자. 그러면 같은 기저에 대한 $zI-T$의 행렬은 $zI-A$이다. 9.46에서 항등 순열 $(1,\ldots,n)$에 해당하는 항은
$$
(z-A_{1,1})\cdots(z-A_{n,n})
$$
이다. 이 식에서 $z^{n-1}$의 계수는
$$
-(A_{1,1}+\cdots+A_{n,n})=-\text{tr}T
$$
이다. $\text{perm}n$의 다른 순열들에서 오는 항들은 많아야 $n-2$개의 대각선 꼴 인자 $z-A_{k,k}$를 포함하므로 $z^{n-1}$의 계수에 기여하지 않는다.

**9.66 하다마르 부등식**

$A$가 $n\times n$ 행렬이라고 하자. $v_1,\ldots,v_n$을 $A$의 열들이라고 하자. 그러면
$$
|\det A|\le \prod_{k=1}^n\|v_k\|.
$$

**증명**

$A$가 가역이 아니면 $\det A=0$이므로 원하는 부등식이 성립한다.

이제 $A$가 가역이라고 하자. QR 분해(7.58)에 의해 유니터리 행렬 $Q$와 대각선 성분이 모두 양수인 상삼각행렬 $R$이 존재하여
$$
A=QR
$$
이다. 그러면

$$
\begin{aligned}
|\det A|
&=|\det Q|\,|\det R|\\
&=|\det R|\\
&=\prod_{k=1}^n R_{k,k}\\
&\le \prod_{k=1}^n \|R_{\cdot,k}\|\\
&=\prod_{k=1}^n \|QR_{\cdot,k}\|\\
&=\prod_{k=1}^n \|v_k\|.
\end{aligned}
$$

첫 줄은 9.49(b)에서, 둘째 줄은 9.58에서, 셋째 줄은 9.48에서 나온다. 다섯째 줄은 $Q$가 등거리사상이기 때문에 성립한다.

$\mathbb{F}=\mathbb{R}$일 때 이 부등식은 기하적으로 해석할 수 있다. $T\in\mathcal{L}(\mathbb{R}^n)$를 표준 기저 $e_1,\ldots,e_n$에 대해 $Te_k=v_k$가 되게 정의하면, $T$는 표준 상자를 $v_1,\ldots,v_n$이 만드는 평행다면체로 보낸다. 9.61에 의해 이 평행다면체의 부피는 $|\det A|$이다. 하다마르 부등식은 주어진 변 길이들 $\|v_1\|,\ldots,\|v_n\|$을 가진 평행다면체 가운데 부피가 가장 큰 것은 변들이 서로 직교할 때임을 말한다.

**9.67 반데르몽드 행렬식**

$n>1$이고 $\beta_1,\ldots,\beta_n\in\mathbb{F}$라고 하자. 그러면

$$
\det
\begin{pmatrix}
1&\beta_1&\beta_1^2&\cdots&\beta_1^{n-1}\\
1&\beta_2&\beta_2^2&\cdots&\beta_2^{n-1}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&\beta_n&\beta_n^2&\cdots&\beta_n^{n-1}
\end{pmatrix}
=\prod_{1\le j<k\le n}(\beta_k-\beta_j).
$$

**증명**

$1,z,\ldots,z^{n-1}$을 $\mathcal{P}_{n-1}(\mathbb{F})$의 표준 기저라고 하고, $e_1,\ldots,e_n$을 $\mathbb{F}^n$의 표준 기저라고 하자. 선형사상 $S:\mathcal{P}_{n-1}(\mathbb{F})\to\mathbb{F}^n$를
$$
Sp=(p(\beta_1),\ldots,p(\beta_n))
$$
로 정의한다. 위 명제에 나타난 반데르몽드 행렬을 $A$라고 하자. 그러면
$$
A=\mathcal{M}(S,(1,z,\ldots,z^{n-1}),(e_1,\ldots,e_n)).
$$

$T:\mathcal{P}_{n-1}(\mathbb{F})\to\mathcal{P}_{n-1}(\mathbb{F})$를
$$
T1=1
$$
이고 각 $k=1,\ldots,n-1$에 대해
$$
Tz^k=(z-\beta_1)(z-\beta_2)\cdots(z-\beta_k)
$$
가 되게 하는 연산자라고 하자. $B=\mathcal{M}(T,(1,z,\ldots,z^{n-1}),(1,z,\ldots,z^{n-1}))$라고 하자. 그러면 $B$는 대각선 성분이 모두 $1$인 상삼각행렬이다. 따라서 $\det B=1$이다.

$C=\mathcal{M}(ST,(1,z,\ldots,z^{n-1}),(e_1,\ldots,e_n))$라고 하자. 그러면 $C=AB$이고, 따라서
$$
\det A=(\det A)(\det B)=\det C.
$$

정의에 의해 $C$는 다음 행렬이다.

$$
\begin{pmatrix}
1&0&0&\cdots&0\\
1&\beta_2-\beta_1&0&\cdots&0\\
1&\beta_3-\beta_1&(\beta_3-\beta_1)(\beta_3-\beta_2)&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&\beta_n-\beta_1&(\beta_n-\beta_1)(\beta_n-\beta_2)&\cdots&
(\beta_n-\beta_1)\cdots(\beta_n-\beta_{n-1})
\end{pmatrix}.
$$

이 행렬은 전치하면 상삼각행렬이 된다. 9.56(a)와 9.48을 사용하면
$$
\det A=\det C=\prod_{1\le j<k\le n}(\beta_k-\beta_j)
$$
이다.

### 연습문제 9C

1. 증명하거나 반례를 들어라. $S,T\in\mathcal{L}(V)$이면
   $$
   \det(S+T)=\det S+\det T.
   $$

2. 정사각행렬 $A$의 첫째 열이 첫째 성분 $A_{1,1}$을 제외하고 모두 $0$이라고 하자. $A$에서 첫째 행과 첫째 열을 지워 얻은 행렬을 $B$라고 하자. 다음을 보여라.
   $$
   \det A=A_{1,1}\det B
   $$

3. $T\in\mathcal{L}(V)$가 멱영이라고 하자. 다음을 증명하여라.
   $$
   \det(I+T)=1
   $$

4. $S\in\mathcal{L}(V)$라고 하자. $S$가 유니터리일 필요충분조건은
   $$
   |\det S|=\|S\|=1
   $$
   임을 증명하여라.

5. $A$가 다음과 같은 블록 상삼각행렬이라고 하자.

   $$
   A=
   \begin{pmatrix}
   A_1&*&\cdots&*\\
   0&A_2&\cdots&*\\
   \vdots&\vdots&\ddots&\vdots\\
   0&0&\cdots&A_m
   \end{pmatrix},
   $$

   여기서 대각선 위의 각 $A_k$는 정사각행렬이다. 다음을 증명하여라.
   $$
   \det A=(\det A_1)\cdots(\det A_m)
   $$

6. $A=(v_1\ \cdots\ v_n)$이 $n\times n$ 행렬이고 $v_k$가 $A$의 $k$번째 열이라고 하자. $(m_1,\ldots,m_n)\in\text{perm}n$이면

  $$
  \det(v_{m_1}\ \cdots\ v_{m_n})
  =\text{sign}(m_1,\ldots,m_n)\det A
  $$
  임을 보여라.

7. $T\in\mathcal{L}(V)$가 가역이라고 하자. $p$를 $T$의 특성다항식, $q$를 $T^{-1}$의 특성다항식이라고 하자. 영이 아닌 모든 $z\in\mathbb{F}$에 대해
   $$
   q(z)=\frac{1}{p(0)}z^{\dim V}p\left(\frac{1}{z}\right)
   $$
   임을 증명하여라.

8. $T\in\mathcal{L}(V)$가 고윳값을 가지지 않는 연산자라고 하자. 이 경우 반드시 $\mathbb{F}=\mathbb{R}$이다. $\det T>0$임을 증명하여라.

9. $V$가 짝수 차원의 실 벡터공간이고 $T\in\mathcal{L}(V)$이며 $\det T<0$이라고 하자. $T$가 적어도 두 개의 서로 다른 고윳값을 가짐을 증명하여라.

10. $V$가 홀수 차원의 실 벡터공간이고 $T\in\mathcal{L}(V)$라고 하자. 최소다항식을 사용하지 않고 $T$가 고윳값을 가짐을 증명하여라.

11. 증명하거나 반례를 들어라. $\mathbb{F}=\mathbb{R}$, $T\in\mathcal{L}(V)$, $\det T>0$이면 $T$는 제곱근을 가진다.

12. $S,T\in\mathcal{L}(V)$이고 $S$가 가역이라고 하자. $p:\mathbb{F}\to\mathbb{F}$를
    $$
    p(z)=\det(zS-T)
    $$
    로 정의한다. $p$가 차수 $\dim V$인 다항식이고, 이 다항식에서 $z^{\dim V}$의 계수가 $\det S$임을 증명하여라.

13. $\mathbb{F}=\mathbb{C}$, $T\in\mathcal{L}(V)$, $n=\dim V>2$라고 하자. $\lambda_1,\ldots,\lambda_n$을 중복도만큼 포함한 $T$의 고윳값들이라고 하자.

(a) $T$의 특성다항식에서 $z^{n-2}$의 계수를 $\lambda_1,\ldots,\lambda_n$으로 나타내는 공식을 찾아라.

(b) $T$의 특성다항식에서 $z$의 계수를 $\lambda_1,\ldots,\lambda_n$으로 나타내는 공식을 찾아라.

14. $V$가 내적공간이고 $T$가 $V$ 위의 양의 연산자라고 하자. 다음을 증명하여라.
    $$
    \det\sqrt{T}=\sqrt{\det T}
    $$

15. $V$가 내적공간이고 $T\in\mathcal{L}(V)$라고 하자. 극분해를 사용하여 다음을 증명하여라. 단, 9.60의 증명과 다른 증명을 제시하여라.
    $$
    |\det T|=\sqrt{\det(T^*T)}
    $$

16. $T\in\mathcal{L}(V)$라고 하자. $g:\mathbb{F}\to\mathbb{F}$를
    $$
    g(x)=\det(I+xT)
    $$
    로 정의한다. 다음을 보여라.
    $$
    g'(0)=\text{tr}T
    $$

    행렬식의 명시적이지만 복잡한 공식을 사용하지 않는 깔끔한 풀이를 찾아라.

17. $a,b,c$가 양수라고 하자. 다음 타원체의 부피를 구하여라.

    $$
    \left\{(x,y,z)\in\mathbb{R}^3:
    \frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}<1
    \right\}
    $$

    힌트: 부피를 알고 있는 집합 $\Omega\subset\mathbb{R}^3$와 $T(\Omega)$가 위 타원체가 되는 $\mathbb{R}^3$ 위의 연산자 $T$를 찾아라.

18. $A$가 가역 정사각행렬이라고 하자. 하다마르 부등식(9.66)이 등식이 될 필요충분조건은 $A$의 각 열이 다른 모든 열과 직교하는 것임을 증명하여라.

19. $V$가 내적공간이고, $e_1,\ldots,e_n$이 $V$의 정규직교 기저이며, $T\in\mathcal{L}(V)$가 양의 연산자라고 하자.

    (a) 다음을 증명하여라.
    $$
    \det T\le \prod_{k=1}^n\langle Te_k,e_k\rangle
    $$

    (b) $T$가 가역이면, (a)의 부등식이 등식일 필요충분조건은 각 $k=1,\ldots,n$에 대해 $e_k$가 $T$의 고유벡터인 것임을 증명하여라.

20. $A$가 $n\times n$ 행렬이고, 어떤 $c$에 대해 모든 $j,k\in\{1,\ldots,n\}$에서 $|A_{j,k}|\le c$라고 하자. 다음을 증명하여라.
    $$
    |\det A|\le c^n n^{n/2}.
    $$

    행렬식 공식 9.46은 $|\det A|\le c^n n!$을 보여 준다. 그러나 이 연습문제의 추정은 훨씬 더 좋다. 예를 들어 $c=1$, $n=100$이면 $c^n n!\approx 10^{158}$이지만, 이 연습문제의 추정은 훨씬 작은 수 $10^{100}$이다. $n$이 $2$의 거듭제곱인 정수이면 위 부등식은 날카로워서 더 개선할 수 없다.

21. $n$이 양의 정수이고 $\delta:\mathbb{C}^{n,n}\to\mathbb{C}$가 다음을 만족하는 함수라고 하자.
    $$
    \delta(AB)=\delta(A)\delta(B)
    $$
    가 모든 $A,B\in\mathbb{C}^{n,n}$에 대해 성립하고, $A$가 대각행렬이면 $\delta(A)$는 $A$의 대각선 성분들의 곱과 같다고 하자. 그러면 모든 $A\in\mathbb{C}^{n,n}$에 대해
    $$
    \delta(A)=\det A
    $$
    임을 증명하여라. 이 연습문제는 행렬식이 정사각행렬 위에 정의된 함수 가운데 곱셈적이고 대각행렬에서 원하는 값을 가지는 유일한 함수임을 보여 준다.

> 내 초등 수학 강의에서 나는 교육적인 이유로 행렬식을 점점 더 배경으로 밀어냈다. 학생들이 긴 식을 줄이는 데 유용한 공식들을 다루는 능숙함은 얻었지만, 그 의미에는 익숙해지지 못하는 경우가 너무 많았기 때문이다. 계산 기술은 때때로 학생이 주제의 세부를 끝까지 파고들어 숙달하는 일을 막았다.
>
> -- 펠릭스 클라인, *고급 관점에서 본 초등수학: 기하학* --

## 9D 텐서곱

### 두 벡터공간의 텐서곱

이제 $v\in V$와 $w\in W$의 곱을 만들고 싶다는 생각에서 텐서곱을 도입한다. 이 곱은
$$
v\otimes w
$$
로 나타내고, $V\otimes W$라는 새로운 벡터공간의 원소가 될 것이다.

이미 $V$와 $W$의 곱공간 $V\times W$가 있지만, 이것은 여기서 원하는 역할을 하지 못한다. 우리는 새 곱이 보통 곱셈에서 기대하는 분배법칙을 만족하기를 원한다. 즉 $v_1,v_2,v\in V$와 $w_1,w_2,w\in W$에 대해
$$
(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w
$$
이고
$$
v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2
$$

이기를 원한다. 또한 모든 $\lambda\in\mathbb{F}$, $v\in V$, $w\in W$에 대해
$$
\lambda(v\otimes w)=(\lambda v)\otimes w=v\otimes(\lambda w)
$$
이 성립하기를 원한다.

나아가 $e_1,\ldots,e_m$이 $V$의 기저이고 $f_1,\ldots,f_n$이 $W$의 기저이면, 모든 $e_j\otimes f_k$로 이루어진 리스트가 $V\otimes W$의 기저가 되기를 원한다. 그러면
$$
\dim(V\otimes W)=(\dim V)(\dim W)
$$
이어야 한다. 반면 $\dim(V\times W)=\dim V+\dim W$이므로 $V\times W$는 여기서 원하는 공간이 아니다.

자연스럽게 차원 $(\dim V)(\dim W)$을 가지는 벡터공간을 만들기 위해, 먼저 쌍선형 범함수들의 벡터공간을 살펴본다.

**9.68 정의: $V\times W$ 위의 쌍선형 범함수, 벡터공간 $\mathcal{B}(V,W)$**

- $V\times W$ 위의 **쌍선형 범함수**는 함수 $\beta:V\times W\to\mathbb{F}$로서 각 $w\in W$에 대해 $v\mapsto\beta(v,w)$가 $V$ 위의 선형범함수이고, 각 $v\in V$에 대해 $w\mapsto\beta(v,w)$가 $W$ 위의 선형범함수인 것이다.

- $V\times W$ 위의 쌍선형 범함수들의 벡터공간을 $\mathcal{B}(V,W)$로 나타낸다.

$W=V$이면 $V\times W$ 위의 쌍선형 범함수는 $V$ 위의 쌍선형 형식이다. $\mathcal{B}(V,W)$의 덧셈과 스칼라곱은 함수의 일반적인 덧셈과 스칼라곱으로 정의한다.

**9.69 예: 쌍선형 범함수**

- $\varphi\in V'$이고 $\tau\in W'$라고 하자. $\beta:V\times W\to\mathbb{F}$를
  $$
  \beta(v,w)=\varphi(v)\tau(w)
  $$
  로 정의하면 $\beta$는 $V\times W$ 위의 쌍선형 범함수이다.

- $v\in V$이고 $w\in W$라고 하자. $\beta:V'\times W'\to\mathbb{F}$를
  $$
  \beta(\varphi,\tau)=\varphi(v)\tau(w)
  $$
  로 정의하면 $\beta$는 $V'\times W'$ 위의 쌍선형 범함수이다.

- $\beta:V\times V'\to\mathbb{F}$를
  $$
  \beta(v,\varphi)=\varphi(v)
  $$
  로 정의하면 $\beta$는 $V\times V'$ 위의 쌍선형 범함수이다.

- $\varphi\in V'$라고 하자. $\beta:V\times\mathcal{L}(V)\to\mathbb{F}$를
  $$
  \beta(v,T)=\varphi(Tv)
  $$
  로 정의하면 $\beta$는 $V\times\mathcal{L}(V)$ 위의 쌍선형 범함수이다.

- $m,n$이 양의 정수라고 하자. $\beta:\mathbb{F}^{m,n}\times\mathbb{F}^{n,m}\to\mathbb{F}$를
  $$
  \beta(A,B)=\text{tr}(AB)
  $$
  로 정의하면 $\beta$는 $\mathbb{F}^{m,n}\times\mathbb{F}^{n,m}$ 위의 쌍선형 범함수이다.

**9.70 쌍선형 범함수들의 벡터공간의 차원**

$$
\dim\mathcal{B}(V,W)=(\dim V)(\dim W).
$$

**증명**

$e_1,\ldots,e_m$을 $V$의 기저, $f_1,\ldots,f_n$을 $W$의 기저라고 하자. $\beta\in\mathcal{B}(V,W)$에 대해 $\mathcal{M}(\beta)$를 $m\times n$ 행렬로 정의하되, 그 $j$행 $k$열 성분을 $\beta(e_j,f_k)$로 둔다. 그러면 $\beta\mapsto\mathcal{M}(\beta)$는 $\mathcal{B}(V,W)$에서 $\mathbb{F}^{m,n}$으로 가는 선형사상이다.

$C\in\mathbb{F}^{m,n}$에 대해 $V\times W$ 위의 쌍선형 범함수 $\beta_C$를

$$
\beta_C(a_1e_1+\cdots+a_me_m,\;b_1f_1+\cdots+b_nf_n)
=\sum_{k=1}^n\sum_{j=1}^m C_{j,k}a_jb_k
$$
로 정의한다.

그러면 $\beta\mapsto\mathcal{M}(\beta)$와 $C\mapsto\beta_C$는 서로 역인 동형사상이다. 따라서
$$
\dim\mathcal{B}(V,W)=\dim\mathbb{F}^{m,n}=mn=(\dim V)(\dim W).
$$

문헌에는 $V\otimes W$에 대한 여러 정의가 나타난다. 유한차원에서는 차원이 같은 벡터공간들이 동형이므로 이 정의들은 서로 동치이다. 하지만 $v\otimes w$를 기저에 의존하지 않고 정의하려면, $V\otimes W$를 $\mathcal{B}(V,W)$가 아니라 $\mathcal{B}(V',W')$로 정의하는 것이 유리하다.

**9.71 정의: 텐서곱, $V\otimes W$, $v\otimes w$**

- 텐서곱 $V\otimes W$는 $\mathcal{B}(V',W')$로 정의한다.

- $v\in V$와 $w\in W$에 대해 텐서곱 $v\otimes w$는 $V\otimes W$의 원소로서
  $$
  (v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)
  $$
  를 모든 $(\varphi,\tau)\in V'\times W'$에 대해 만족하는 함수이다.

**9.72 두 벡터공간의 텐서곱의 차원**

$$
\dim(V\otimes W)=(\dim V)(\dim W).
$$

**증명**

벡터공간과 그 쌍대공간은 같은 차원을 가지므로
$$
\dim V'=\dim V,\qquad \dim W'=\dim W.
$$

따라서 9.70에 의해
$$
\dim\mathcal{B}(V',W')=(\dim V)(\dim W).
$$

**9.73 텐서곱의 쌍선형성**

$v,v_1,v_2\in V$, $w,w_1,w_2\in W$, $\lambda\in\mathbb{F}$라고 하자. 그러면
$$
(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w
$$
이고
$$
v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2
$$
이며
$$
\lambda(v\otimes w)=(\lambda v)\otimes w=v\otimes(\lambda w).
$$

**증명**

$(\varphi,\tau)\in V'\times W'$라고 하자. 그러면

$$
\begin{aligned}
((v_1+v_2)\otimes w)(\varphi,\tau)
&=\varphi(v_1+v_2)\tau(w)\\
&=\varphi(v_1)\tau(w)+\varphi(v_2)\tau(w)\\
&=(v_1\otimes w)(\varphi,\tau)+(v_2\otimes w)(\varphi,\tau)\\
&=(v_1\otimes w+v_2\otimes w)(\varphi,\tau).
\end{aligned}
$$

따라서 $(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w$이다. 나머지 등식들도 비슷하게 증명된다.

**9.74 $V\otimes W$의 기저**

$e_1,\ldots,e_m$이 $V$의 벡터 리스트이고 $f_1,\ldots,f_n$이 $W$의 벡터 리스트라고 하자.

(a) $e_1,\ldots,e_m$과 $f_1,\ldots,f_n$이 둘 다 일차독립 리스트이면,
$$
\{e_j\otimes f_k\}_{j=1,\ldots,m;\ k=1,\ldots,n}
$$
은 $V\otimes W$의 일차독립 리스트이다.

(b) $e_1,\ldots,e_m$이 $V$의 기저이고 $f_1,\ldots,f_n$이 $W$의 기저이면,
$$
\{e_j\otimes f_k\}_{j=1,\ldots,m;\ k=1,\ldots,n}
$$
은 $V\otimes W$의 기저이다.

**증명**

(a)를 증명하자. $e_1,\ldots,e_m$과 $f_1,\ldots,f_n$이 둘 다 일차독립이라고 하자. 선형사상 보조정리에 의해 $\varphi_1,\ldots,\varphi_m\in V'$와 $\tau_1,\ldots,\tau_n\in W'$가 존재하여

$$
\varphi_j(e_k)=
\begin{cases}
1,& j=k,\\
0,& j\ne k
\end{cases}
$$
이고

$$
\tau_j(f_k)=
\begin{cases}
1,& j=k,\\
0,& j\ne k
\end{cases}
$$
이다.

스칼라들 $a_{j,k}$가

$$
\sum_{k=1}^n\sum_{j=1}^m a_{j,k}(e_j\otimes f_k)=0
\tag{9.75}
$$
을 만족한다고 하자. $(e_j\otimes f_k)(\varphi_M,\tau_N)$은 $j=M$이고 $k=N$이면 $1$이고, 그렇지 않으면 $0$이다. 따라서 (9.75)의 양변을 $(\varphi_M,\tau_N)$에 적용하면 $a_{M,N}=0$을 얻는다. 모든 $M,N$에 대해 이것이 성립하므로 위 리스트는 일차독립이다.

(b)는 (a), 9.72, 그리고 길이가 알맞은 일차독립 리스트는 기저라는 사실에서 따른다.

9.74(b)에 의해 $V\otimes W$의 모든 원소는 $v\otimes w$ 꼴의 원소들의 유한합으로 쓸 수 있다. 그러나 $\dim V>1$이고 $\dim W>1$이면
$$
\{v\otimes w:(v,w)\in V\times W\}\ne V\otimes W
$$
이다.

**9.76 예: $\mathbb{F}^m$의 원소와 $\mathbb{F}^n$의 원소의 텐서곱**

$m,n$이 양의 정수라고 하자. $e_1,\ldots,e_m$을 $\mathbb{F}^m$의 표준 기저, $f_1,\ldots,f_n$을 $\mathbb{F}^n$의 표준 기저라고 하자.

$$
v=(v_1,\ldots,v_m)\in\mathbb{F}^m,\qquad
w=(w_1,\ldots,w_n)\in\mathbb{F}^n
$$
이면

$$
\begin{aligned}
v\otimes w
&=\left(\sum_{j=1}^m v_je_j\right)\otimes
\left(\sum_{k=1}^n w_kf_k\right)\\
&=\sum_{k=1}^n\sum_{j=1}^m (v_jw_k)(e_j\otimes f_k).
\end{aligned}
$$

따라서 9.74(b)가 주는 $\mathbb{F}^m\otimes\mathbb{F}^n$의 기저
$$
\{e_j\otimes f_k\}_{j=1,\ldots,m;\ k=1,\ldots,n}
$$
에 대해 $v\otimes w$의 계수들은 $v_jw_k$이다. 이 수들을 리스트 대신 $m\times n$ 행렬로 쓰면 $v\otimes w$를 다음 행렬과 동일시할 수 있다.

$$
\begin{pmatrix}
v_1w_1&\cdots&v_1w_n\\
\vdots&\ddots&\vdots\\
v_mw_1&\cdots&v_mw_n
\end{pmatrix}.
$$

**9.77 정의: 쌍선형 사상**

$V\times W$에서 벡터공간 $U$로 가는 **쌍선형 사상**은 함수 $\Gamma:V\times W\to U$로서, 각 $w\in W$에 대해 $v\mapsto\Gamma(v,w)$가 $V$에서 $U$로 가는 선형사상이고, 각 $v\in V$에 대해 $w\mapsto\Gamma(v,w)$가 $W$에서 $U$로 가는 선형사상인 것이다.

**9.78 예: 쌍선형 사상**

- $V\times W$ 위의 모든 쌍선형 범함수는 $V\times W$에서 $\mathbb{F}$로 가는 쌍선형 사상이다.

- 함수 $\Gamma:V\times W\to V\otimes W$를
  $$
  \Gamma(v,w)=v\otimes w
  $$
  로 정의하면 $\Gamma$는 $V\times W$에서 $V\otimes W$로 가는 쌍선형 사상이다.

- 함수 $\Gamma:\mathcal{L}(V)\times\mathcal{L}(V)\to\mathcal{L}(V)$를
  $$
  \Gamma(S,T)=ST
  $$
  로 정의하면 $\Gamma$는 쌍선형 사상이다.

- 함수 $\Gamma:V\times\mathcal{L}(V,W)\to W$를
  $$
  \Gamma(v,T)=Tv
  $$
  로 정의하면 $\Gamma$는 쌍선형 사상이다.

**9.79 쌍선형 사상을 선형사상으로 바꾸기**

$U$가 벡터공간이라고 하자.

(a) $\Gamma:V\times W\to U$가 쌍선형 사상이라고 하자. 그러면 다음을 모든 $(v,w)\in V\times W$에 대해 만족하는 유일한 선형사상 $\widehat{\Gamma}:V\otimes W\to U$가 존재한다.
$$
\widehat{\Gamma}(v\otimes w)=\Gamma(v,w)
$$

(b) 반대로 $T:V\otimes W\to U$가 선형사상이라고 하자. 그러면 다음을 모든 $(v,w)\in V\times W$에 대해 만족하는 유일한 쌍선형 사상 $T^\#:V\times W\to U$가 존재한다.
$$
T^\#(v,w)=T(v\otimes w)
$$

**증명**

$e_1,\ldots,e_m$을 $V$의 기저, $f_1,\ldots,f_n$을 $W$의 기저라고 하자. 선형사상 보조정리와 9.74(b)에 의해 다음을 만족하는 유일한 선형사상 $\widehat{\Gamma}:V\otimes W\to U$가 존재한다.
$$
\widehat{\Gamma}(e_j\otimes f_k)=\Gamma(e_j,f_k)
$$

모든 $j=1,\ldots,m$과 $k=1,\ldots,n$에 대해 성립한다.

이제 $v\in V$, $w\in W$라고 하자. 어떤 $a_1,\ldots,a_m,b_1,\ldots,b_n\in\mathbb{F}$에 대해

$$
v=a_1e_1+\cdots+a_me_m,\qquad
w=b_1f_1+\cdots+b_nf_n
$$
이다. 그러면

$$
\begin{aligned}
\widehat{\Gamma}(v\otimes w)
&=\widehat{\Gamma}\left(\sum_{k=1}^n\sum_{j=1}^m a_jb_k(e_j\otimes f_k)\right)\\
&=\sum_{k=1}^n\sum_{j=1}^m a_jb_k\widehat{\Gamma}(e_j\otimes f_k)\\
&=\sum_{k=1}^n\sum_{j=1}^m a_jb_k\Gamma(e_j,f_k)\\
&=\Gamma(v,w).
\end{aligned}
$$

9.74(b)에 의해 이런 선형사상 $\widehat{\Gamma}$는 유일하다. 따라서 (a)가 증명된다.

(b)를 증명하기 위해 $T^\#:V\times W\to U$를
$$
T^\#(v,w)=T(v\otimes w)
$$
로 정의한다. 텐서곱의 쌍선형성과 $T$의 선형성에 의해 $T^\#$는 쌍선형이다. 조건을 만족하는 $T^\#$의 유일성은 명백하다.

9.79(a)를 증명할 때 단순히 모든 $v,w$에 대해 $\widehat{\Gamma}(v\otimes w)=\Gamma(v,w)$로 정의하고 이를 $V\otimes W$ 전체로 선형 확장할 수는 없다. $V\otimes W$의 원소가 $v\otimes w$ 꼴 원소들의 유한합으로 표현되는 방식은 유일하지 않기 때문이다. 위 증명은 기저를 사용하여 이 문제를 피한다. 그러나 모든 $v,w$에 대해 $\widehat{\Gamma}(v\otimes w)=\Gamma(v,w)$가 성립하므로, 최종적으로 얻은 $\widehat{\Gamma}$는 선택한 기저에 의존하지 않는다.

### 내적공간의 텐서곱

**9.80 두 내적공간의 텐서곱 위의 내적**

$V$와 $W$가 내적공간이라고 하자. 그러면 모든 $v,u\in V$와 $w,x\in W$에 대해

$$
\langle v\otimes w,\;u\otimes x\rangle
=\langle v,u\rangle\langle w,x\rangle
$$
을 만족하는 $V\otimes W$ 위의 유일한 내적이 존재한다.

**증명**

$e_1,\ldots,e_m$을 $V$의 정규직교 기저, $f_1,\ldots,f_n$을 $W$의 정규직교 기저라고 하자. $V\otimes W$ 위의 내적을 다음과 같이 정의한다.

$$
\left\langle
\sum_{k=1}^n\sum_{j=1}^m b_{j,k}e_j\otimes f_k,\;
\sum_{k=1}^n\sum_{j=1}^m c_{j,k}e_j\otimes f_k
\right\rangle
=\sum_{k=1}^n\sum_{j=1}^m b_{j,k}\overline{c_{j,k}}.
\tag{9.81}
$$

9.74(b)를 사용하면 9.81이 $V\otimes W$ 위의 내적을 정의함을 확인할 수 있다.

$v,u\in V$와 $w,x\in W$라고 하자. 예를 들어

$$
v=\sum_{j=1}^m v_je_j,\qquad
u=\sum_{j=1}^m u_je_j,\qquad
w=\sum_{k=1}^n w_kf_k,\qquad
x=\sum_{k=1}^n x_kf_k
$$
라고 쓰면

$$
\begin{aligned}
\langle v\otimes w,\;u\otimes x\rangle
&=\left\langle
\sum_{k=1}^n\sum_{j=1}^m v_jw_ke_j\otimes f_k,\;
\sum_{k=1}^n\sum_{j=1}^m u_jx_ke_j\otimes f_k
\right\rangle\\
&=\sum_{k=1}^n\sum_{j=1}^m v_j\overline{u_j}w_k\overline{x_k}\\
&=\left(\sum_{j=1}^m v_j\overline{u_j}\right)
\left(\sum_{k=1}^n w_k\overline{x_k}\right)\\
&=\langle v,u\rangle\langle w,x\rangle.
\end{aligned}
$$

마지막으로 $V\otimes W$의 모든 원소는 $v\otimes w$ 꼴 원소들의 일차결합으로 쓸 수 있으므로, 위 조건을 만족하는 내적은 유일하다.

**9.82 정의: 두 내적공간의 텐서곱 위의 내적**

$V$와 $W$가 내적공간이라고 하자. $V\otimes W$ 위의 내적은 모든 $v,u\in V$와 $w,x\in W$에 대해

$$
\langle v\otimes w,\;u\otimes x\rangle
=\langle v,u\rangle\langle w,x\rangle
$$
을 만족하는 유일한 함수
$$
\langle\cdot,\cdot\rangle:(V\otimes W)\times(V\otimes W)\to\mathbb{F}
$$
이다.

위 식에서 $u=v$, $x=w$를 대입하고 제곱근을 취하면 모든 $v\in V$, $w\in W$에 대해
$$
\|v\otimes w\|=\|v\|\,\|w\|
$$
가 성립한다.

**9.83 $V\otimes W$의 정규직교 기저**

$V$와 $W$가 내적공간이고, $e_1,\ldots,e_m$이 $V$의 정규직교 기저이며, $f_1,\ldots,f_n$이 $W$의 정규직교 기저라고 하자. 그러면
$$
\{e_j\otimes f_k\}_{j=1,\ldots,m;\ k=1,\ldots,n}
$$
은 $V\otimes W$의 정규직교 기저이다.

**증명**

9.74(b)에 의해 위 리스트는 $V\otimes W$의 기저이다. 정규직교성만 확인하면 된다. $j,M\in\{1,\ldots,m\}$이고 $k,N\in\{1,\ldots,n\}$이면

$$
\langle e_j\otimes f_k,\;e_M\otimes f_N\rangle
=\langle e_j,e_M\rangle\langle f_k,f_N\rangle
=\begin{cases}
1,& j=M\text{이고 }k=N,\\
0,& \text{그렇지 않으면}.
\end{cases}
$$

따라서 위 이중 지표 리스트는 $V\otimes W$의 정규직교 기저이다.

### 여러 벡터공간의 텐서곱

두 유한차원 벡터공간의 텐서곱에서 배운 내용을 여러 유한차원 벡터공간의 텐서곱으로 확장한다. 새로운 아이디어는 필요하지 않고 표기만 조금 복잡해진다. 따라서 이 부분에서는 증명을 생략하고, 정의와 결과만 제시한다.

**9.84 표기: $V_1,\ldots,V_m$**

이 소절의 나머지 부분에서 $m$은 $1$보다 큰 정수이고, $V_1,\ldots,V_m$은 유한차원 벡터공간을 뜻한다.

**9.85 정의: $m$-선형 범함수, 벡터공간 $\mathcal{B}(V_1,\ldots,V_m)$**

- $V_1\times\cdots\times V_m$ 위의 **$m$-선형 범함수**는 함수 $\beta:V_1\times\cdots\times V_m\to\mathbb{F}$로서 다른 자리들을 고정하면 각 자리에서 선형범함수인 것이다.

- $V_1\times\cdots\times V_m$ 위의 $m$-선형 범함수들의 벡터공간을 $\mathcal{B}(V_1,\ldots,V_m)$으로 나타낸다.

**9.86 예: $m$-선형 범함수**

각 $k\in\{1,\ldots,m\}$에 대해 $\varphi_k\in V_k'$라고 하자. 함수 $\beta:V_1\times\cdots\times V_m\to\mathbb{F}$를
$$
\beta(v_1,\ldots,v_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)
$$
로 정의하면 $\beta$는 $V_1\times\cdots\times V_m$ 위의 $m$-선형 범함수이다.

**9.87 $m$-선형 범함수들의 벡터공간의 차원**

$$
\dim\mathcal{B}(V_1,\ldots,V_m)=(\dim V_1)\cdots(\dim V_m).
$$

**9.88 정의: 텐서곱, $V_1\otimes\cdots\otimes V_m$, $v_1\otimes\cdots\otimes v_m$**

- 텐서곱 $V_1\otimes\cdots\otimes V_m$은
  $$
  \mathcal{B}(V_1',\ldots,V_m')
  $$
  로 정의한다.

- $v_1\in V_1,\ldots,v_m\in V_m$에 대해 텐서곱 $v_1\otimes\cdots\otimes v_m$은 $V_1\otimes\cdots\otimes V_m$의 원소로서 모든 $(\varphi_1,\ldots,\varphi_m)\in V_1'\times\cdots\times V_m'$에 대해

  $$
  (v_1\otimes\cdots\otimes v_m)(\varphi_1,\ldots,\varphi_m)
  =\varphi_1(v_1)\cdots\varphi_m(v_m)
  $$
  를 만족하는 함수이다.

**9.89 텐서곱의 차원**

$$
\dim(V_1\otimes\cdots\otimes V_m)
=(\dim V_1)\cdots(\dim V_m).
$$

**9.90 $V_1\otimes\cdots\otimes V_m$의 기저**

각 $k=1,\ldots,m$에 대해 $\dim V_k=n_k$이고
$$
e_1^k,\ldots,e_{n_k}^k
$$
가 $V_k$의 기저라고 하자. 그러면
$$
\{e_{j_1}^1\otimes\cdots\otimes e_{j_m}^m\}_{j_1=1,\ldots,n_1;\ \cdots;\ j_m=1,\ldots,n_m}
$$
은 $V_1\otimes\cdots\otimes V_m$의 기저이다.

$m=2$이면 $V_1\otimes V_2$의 원소의 계수들은 두 지표를 가진 배열, 즉 행렬로 나타낼 수 있다. $m>2$이면 $V_1\otimes\cdots\otimes V_m$의 임의의 원소를 나타내려면 $m$개의 지표를 가진 배열이 필요하다. 따라서 텐서곱은 여러 지표로 지정되는 대상들을 다룰 때 자연스럽게 나타난다.

**9.91 정의: $m$-선형 사상**

$V_1\times\cdots\times V_m$에서 벡터공간 $U$로 가는 **$m$-선형 사상**은 함수
$$
\Gamma:V_1\times\cdots\times V_m\to U
$$
로서 다른 자리들을 고정하면 각 자리에서 선형사상인 것이다.

**9.92 $m$-선형 사상을 선형사상으로 바꾸기**

$U$가 벡터공간이라고 하자.

(a) $\Gamma:V_1\times\cdots\times V_m\to U$가 $m$-선형 사상이라고 하자. 그러면 모든 $(v_1,\ldots,v_m)\in V_1\times\cdots\times V_m$에 대해

$$
\widehat{\Gamma}(v_1\otimes\cdots\otimes v_m)
=\Gamma(v_1,\ldots,v_m)
$$
를 만족하는 유일한 선형사상
$$
\widehat{\Gamma}:V_1\otimes\cdots\otimes V_m\to U
$$
가 존재한다.

(b) 반대로 $T:V_1\otimes\cdots\otimes V_m\to U$가 선형사상이라고 하자. 그러면 모든 $(v_1,\ldots,v_m)\in V_1\times\cdots\times V_m$에 대해
$$
T^\#(v_1,\ldots,v_m)=T(v_1\otimes\cdots\otimes v_m)
$$
를 만족하는 유일한 $m$-선형 사상
$$
T^\#:V_1\times\cdots\times V_m\to U
$$
가 존재한다.

### 연습문제 9D

1. $v\in V$이고 $w\in W$라고 하자. $v\otimes w=0$일 필요충분조건은 $v=0$ 또는 $w=0$임을 증명하여라.

2. $\mathbb{R}^3$ 안의 서로 다른 여섯 벡터 $v_1,v_2,v_3,w_1,w_2,w_3$의 예를 들어
   $$
   v_1\otimes w_1+v_2\otimes w_2+v_3\otimes w_3=0
   $$
   이지만 $v_1\otimes w_1$, $v_2\otimes w_2$, $v_3\otimes w_3$ 가운데 어느 하나도 이 리스트의 다른 원소의 스칼라배가 아니게 하여라.

3. $v_1,\ldots,v_m$이 $V$의 일차독립 리스트라고 하자. 또한 $w_1,\ldots,w_m$이 $W$의 리스트이고
   $$
   v_1\otimes w_1+\cdots+v_m\otimes w_m=0
   $$
   이라고 하자. $w_1=\cdots=w_m=0$임을 증명하여라.

4. $\dim V>1$이고 $\dim W>1$이라고 하자. 다음 집합이 $V\otimes W$의 부분공간이 아님을 증명하여라.
   $$
   \{v\otimes w:(v,w)\in V\times W\}
   $$

   따라서 이 경우
   $$
   \{v\otimes w:(v,w)\in V\times W\}\ne V\otimes W.
   $$

5. $m,n$이 양의 정수라고 하자. $v\in\mathbb{F}^m$과 $w\in\mathbb{F}^n$에 대해 9.76처럼 $v\otimes w$를 $m\times n$ 행렬과 동일시한다. 이 동일시 아래에서
   $$
   \{v\otimes w:v\in\mathbb{F}^m,\ w\in\mathbb{F}^n\}
   $$
   이 $\mathbb{F}$의 성분을 가지는 랭크가 $1$ 이하인 모든 $m\times n$ 행렬들의 집합임을 보여라.

6. $m,n$이 양의 정수라고 하자. 연습문제 5와 유사하게, $\mathbb{F}$의 성분을 가지는 랭크가 $2$ 이하인 $m\times n$ 행렬들의 집합을 설명하여라.

7. $\dim V>2$이고 $\dim W>2$라고 하자. 다음을 증명하여라.

   $$
   \{v_1\otimes w_1+v_2\otimes w_2:
   v_1,v_2\in V,\ w_1,w_2\in W\}\ne V\otimes W
   $$

8. $v_1,\ldots,v_m\in V$와 $w_1,\ldots,w_m\in W$가
   $$
   v_1\otimes w_1+\cdots+v_m\otimes w_m=0
   $$
   을 만족한다고 하자. $U$가 벡터공간이고 $\Gamma:V\times W\to U$가 쌍선형 사상이면
   $$
   \Gamma(v_1,w_1)+\cdots+\Gamma(v_m,w_m)=0
   $$
   임을 보여라.

9. $S\in\mathcal{L}(V)$이고 $T\in\mathcal{L}(W)$라고 하자. 모든 $v\in V$와 $w\in W$에 대해 $v\otimes w$를 $Sv\otimes Tw$로 보내는 $V\otimes W$ 위의 유일한 연산자가 존재함을 증명하여라. 관습적으로 이 연산자를 $S\otimes T$라고 부른다.

10. $S\in\mathcal{L}(V)$이고 $T\in\mathcal{L}(W)$라고 하자. $S\otimes T$가 $V\otimes W$ 위의 가역 연산자일 필요충분조건은 $S$와 $T$가 모두 가역인 것이다. 또한 $S$와 $T$가 모두 가역이면
    $$
    (S\otimes T)^{-1}=S^{-1}\otimes T^{-1}
    $$
    임을 증명하여라. 여기서 연습문제 9 뒤의 표기를 사용한다.

11. $V$와 $W$가 내적공간이라고 하자. $S\in\mathcal{L}(V)$이고 $T\in\mathcal{L}(W)$이면
    $$
    (S\otimes T)^*=S^*\otimes T^*
    $$
    임을 증명하여라. 여기서 연습문제 9 뒤의 표기를 사용한다.

12. $V_1,\ldots,V_m$이 유한차원 내적공간이라고 하자. 모든 $(v_1,\ldots,v_m)$과 $(u_1,\ldots,u_m)$에 대해

    $$
    \langle v_1\otimes\cdots\otimes v_m,\;
    u_1\otimes\cdots\otimes u_m\rangle
    =\langle v_1,u_1\rangle\cdots\langle v_m,u_m\rangle
    $$
    을 만족하는 $V_1\otimes\cdots\otimes V_m$ 위의 유일한 내적이 존재함을 증명하여라.

    위 식은 모든 $(v_1,\ldots,v_m)\in V_1\times\cdots\times V_m$에 대해

    $$
    \|v_1\otimes\cdots\otimes v_m\|
    =\|v_1\|\cdots\|v_m\|
    $$
    임을 함의한다.

13. $V_1,\ldots,V_m$이 유한차원 내적공간이고, $V_1\otimes\cdots\otimes V_m$에 연습문제 12의 내적을 넣었다고 하자. 각 $k=1,\ldots,m$에 대해
    $$
    e_1^k,\ldots,e_{n_k}^k
    $$
    가 $V_k$의 정규직교 기저라고 하자. 다음 리스트가 $V_1\otimes\cdots\otimes V_m$의 정규직교 기저임을 보여라.
    $$
    \{e_{j_1}^1\otimes\cdots\otimes e_{j_m}^m\}_{j_1=1,\ldots,n_1;\ \cdots;\ j_m=1,\ldots,n_m}
    $$
