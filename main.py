import numpy as np

x = np.arange(15, dtype=np.int64).reshape(3, 5) #.arange=Python組み込みのrange()のndarray版 #.reshape=多次元配列に変換
print(x)

x[:,:3:3] = 88
print(x)
x[1:, ::2] = -99 #スライス[start:stop:step]によって、リストや文字列、タプルなどのシーケンスオブジェクトの一部分を選択して取得したり別の値を代入したり
print(x)         #2次元配列の場合、[p:q:r,x:y:z]において、p,q,rは要素であるリストへのスライス、x,y,zはさらにそのリストの中身に対するスライスとなる

y = np.arange(15, dtype=np.int64).reshape(3, 5)
z1 = x.max(axis=1) #axis=1は行に沿った処理指定（行の中で最大値探索）
z2 = y.max(axis=0) #axis=0は列に沿った処理指定（列の中で最大値探索）
print(z1)
print(z2)

rng = np.random.default_rng() #多分乱数生成オブジェクトを作ってる
print(rng)                    #だから返り値がGenerator
samples = rng.normal(size=5)  #.nomal=正規分布からのランダムサンプルの抽出 #size=指定した数だけサンプルを抽出
print(samples)

e_input = np.zeros(15)
print(e_input)
print(e_input.reshape(3,5))