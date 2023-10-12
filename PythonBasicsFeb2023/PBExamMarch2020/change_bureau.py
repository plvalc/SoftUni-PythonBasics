btc_qty = int(input())
cny_qty = float(input())
commission = float(input())

bgn_1 = btc_qty * 1168
usd = cny_qty * 0.15
bgn_2 = usd * 1.76

eur = (bgn_1 + bgn_2) / 1.95

result = eur * ((100 - commission) / 100)

print(f"{result:.2f}")
