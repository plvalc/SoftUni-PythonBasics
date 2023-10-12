det_bottles = int(input())

clean_dishes = 0
clean_pots = 0
total_det = det_bottles * 750
is_det_left = True
cleaning_counter = 0

while True:
    user_input = input()
    if user_input == 'End':
        break

    cleaning_counter += 1
    user_input = int(user_input)
    if cleaning_counter % 3 == 0:
        clean_pots += user_input
        total_det -= 15 * user_input
    else:
        clean_dishes += user_input
        total_det -= 5 * user_input

    if total_det < 0:
        is_det_left = False
        break

if is_det_left:
    print(f'Detergent was enough!')
    print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
    print(f'Leftover detergent {total_det} ml.')
else:
    print(f'Not enough detergent, {abs(total_det)} ml. more necessary!')
