2018/04/23

## 問題2(Beale関数)

以下に定義される**Beale関数**(Beale function)の最小値を初期解(1.0,0.8)からの探索で求めよ.

<img src="https://latex.codecogs.com/gif.latex?f(x_1,x_2)=\sum_{i=1}^{3}\{c_i-x_i(1-(x_2)^{i})\}^2"/>

ただし<img src="https://latex.codecogs.com/gif.latex?c_1=1.5,c_2=2.25,c_3=2.625"/>とする.

## 解
これも[問題1](problem_1.md)と同様の方法で解くことができる.

**scipy** の中にBeale関数が定義されていないか期待したが存在しなかったため, 今回は自分で関数を作る必要がある. 私は以下のように関数を作成した.

```python
def beale(x):
    c = np.array([0, 1.5, 2.25, 2.625]) #c[0]は実際には用いない箇所
    return np.sum([(c[i] - x[0]*(1. - (x[1])**i))**2  for i in range(1,4)])
```

また, 今回は勾配ベクトルは用いない方法で解を計算しようと思う(というより, 勾配ベクトルをどのように計算できるのかがわからない).

教科書では二つの方法(**Nelder-Mead法**, **Powell法**)が紹介されているため, 双方で計算を行ってみた.

ネットで調べたところ, Beale関数は(3.0,0.5)で最小値を得るらしい.

[サンプル](code_example/problem_2.py)
