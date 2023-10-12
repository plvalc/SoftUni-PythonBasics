# Read user input
day = input()
result = "Error"
# Logic
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    result = "Working day"
elif day == "Saturday" or day == "Sunday":
    result = "Weekend"

# Output
print(result)
