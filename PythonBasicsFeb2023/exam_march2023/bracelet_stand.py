pocket_money = float(input())
daily_profit = float(input())
total_expenses = float(input())
gift_price = float(input())

pocket_money *= 5
daily_profit *= 5
total_money = pocket_money + daily_profit
total_money -= total_expenses


if total_money >= gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(gift_price - total_money):.2f} BGN.")
