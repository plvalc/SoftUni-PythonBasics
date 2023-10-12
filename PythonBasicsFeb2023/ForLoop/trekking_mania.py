group_qty = int(input())

musalla = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_persons = 0

for i in range(group_qty):
    group_persons = int(input())

    if group_persons < 6:
        musalla += group_persons
    elif group_persons < 13:
        montblanc += group_persons
    elif group_persons < 26:
        kilimanjaro += group_persons
    elif group_persons < 41:
        k2 += group_persons
    else:
        everest += group_persons

total_persons = musalla + montblanc + kilimanjaro + k2 + everest
musalla = musalla / total_persons * 100
montblanc = montblanc / total_persons * 100
kilimanjaro = kilimanjaro / total_persons * 100
k2 = k2 / total_persons * 100
everest = everest / total_persons * 100

print(f"{musalla:.2f}%")
print(f"{montblanc:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
