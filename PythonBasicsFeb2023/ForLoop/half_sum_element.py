n = int(input())
max_number = 0
result = 0

for i in range(n):
    number = int(input())
    if i == 0:
        max_number = number
    if max_number < number:
        max_number = number
    result += number

diff = abs(result - 2 * max_number)

if diff == 0:
    print(f"Yes")
    print(f"Sum = {result - max_number}")
else:
    print(f"No")
    print(f"Diff = {diff}")
