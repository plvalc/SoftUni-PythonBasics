hour = int(input())
day = input()
result = "closed"

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hour < 18:
        result = "open"

print(result)
