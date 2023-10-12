sum_prime = 0
sum_non_prime = 0

while True:
    user_input = input()
    if user_input == 'stop':
        break
    user_input = int(user_input)
    if user_input < 0:
        print(f"Number is negative.")
    else:
        prime_counter = 0
        for i in range(1, user_input + 1):
            if user_input % i == 0:
                prime_counter += 1
        if prime_counter == 2:
            sum_prime += user_input
        else:
            sum_non_prime += user_input

print(f"Sum of all prime numbers is: {sum_prime}")
print(f'Sum of all non prime numbers is: {sum_non_prime}')
