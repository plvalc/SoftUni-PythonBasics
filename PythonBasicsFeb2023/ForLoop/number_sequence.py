n = int(input())
min_number = 0
max_number = 0

for i in range(n):
    number = int(input())
    if i == 0:
        min_number = number
        max_number = number
    else:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
