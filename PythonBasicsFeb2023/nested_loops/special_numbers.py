n = int(input())

for i in range(1, 10):
    if n % i != 0:
        continue
    for j in range(1, 10):
        if n % j != 0:
            continue
        for k in range(1, 10):
            if n % k != 0:
                continue
            for l in range(1, 10):
                if n % l != 0:
                    continue
                print(f"{i}{j}{k}{l}", end=" ")
