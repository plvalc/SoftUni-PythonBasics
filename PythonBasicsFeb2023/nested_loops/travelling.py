while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    while True:
        user_input = float(input())
        budget -= user_input
        if budget <= 0:
            print(f'Going to {destination}!')
            break
