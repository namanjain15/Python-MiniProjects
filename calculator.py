def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return "Error: Division by zero" if num2 == 0 else num1 / num2
    return "Invalid operator"

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: "))

print(f"Result: {calculate(a, op, b)}")