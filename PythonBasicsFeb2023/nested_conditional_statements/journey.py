budget = float(input())
season = input()

price = 0
place = ""
place_type = "Hotel"

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        place_type = "Camp"
    elif season == "winter":
        price = budget * 0.7
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        price = budget * 0.4
        place_type = "Camp"
    elif season == "winter":
        price = budget * 0.8
else:
    place = "Europe"
    price = budget * 0.9

print(f"Somewhere in {place}")
print(f"{place_type} - {price:.2f}")
