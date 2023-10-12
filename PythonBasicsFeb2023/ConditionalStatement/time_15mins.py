hours = int(input())
minutes = int(input())

time = hours * 60 + minutes
time += 15

hours = time // 60
minutes = time % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
