Integers = list(map(int, input().split()))

count = 0
if Integers[0] == Integers[1] == Integers[2]:
    print(count)
    exit()

while True:
    count += 1
    Integers.sort()
    if Integers[0] < Integers[1]:
        Integers[0] += 2
    else:
        Integers[0] += 1
        Integers[1] += 1
    if Integers[0] == Integers[1] == Integers[2]:
        break

print(count)
