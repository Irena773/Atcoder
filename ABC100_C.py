N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(len(A)):
    while A[i] != 1:
        if A[i] % 2 == 0:
            count += 1
            A[i] = A[i] / 2
        else:
            break
print(count)
