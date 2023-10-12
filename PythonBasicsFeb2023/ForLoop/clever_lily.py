age = int(input())
washer_price = float(input())
toy_price = int(input())

birthday_sum = 10
total_sum = 0
total_toys = 0
toys_sum = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        total_sum += birthday_sum - 1
        birthday_sum += 10
    else:
        total_toys += 1

toys_sum = total_toys * toy_price
total_sum += toys_sum

diff = abs(total_sum - washer_price)

if total_sum >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
