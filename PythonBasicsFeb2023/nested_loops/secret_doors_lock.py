a = int(input())    # 1__
b = int(input())    # _1_
c = int(input())    # __1

for x in range(2, 10, 2):
    if x > a:
        break
    for y in range(2, 8):
        if y > b:
            break
        if y == 4 or y == 6:
            continue
        for z in range(2, 10, 2):
            if z > c:
                break
            print(x, y, z)
