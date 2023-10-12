flower_type = input()
flower_qty = int(input())
budget = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = flower_qty * 5
elif flower_type == "Dahlias":
    total_price = flower_qty * 3.8
elif flower_type == "Tulips":
    total_price = flower_qty * 2.8
elif flower_type == "Narcissus":
    total_price = flower_qty * 3
elif flower_type == "Gladiolus":
    total_price = flower_qty * 2.5

if flower_type == "Roses" and flower_qty > 80:
    total_price *= 0.9
elif flower_type == "Dahlias" and flower_qty > 90:
    total_price *= 0.85
elif flower_type == "Tulips" and flower_qty > 80:
    total_price *= 0.85
elif flower_type == "Narcissus" and flower_qty < 120:
    total_price *= 1.15
elif flower_type == "Gladiolus" and flower_qty < 80:
    total_price *= 1.2

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_qty} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
