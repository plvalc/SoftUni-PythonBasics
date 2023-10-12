area = float(input())
price = area * 7.61
price_discount = price * 0.18
client_price = price - price_discount

print(f"The final price is: {client_price} lv.")
print(f"The discount is: {price_discount} lv.")