start_num = int(input())
end_num = int(input())
magic_num = int(input())

combination = 0
is_found = False

for first_num in range(start_num, end_num + 1):
    for second_num in range(start_num, end_num + 1):
        combination += 1
        if first_num + second_num == magic_num:
            is_found = True
            print(f"Combination N:{combination} ({first_num} + {second_num} = {magic_num})")
            break
    if is_found:
        break

else:
    print(f"{combination} combinations - neither equals {magic_num}")
