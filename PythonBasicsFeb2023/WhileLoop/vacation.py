trip_price = float(input())
current_money = float(input())
consistent_days = 0
total_days = 0
has_failed = False

while trip_price > current_money:
    action = input()
    money = float(input())

    if current_money < 0:
        current_money = 0

    if action == 'spend':
        current_money -= money
        if current_money < 0:
            current_money = 0
        consistent_days += 1

    elif action == 'save':
        current_money += money
        consistent_days = 0

    total_days += 1

    if consistent_days >= 5:
        has_failed = True
        break

if has_failed:
    print(f'You can\'t save the money.')
    print(f'{total_days}')
else:
    print(f'You saved the money for {total_days} days.')
