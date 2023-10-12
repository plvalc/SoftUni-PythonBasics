floors = int(input())
rooms = int(input())
room_type = ''

for floor in range(floors, 0, - 1):
    if floor == floors:
        room_type = 'L'
    elif floor % 2 == 0:
        room_type = 'O'
    else:
        room_type = 'A'
    for room in range(rooms):

        print(f'{room_type}{floor}{room}', end=' ')
    print()
