import math
A,B,C = map(int, input().split())

# 立方体なので全部同じ長さにしないといけない
# したがって最大公約数を求めることで一辺の長さが何になるか求める
tmp = math.gcd(A, math.gcd(B,C))

# 上で求めた長さに幅、奥行き、高さがなるようにtmpでわることで切る回数を求める
ans = (A // tmp) -1 + (B // tmp) -1 + (C // tmp) -1 
print(ans)
