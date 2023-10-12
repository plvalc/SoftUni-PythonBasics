fruit = input()
set_size = input()
set_qty = int(input())

price = 0

if set_size == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.1
    elif fruit == "Raspberry":
        price = 20
elif set_size == "big":
    if fruit == "Watermelon":
        price = 28.7
    elif fruit == "Mango":
        price = 19.6
    elif fruit == "Pineapple":
        price = 24.8
    elif fruit == "Raspberry":
        price = 15.2

if set_size == "small":
    price = price * 2
elif set_size == "big":
    price = price *5

price *= set_qty

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")
