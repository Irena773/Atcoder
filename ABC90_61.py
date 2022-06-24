from collections import deque

Q = int(input())

t = []
x = []
for _ in range(Q):
    T,X = map(int, input().split())
    t.append(T)
    x.append(X)

card = deque()

for i in range(Q):
    if t[i] == 1:
        card.appendleft(x[i])
    elif t[i] == 2:
        card.append(x[i])
    else:
        print(card[x[i]-1])
