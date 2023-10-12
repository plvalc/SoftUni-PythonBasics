days = int(input())
room_type = input()
score = input()

price = 0


if room_type == "room for one person":
    price = (days - 1) * 18
elif room_type == "apartment":
    price = (days - 1) * 25
    if days < 10:
        price *= 0.7
    elif days < 15:
        price *= 0.65
    else:
        price *= 0.5
elif room_type == "president apartment":
    price = (days - 1) * 35
    if days < 10:
        price *= 0.9
    elif days < 15:
        price *= 0.85
    else:
        price *= 0.8

if score == "positive":
    price *= 1.25
elif score == "negative":
    price *= 0.9

print(f"{price:.2f}")
