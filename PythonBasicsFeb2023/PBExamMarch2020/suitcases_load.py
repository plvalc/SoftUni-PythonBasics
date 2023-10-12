capacity = float(input())
suitcase = 0
suitcase_qty = 0
is_end = False

while True:
    user_input = input()
    if user_input == 'End':
        is_end = True
        break
    user_input = float(user_input)
    if (suitcase_qty + 1) % 3 == 0:
        user_input *= 1.1
    if user_input > capacity:
        break
    capacity -= user_input
    suitcase_qty += 1

if is_end:
    print(f'Congratulations! All suitcases are loaded!')
else:
    print(f'No more space!')
print(f'Statistic: {suitcase_qty} suitcases loaded.')
