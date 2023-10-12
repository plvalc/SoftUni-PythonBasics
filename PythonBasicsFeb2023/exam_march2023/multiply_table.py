n = int(input())

n = str(n)
a = int(n[2])
b = int(n[1])
c = int(n[0])

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")
