name = input()
grade = 1
average = 0
fails = 0
while True:
    score = float(input())
    if score >= 4:
        grade += 1
        average += score
        if grade > 12:
            print(f'{name} graduated. Average grade: {average/12:.2f}')
            break
    else:
        fails += 1
    if fails > 1:
        print(f'{name} has been excluded at {grade} grade')
        break
