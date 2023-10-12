import math
tennis_racket_price = float(input())
tennis_racket_qty = int(input())
sneakers_qty = int(input())

total_tennis_racket_price = tennis_racket_price * tennis_racket_qty
sneakers_price = tennis_racket_price / 6 * sneakers_qty
other_equipment_price = (total_tennis_racket_price + sneakers_price) * 0.2

total_price = total_tennis_racket_price + sneakers_price + other_equipment_price

total_djokovic = total_price / 8
total_sponsors = math.ceil(total_price * 7 / 8)

print(f'Price to be paid by Djokovic {math.floor(total_djokovic)}')
print(f'Price to be paid by sponsors {total_sponsors}')
