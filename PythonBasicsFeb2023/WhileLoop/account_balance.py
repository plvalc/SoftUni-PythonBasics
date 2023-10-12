total_sum = 0

while True:
    user_input = input()
    if user_input == "NoMoreMoney":
        break
    user_input = float(user_input)
    if user_input < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {user_input:.2f}')
    total_sum += user_input

print(f'Total: {total_sum:.2f}')
