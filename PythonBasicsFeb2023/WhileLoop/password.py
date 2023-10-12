user = input()
pwd = input()

while True:
    user_input = input()
    if user_input != pwd:
        continue
    else:
        break
print(f'Welcome {user}!')
