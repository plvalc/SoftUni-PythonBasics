fail_threshold = int(input())

sum_grades = 0
problem_counter = 0
failed_counter = 0
has_failed = True
last_problem_name = ''

while failed_counter < fail_threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_counter +=1
    sum_grades += grade
    problem_counter +=1
    last_problem_name = problem_name

if has_failed:
    print(f'You need a break, {fail_threshold} poor grades.')
else:
    print(f'Average score: {sum_grades/problem_counter:.2f}')
    print(f'Number of problems: {problem_counter}')
    print(f'Last problem: {last_problem_name}')
