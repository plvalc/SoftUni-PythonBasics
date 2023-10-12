exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrive_time = arrive_hour * 60 + arrive_min

diff = abs(exam_time - arrive_time)
diff_h = diff // 60
diff_m = diff % 60

if exam_time < arrive_time: # Late
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours after the start")
        else:
            print(f"{diff_h}:{diff_m} hours after the start")

else: # On time or Early
    if diff <= 30:
        print("On time")
    else:
        print("Early")

    if diff < 60:
        print(f"{diff_m} minutes before the start")
    else:
        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours before the start")
        else:
            print(f"{diff_h}:{diff_m} hours before the start")
