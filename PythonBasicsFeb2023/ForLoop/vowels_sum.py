input_text = input()
result = 0

text_length = len(input_text)


for i in range(0, text_length):
    if input_text[i] == "a":
        result += 1
    if input_text[i] == "e":
        result += 2
    if input_text[i] == "i":
        result += 3
    if input_text[i] == "o":
        result += 4
    if input_text[i] == "u":
        result += 5

print(result)
