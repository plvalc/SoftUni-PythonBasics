last_sector = input()
rows_first_sector = int(input())
odd_seats = int(input())

seats_count = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 == 0:
            seats = odd_seats + 2
        else:
            seats = odd_seats
        for seat in range(ord('a'), (ord('a') + seats)):
            seats_count += 1
            print(f'{chr(sector)}{row}{chr(seat)}')
    rows_first_sector += 1
print(seats_count)
