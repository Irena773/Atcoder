def base10to(n,b):
    #  //は整数除算 % はあまり
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

N,K= map(int, input().split())


num = str(N)
for i in range(K):
    # 8進数を10進数に変換
    base_10 = int(num,8)
    # 10進数を9進数に変換
    base_9 = str(base10to(base_10,9))
    num = ""
    for j in range(len(base_9)):
        if base_9[j] == "8":
            num += "5"
        else:
            num += base_9[j]
print(num)
