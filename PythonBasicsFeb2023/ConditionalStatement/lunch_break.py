from math import ceil

tv_series = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

spare_time = break_time - lunch_time - rest_time

if spare_time >= episode_time:
    print(f"You have enough time to watch {tv_series} and left with {ceil(spare_time - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series}, you need {ceil(episode_time - spare_time)} more minutes.")
