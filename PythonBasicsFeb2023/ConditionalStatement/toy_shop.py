trip_price = float(input())
puzzle_qty = int(input())
doll_qty = int(input())
teddy_qty = int(input())
minion_qty = int(input())
truck_qty = int(input())

total_qty = puzzle_qty + doll_qty + teddy_qty + minion_qty + truck_qty
total_price = puzzle_qty * 2.6 + doll_qty * 3 + teddy_qty * 4.1 \
              + minion_qty * 8.2 + truck_qty * 2

if total_qty >= 50:  # qty discount
    total_price *= 75/100

total_price *= 90/100  # After rent

if total_price - trip_price >= 0:
    print(f"Yes! {total_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_price:.2f} lv needed.")
