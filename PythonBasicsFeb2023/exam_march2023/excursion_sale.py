sea_qty = int(input())
mountain_qty = int(input())

profit = 0
is_sold = False

while True:
    if sea_qty == 0 and mountain_qty == 0:
        is_sold = True
        break
    place = input()
    if place == "Stop":
        break
    if place == "sea":
        if sea_qty == 0:
            continue
        sea_qty -= 1
        profit += 680
    elif place == "mountain":
        if mountain_qty == 0:
            continue
        mountain_qty -= 1
        profit += 499

if is_sold:
    print(f'Good job! Everything is sold.')
print(f"Profit: {profit} leva.")
