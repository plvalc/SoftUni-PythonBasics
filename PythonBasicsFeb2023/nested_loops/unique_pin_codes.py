num1_max = int(input())
num2_max = int(input())
num3_max = int(input())

num1 = 0
num2 = 0
num3 = 0

for i in range(1, num1_max + 1):
    if i % 2 == 0:
        num1 = i
    else:
        continue
    for j in range(2, num2_max + 1):
        count2 = 0
        for k in range(1, j + 1):
            if j % k == 0:
                count2 += 1
        if count2 == 2:
            num2 = j
        else:
            continue
        for m in range(1, num3_max + 1):
            if m % 2 == 0:
                num3 = m
                print(num1, num2, num3)
