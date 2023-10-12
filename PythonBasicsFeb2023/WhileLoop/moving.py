a = int(input())
b = int(input())
c = int(input())

is_done = False
spare_volume = a * b * c

while spare_volume > 0:
    user_input = input()
    if user_input == 'Done':
        is_done = True
        break
    spare_volume -= int(user_input)

if is_done:
    print(f'{spare_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(spare_volume)} Cubic meters more.')
