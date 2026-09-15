def calculator():
    a = int(input("enter a first number:"))
    operator = input("enter a operator like +,-,*,/..:")
    b = int(input("enter a second number:"))

    if operator == "+":
      result = a + b 
    elif operator == "-":
       result = a - b
    elif operator == "*": 
       result = a * b
    elif operator == "/":
      if b == 0:
       result = ("you cannot devided by zero")
       result = a / b
    else: ("invalid operator")

    print("Result =", result)

calculator()



