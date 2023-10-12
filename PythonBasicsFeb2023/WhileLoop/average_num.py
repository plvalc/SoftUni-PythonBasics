n = int(input())

total_sum = 0

for i in range(n):
    user_input = int(input())
    total_sum += user_input

result = total_sum / n
print(f'{result:.2f}')
