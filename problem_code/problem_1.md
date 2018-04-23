2018/04/23

## 問題1
Rosenbrock関数の最小化を初期値を変えて行え. 実は, Rosenbrock関数は実行可能領域

<img src="https://latex.codecogs.com/gif.latex?-2.048&space;\le&space;x_i&space;\le&space;2.048" />

で定義されている関数である. この範囲外の初期値を与えるとどうなるか実験せよ.

## 解
Rosenbrock関数は複数の変数からなる関数である. なので最小値を求める際は**scipy.optimize.minimize**を使えばよい.

実はこの問題は[6.3](../sample_code/6/6_3.py)でほとんど同様の計算をおこなっている. このサンプルでは, 初期値を<img src="https://latex.codecogs.com/gif.latex?x_0=(2.0,2.0,2.0,2.0,2.0)" />としているので, この部分を書き換えるのみでよい.

今回作成した[プログラム](problem_1.py)では初期値を

<img src="https://latex.codecogs.com/gif.latex?x_0=(-2.0,-1.8,\cdots,1.8,2.0)" />

と設定した場合を解いてみた.
