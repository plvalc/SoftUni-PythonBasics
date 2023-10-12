first_letter = input()
last_letter = input()
miss_letter = input()

symbol1 = ''
symbol2 = ''
symbol3 = ''
counter = 0

for letter1 in range(ord(first_letter), ord(last_letter) + 1):
    if chr(letter1) != miss_letter:
        symbol1 = chr(letter1)
    else:
        continue
    for letter2 in range(ord(first_letter), ord(last_letter) + 1):
        if chr(letter2) != miss_letter:
            symbol2 = chr(letter2)
        else:
            continue
        for letter3 in range(ord(first_letter), ord(last_letter) + 1):
            if chr(letter3) != miss_letter:
                symbol3 = chr(letter3)
                counter += 1
                print(symbol1 + symbol2 + symbol3, end=' ')
            else:
                continue
print(counter)
