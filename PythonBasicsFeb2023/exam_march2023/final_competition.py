dancers_qty = int(input())
scores = float(input())
season = input()
place = input()

money = 0

if place == "Bulgaria":
    money = scores * dancers_qty
elif place == "Abroad":
    money = dancers_qty * scores * 1.5

if place == "Bulgaria":
    if season == "summer":
        money *= 0.95
    elif season == "winter":
        money *= 0.92

elif place == "Abroad":
    if season == "summer":
        money *= 0.9
    elif season == "winter":
        money *= 0.85

charity = money * 0.75
money *= 0.25 / dancers_qty

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money:.2f}")
