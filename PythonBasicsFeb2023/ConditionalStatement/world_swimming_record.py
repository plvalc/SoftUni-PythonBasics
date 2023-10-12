from math import floor

record = float(input())
meters = float(input())
seconds_per_meter = float(input())

total_time = meters * seconds_per_meter
delay = floor(meters / 15) * 12.5
total_time += delay

time_difference = abs(total_time - record)

if total_time - record < 0:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time > 0:
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")
