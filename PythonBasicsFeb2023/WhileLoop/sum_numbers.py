number = int(input())
sum_number = 0

while True:
    user_input = int(input())
    sum_number += user_input
    if sum_number >= number:
        break
print(sum_number)
