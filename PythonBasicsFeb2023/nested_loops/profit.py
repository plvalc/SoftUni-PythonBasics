lv1 = int(input())
lv2 = int(input())
lv5 = int(input())
total = int(input())

for z in range(0, lv1 + 1):
    for y in range(0, lv2 + 1):
        for x in range(0, lv5 + 1):
            if x * 5 + y * 2 + z == total:
                print(f'{z} * 1 lv. + {y} * 2 lv. + {x} * 5 lv. = {total} lv.')
