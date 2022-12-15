import numexpr
operation = input("Enter number...: ")
result = numexpr.evaluate(operation)

print(f"Result : {result}")
