n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    input_number = int(input())
    if input_number < 200:
        p1 += 1
    elif input_number < 400:
        p2 += 1
    elif input_number < 600:
        p3 += 1
    elif input_number < 800:
        p4 += 1
    else:
        p5 += 1

p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
