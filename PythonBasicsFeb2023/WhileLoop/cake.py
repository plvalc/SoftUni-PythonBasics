a = int(input())
b = int(input())

cake_size = a * b
is_left = False

while cake_size > 0:
    user_input = input()
    if user_input == 'STOP':
        is_left = True
        break
    cake_size -= int(user_input)

if is_left:
    print(f'{cake_size} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')