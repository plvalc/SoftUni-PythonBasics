pen_qty = int(input())
marker_qty = int(input())
detergent_liters = int(input())
discount = int(input())

total_price = pen_qty * 5.8 + marker_qty * 7.2 + detergent_liters * 1.2
total_price -= total_price * discount / 100
print(total_price)