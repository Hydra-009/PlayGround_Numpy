import numpy as np

x = np.arange(15, dtype=np.int64).reshape(3, 5) #.arange=Python組み込みのrange()のndarray版 #.reshape=多次元配列に変換
print(x)

x[:,:3:3] = 88
print(x)
x[1:, ::2] = -99 #スライス[start:stop:step]によって、リストや文字列、タプルなどのシーケンスオブジェクトの一部分を選択して取得したり別の値を代入したり
print(x)         #2次元配列の場合、[p:q:r,x:y:z]において、p,q,rは要素であるリストへのスライス、x,y,zはさらにそのリストの中身に対するスライスとなる

x.max(axis=1)
print(x)