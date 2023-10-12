number1 = int(input())
number2 = int(input())
operator = input()

result = 0
even = "even"

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    else:
        result = number1 * number2

    if result % 2 != 0:
        even = "odd"

    print(f"{number1} {operator} {number2} = {result} - {even}")

elif operator == "/" and number2 != 0:
    result = number1 / number2
    print(f"{number1} / {number2} = {result:.2f}")

elif operator == "%" and number2 != 0:
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")

elif (operator == "/" or operator == "%") and number2 == 0:
    print(f"Cannot divide {number1} by zero")
