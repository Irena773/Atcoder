N = int(input())
A = list(map(int, input().split())) 


P = 0
num = 0b0
for i in range(N):
    num += 0b1000
    if A[i] == 1:
        num = num >> 1
    elif A[i] == 2:
        num = num >> 2
    elif A[i] == 3:
        num = num >> 3
    else:
        num = num >> 4
# print(bin(num))
str_base = str(bin(num))
str_base = str_base.replace('0b', '')
# print(str_base)
count = 0
for i in range(len(str_base)):
    if str_base[i] == "1":
        count += 1
print(N - count)
