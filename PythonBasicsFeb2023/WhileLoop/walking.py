daily_goal = 10000
steps = 0
is_going_home = False

while steps <= daily_goal:
    user_input = input()
    if user_input == 'Going home':
        is_going_home = True
        continue
    user_input = int(user_input)
    steps += user_input

    if is_going_home:
        break

if steps < daily_goal:
    print(f'{daily_goal - steps} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{steps - daily_goal} steps over the goal!')
