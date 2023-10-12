total_food = int(input()) * 1000
while True:
    user_input = input()
    if user_input == 'Adopted':
        break
    user_input = int(user_input)
    total_food -= user_input

if total_food >= 0:
    print(f'Food is enough! Leftovers: {total_food} grams.')
else:
    print(f'Food is not enough. You need {abs(total_food)} grams more.')
