x = int(input())
y = int(input())

for number in range(x, y + 1):
    sum_even = 0
    sum_odd = 0
    number = str(number)
    for number_len in range(len(number)):
        digit = number[number_len]
        digit = int(digit)
        if number_len % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    if sum_even == sum_odd:
        print(number, end=' ')
