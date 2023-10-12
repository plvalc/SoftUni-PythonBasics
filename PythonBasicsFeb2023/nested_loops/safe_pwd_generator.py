a = int(input())
b = int(input())
max_pwd = int(input())

pwd_count = 0
dig_a = 35  # chr(35-55)
dig_b = 64  # chr(64-96)
dig_x = 1
dig_y = 1
is_reached = False

for dig_x in range(1, a + 1):
    if is_reached:
        break
    for dig_y in range(1, b + 1):
        print(f'{chr(dig_a)}{chr(dig_b)}{dig_x}{dig_y}{chr(dig_b)}{chr(dig_a)}', end='|')
        pwd_count += 1
        if pwd_count >= max_pwd:
            is_reached = True
            break
        elif is_reached:
            break
        dig_a += 1
        dig_b += 1
        if dig_a > 55:
            dig_a = 35
        if dig_b > 96:
            dig_b = 64
        if dig_x > a or dig_y > b:
            is_reached = True
            break


