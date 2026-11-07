def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b
try:
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
except ValueError:
    print("please enter numbers only")

choice = input("What operation would you like to do Add,Subtract,Multiply,Divide?:")
if choice == "divide":
    print(divide(num1,num2))
elif choice == "add":
    print(add(num1,num2))
elif choice == "subtract":
    print(subtract(num1,num2))
elif choice == "multiply":
    print(multiply(num1,num2))