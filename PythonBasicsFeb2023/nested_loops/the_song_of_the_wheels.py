m = int(input())

pwd_count = 0
pwd = ''
is_found = False

for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(1, 10):
            for d in range(1, c):
                if a * b + c * d == m:
                    pwd_count += 1
                    print(f'{a}{b}{c}{d} ', end='')

                    if pwd_count == 4:
                        pwd = f'{a}{b}{c}{d}'
                        is_found = True
if is_found:
    print()
    print(f'Password: {pwd}')
else:
    print()
    print(f'No!')