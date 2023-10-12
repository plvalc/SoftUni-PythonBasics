price_20kg = float(input())
weight = float(input())
days_to_trip = int(input())
luggage_qty = int(input())

total_price = 0

if weight < 10:
    total_price = 0.2 * price_20kg
elif weight <= 20:
    total_price = 0.5 * price_20kg
else:
    total_price = price_20kg

if days_to_trip > 30:
    total_price *= 1.1
elif days_to_trip >= 7:
    total_price *= 1.15
else:
    total_price *= 1.4

total_price *= luggage_qty

print(f'The total price of bags is: {total_price:.2f} lv.')
