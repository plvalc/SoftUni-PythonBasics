product = input()
result = "unknown"

if product == "banana" or product == "apple" or product == "kiwi"\
        or product == "cherry"\
        or product == "lemon"\
        or product == "grapes":
    result = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    result = "vegetable"

print(result)
