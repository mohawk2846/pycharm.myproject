a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operation = input("What are doing(+,-,*,/)???")
result = 0

if operation == "-":
    result = a - b
elif operation == "+":
    result = a + b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
print(f"Result : {result}")
