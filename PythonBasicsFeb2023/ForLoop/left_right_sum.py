n = int(input())
left_sum = 0
right_sum = 0

for i in range(n):
    number = int(input())
    left_sum += number

for i in range(n):
    number = int(input())
    right_sum += number

diff = abs(left_sum - right_sum)
if diff == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
