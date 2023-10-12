"""
capital letters 65-90
small letters 97-122
Space 32
"""
secret_msg = ''
secret_word = ''
secret_cmd = ''
is_c = False
is_o = False
is_n = False

while True:
    user_input = input()

    if is_c and is_o and is_n:
        secret_msg += secret_word + ' '
        is_c = False
        is_o = False
        is_n = False
        secret_word = ''

    if user_input == 'End':
        break

    if ord(user_input) == 32 or 65 <= ord(user_input) <= 90 or 97 <= ord(user_input) <= 122:
        if user_input == 'c':
            if is_c:
                secret_word += user_input
            else:
                is_c = True
        elif user_input == 'o':
            if is_o:
                secret_word += user_input
            else:
                is_o = True
        elif user_input == 'n':
            if is_n:
                secret_word += user_input
            else:
                is_n = True

        else:
            secret_word += user_input

print(secret_msg)