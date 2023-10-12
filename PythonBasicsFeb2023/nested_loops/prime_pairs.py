first_start = int(input())
second_start = int(input())
first_offset = int(input())
second_offset = int(input())

for first in range(first_start, first_start + first_offset + 1):
    prime_count = 0
    for i in range(1, first + 1):
        if first % i == 0:
            prime_count += 1
    if prime_count != 2:
        continue

    for second in range(second_start, second_start + second_offset + 1):
        prime_count = 0
        for i in range(1, second + 1):
            if second % i == 0:
                prime_count += 1
        if prime_count != 2:
            continue
        print(f'{first}{second}')
