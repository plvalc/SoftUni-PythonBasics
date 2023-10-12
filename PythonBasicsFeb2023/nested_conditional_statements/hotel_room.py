month = input()
nights = int(input())

studio_price = 0
apt_price = 0

if month == "May" or month == "October":
    studio_price = nights * 50
    apt_price = nights * 65

elif month == "June" or month == "September":
    studio_price = nights * 75.2
    apt_price = nights * 68.7

elif month == "July" or month == "August":
    studio_price = nights * 76
    apt_price = nights * 77

if 7 < nights < 14 and (month == "May" or month == "October"):
    studio_price *= 0.95
elif nights > 14 and (month == "May" or month == "October"):
    studio_price *= 0.7
elif nights > 14 and (month == "June" or month == "September"):
    studio_price *= 0.8

if nights > 14:
    apt_price *= 0.9

print(f"Apartment: {apt_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
