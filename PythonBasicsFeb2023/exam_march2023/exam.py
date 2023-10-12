students = int(input())

top_students = 0
good_students = 0
fine_students = 0
fail_students = 0
total_scores = 0


for i in range(students):
    score = float(input())
    total_scores += score

    if score >= 5:
        top_students += 1
    elif score >= 4:
        good_students += 1
    elif score >= 3:
        fine_students += 1
    else:
        fail_students += 1

top_students /= students / 100
good_students /= students / 100
fine_students /= students / 100
fail_students /= students / 100
average = total_scores / students


print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {good_students:.2f}%")
print(f"Between 3.00 and 3.99: {fine_students:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average:.2f}")
