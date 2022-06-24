N = int(input())
C = []
P = []
for _ in range(N):
    c,p = map(int, input().split())
    C.append(c)
    P.append(p)
Q = int(input())
L = []
R = []
for _ in range(Q):
    l,r = map(int, input().split())
    # 左側は閉区間なので-1する
    L.append(l-1)
    R.append(r)

tmp1 = 0
tmp2 = 0
sum_scores = [[0,0]]
# 累積和を取る
for i in range(N):
    if C[i] == 1:
        tmp1 += P[i]
    else:
        tmp2 += P[i]
    sum_scores.append([tmp1, tmp2])

# クエリに答える
for j in range(Q):
    A = sum_scores[R[j]][0]-sum_scores[L[j]][0]
    B = sum_scores[R[j]][1]-sum_scores[L[j]][1]
    print(str(A) + " " + str(B))
