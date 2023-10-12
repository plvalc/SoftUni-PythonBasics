walk_minutes = int(input())
walk_qty = int(input())
calories = int(input())

calories_burn = (walk_qty * walk_minutes) * 5

if calories_burn * 2 >= calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")
