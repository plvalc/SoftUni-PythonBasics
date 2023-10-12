change = float(input())
change = int(change * 100)

lv_2 = change // 200
change -= lv_2 * 200
lv_1 = change // 100
change -= lv_1 * 100
st_50 = change // 50
change -= st_50 * 50
st_20 = change // 20
change -= st_20 * 20
st_10 = change // 10
change -= st_10 * 10
st_5 = change // 5
change -= st_5 * 5
st_2 = change // 2
change -= st_2 * 2
st_1 = change // 1
change -= st_1 * 1

total = int(lv_2 + lv_1 + st_50 + st_20 + st_10 + st_5 + st_2 + st_1)
print(total)
