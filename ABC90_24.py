N,K= map(int, input().split())
A = list(map(int, input().split())) 
B = list(map(int, input().split()))

count = 0
# 各要素の差をとって同じ数列になるには何回操作する必要があるかもとめる
for i in range(len(A)):
    tmp = abs(A[i] - B[i])
    count += tmp

# それがK回以下であるか判定する
if count <= K :
    # 残りの操作回数が偶数であるか判定する(偶数であれば、残りの操作は+1-1をしていればいいだけ)
    if (K - count) % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
