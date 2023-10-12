length = int(input())
width = int(input())
hight = int(input())
percent = float(input())

total_liters = (length * width * hight / 1000) * (1 - percent / 100)
print(total_liters)
