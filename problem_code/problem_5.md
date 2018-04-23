2018/04/23

## 問題5
鳥が放物線<img src="https://latex.codecogs.com/gif.latex?y=x^2&plus;10"/>を描いて飛んでいる. いま(10,0)の位置にいるカメラマンが, 鳥との距離が最小の地点でシャッターを押そうとしている. 鳥がどの座標に来た時にシャッタを押せばよいだろうか?

## 解
鳥の座標は<img src="https://latex.codecogs.com/gif.latex?(x,x^2&plus;10)"/>と表すことができる. カメラマンの位置は固定されているので, 二人の距離は次のように書ける(かなり助長に書いてしまった...).

```python
def f(x):
    return x**2+10.

def dist(x):
    x_o, y_o = 10., 0 #カメラマンの位置座標
    return np.sqrt((x-x_o)**2+(f(x)-y_o)**2)
```

つまり, この```dist```という関数を最小化する```x```を求めるだけでよい.

[サンプル1](code_example/problem_5.py)

また, 頑張って二行で書いてもみた.

[サンプル2](code_example/problem_5_.py)
