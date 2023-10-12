total_sum = int(input())
total_sold = 0
total_cs = 0
total_cc = 0
cs_counter = 0
cc_counter = 0

transaction_count = 0
is_end = False

while True:
    if total_sold >= total_sum:
        break
    user_input = input()
    if user_input == "End":
        is_end = True
        break
    user_input = int(user_input)
    transaction_count += 1

    if transaction_count % 2 == 1:  # Cash payment
        if user_input > 100:
            print(f'Error in transaction!')
            continue
        total_sold += user_input
        total_cs += user_input
        cs_counter += 1
        print(f'Product sold!')
        continue
    else:  # Credit Card payment
        if user_input < 10:
            print(f'Error in transaction!')
            continue
        total_sold += user_input
        total_cc += user_input
        cc_counter += 1
        print(f'Product sold!')
        continue

if is_end:
    print(f'Failed to collect required money for charity.')
else:
    print(f'Average CS: {total_cs / cs_counter :.2f}')
    print(f'Average CC: {total_cc / cc_counter :.2f}')
