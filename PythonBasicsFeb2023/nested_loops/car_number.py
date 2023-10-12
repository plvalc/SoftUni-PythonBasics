start_num = int(input())
end_num = int(input())

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        for k in range(start_num, end_num + 1):
            if (j + k) % 2 != 0:
                continue
            for m in range(start_num, end_num + 1):
                if i <= m:
                    continue
                if (i + m) % 2 == 1:
                    print(f'{i}{j}{k}{m}', end=' ')
