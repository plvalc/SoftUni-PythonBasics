n = int(input())
number = 0
is_reached = False

for row in range(n):
    for col in range(row + 1):
        number += 1
        print(f'{number}', end=' ')
        if number >= n:
            is_reached = True
            break
    if is_reached:
        break
    print()
