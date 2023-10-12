points = int(input())

if points <= 100:
    bonus = 5
elif points > 1000:
    bonus = points * 10/100
else:
    bonus = points * 20/100
if points % 2 == 0:
    bonus += 1
if points % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + points)
