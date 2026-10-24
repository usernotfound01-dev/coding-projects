try:
    x = int(input("enter a number:"))
    print(x)

except ValueError as a:
    print("the error is",a)