nylon_qty = int(input())
paint_qty = int(input())
thinner_qty = int(input())
work_hours = int(input())

total_price = (nylon_qty + 2) * 1.5 + paint_qty * 1.1 * 14.5 + thinner_qty * 5 + 0.4
total_price += (total_price * 0.3) * work_hours
print(total_price)
