fat = int(input())
protein = int(input())
carb = int(input())
total_calories = int(input())
percent_water = int(input())

total_fat = fat * total_calories / 9
total_protein = protein * total_calories / 4
total_carb = carb * total_calories / 4

total_food = total_fat + total_protein + total_carb

calories = total_calories / total_food

calories *= (100 - percent_water)

print(f'{calories:.4f}')

