men = int(input())
women = int(input())
tables = int(input())

is_full = False

for i in range(1, men + 1):
    if is_full:
        break
    for j in range(1, women + 1):
        tables -= 1
        if tables < 0:
            is_full = True
            break
        print(f'({i} <-> {j}) ', end='')
