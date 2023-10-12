budget = float(input())
statist_qty = int(input())
clothing_price = float(input())

decor_price = 10/100 * budget
total_clothing_price = clothing_price * statist_qty

if statist_qty >= 150:
    total_clothing_price *= 90/100

total_price = decor_price + total_clothing_price

if budget - total_price < 0:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
