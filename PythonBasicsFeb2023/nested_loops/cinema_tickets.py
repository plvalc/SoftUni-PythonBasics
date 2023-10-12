total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    tickets = 0
    if movie_name == "Finish":
        break
    free_seats = int(input())
    for i in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
            tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            tickets += 1
    print(f"{movie_name} - {((tickets / free_seats) * 100):.2f}% full.")

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {total_tickets}')
print(f'{((student_tickets / total_tickets) * 100):.2f}% student tickets.')
print(f'{((standard_tickets / total_tickets) * 100):.2f}% standard tickets.')
print(f'{((kid_tickets / total_tickets) * 100):.2f}% kids tickets.')
