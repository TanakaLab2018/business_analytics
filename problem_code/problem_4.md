2018/04/23
## 問題4

## 解
この節の目的となっている問題である.

考える問題はすなわち以下のような関数<img src="https://latex.codecogs.com/gif.latex?f"/>の最小値を

<img src="https://latex.codecogs.com/gif.latex?f(x,y)=\sum_{i=1}^{7}w_i\sqrt{(x_i-x)^2&plus;(y_i-y)^2}"/>

次のような束縛条件を課して求めればよいということになる.

<img src="https://latex.codecogs.com/gif.latex?(50-x)^2&plus;(50-y)^2\ge40^2"/>

以上のように条件を課した場合での最小値を求める場合は, **scipy.optimize.minimize** の **SLSQP法** を用いることで可能となる([6.4](./../sample_code/6/6_4.py)を参照).

私は家庭の各々のデータを次のように```data```に格納し
```python
#dataの中に[x座標, y座標, 人数]の順で情報を入力
data = np.array([    [24, 54, 2],
                    [60, 63, 1],
                    [1, 84, 2],
                    [23, 100, 3],
                    [84, 48, 4],
                    [15, 64, 5],
                    [52, 74, 4] ])
```

考える関数と束縛条件の式を次のように作成した.

```python
def f(x):
    return np.sum(np.array([data[i,2]*np.sqrt((data[i,0]-x[0])**2+(data[i,1]-x[1])**2) for i in range(len(data))]))
```

```python
def sub(x):
    return  (50-x[0])**2 + (50-x[1])**2 - 40**2
```

そして,
* 条件のない場合の最適解: ```res1```
* 条件のある場合の最適解: ```res2```
として, 計算をおこなった.

[サンプル](code_example/problem_4.py)
