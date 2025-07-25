def calculator():
    print("🔢 Simple Calculator")
    print("Available operations: +, -, *, /, %, **, //")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation: ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        elif op == '%':
            result = num1 % num2
        elif op == '**':
            result = num1 ** num2
        elif op == '//':
            result = num1 // num2
        else:
            result = "Invalid operation!"

        print(f"Result: {result}")
    except ValueError:
        print("❗ Invalid number entered.")

calculator()
