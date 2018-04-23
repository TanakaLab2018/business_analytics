2018/04/23

## 問題3(Powell関数)
以下に定義される**Powell関数** (Powell function)の最小値を初期解(3,-1,0,1)からの探索で求めよ.

<img src="https://latex.codecogs.com/gif.latex?f(x_1,x_2,x_3,x_4)=(x_1-10x_2)^2&plus;5(x_3-x_4)&plus;(x_2-2x_3)^4&plus;10(x_1-x_4)^4" />

## 解
この問題も[問題1](problem_1.md)や[問題2](problem_2.md)と同様である.

Powell関数を作成して**scipy.optimize.minimize**に投げてあげればよい.

[ここのサイト](https://www.sfu.ca/~ssurjano/powell.html)によると, 最小値をとるのは<img src="https://latex.codecogs.com/gif.latex?x_0=(0.,0.,0.,0.)" />であるそう.

[サンプル](code_example/problem_3.py)
