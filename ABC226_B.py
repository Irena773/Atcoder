N = int(input())
a = []
dict = {}
ans = 0
for _ in range(N):
    tmp = list(map(int, input().split())) 
    a.append(tmp[1:])
    element = " ".join([str(_) for _ in tmp[1:]])
    if element not in dict:
        ans += 1
        dict[element] = 1

print(ans)
