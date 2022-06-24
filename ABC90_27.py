N = int(input())
S = []

for _ in range(N):
    s = input()
    S.append(s)

user = set()

# setのデータ構造を使って要素数の比較をすることで重複の判定をする
for i in range(N):
    tmp1 = len(user)
    user.add(S[i])
    tmp2 = len(user)
    # 重複がなかったら要素数が同じでない
    if tmp1 != tmp2:
        print(i+1)
