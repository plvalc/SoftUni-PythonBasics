open_tabs = int(input())
salary = float(input())

fine = 0

for i in range(open_tabs):
    tab_name = input()

    if tab_name == "Facebook":
        fine += 150
    elif tab_name == "Instagram":
        fine += 100
    elif tab_name == "Reddit":
        fine += 50

if salary <= fine:
    print(f"You have lost your salary.")
else:
    diff = int(salary - fine)
    print(f"{diff}")
