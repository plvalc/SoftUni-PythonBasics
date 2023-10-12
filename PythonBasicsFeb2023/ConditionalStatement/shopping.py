# Read user input
budget = float(input())
gpu_qty = int(input())
cpu_qty = int(input())
ram_qty = int(input())

# Logic
total_price = gpu_qty * 250 + cpu_qty * (35/100 * gpu_qty * 250) + ram_qty * (10/100 * gpu_qty * 250)

if gpu_qty > cpu_qty:
    total_price *= 85/100
if budget - total_price >= 0:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")

# Output
