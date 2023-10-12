n = int(input())

for dig1 in range(1, 10):
    for dig2 in range(1, 10):
        if n % (dig1 + dig2) != 0:
            continue
        for dig3 in range(1, 10):
            for dig4 in range(1, 10):
                if dig1 + dig2 == dig3 + dig4:
                    print(f'{dig1}{dig2}{dig3}{dig4}', end=' ')
                else:
                    continue
