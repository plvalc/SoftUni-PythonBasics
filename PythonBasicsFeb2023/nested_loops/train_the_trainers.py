jury_qty = int(input())
all_scores = 0
tasks = 0

while True:
    user_input = input()
    if user_input == "Finish":
        break
    name = user_input

    total_score = 0
    average_score = 0
    for i in range(jury_qty):
        score = float(input())
        total_score += score
        average_score = total_score / jury_qty
    all_scores += average_score
    tasks += 1
    print(f"{name} - {average_score:.2f}.")

print(f"Student's final assessment is {(all_scores / tasks):.2f}.")
