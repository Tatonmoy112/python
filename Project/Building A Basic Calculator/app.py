def cal():
    num1 = int(input("Enter your first value:"))
    num2 = int(input("Enter your second value:"))
    op = (input("Enter your operator: (+, -, *, /, %, **)>>> "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "**":
        print(num1 ** num2)
    else:
        print("Invalid operator")

cal()