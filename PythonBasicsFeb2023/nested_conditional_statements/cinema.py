screening = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if screening == "Premiere":
    income = cinema_capacity * 12
elif screening == "Normal":
    income = cinema_capacity * 7.5
elif screening == "Discount":
    income = cinema_capacity * 5

print(f"{income:.2f} leva")
