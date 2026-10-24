try:
    x = int(input("enter a number:"))
    print(x)

except ValueError as a:
    print("the error is",a)

try:
    n1 = int(input("enter numer 1:"))
    n2 = int(input("enter numer 2:"))
    result = n1/n2

    print("the answer is:",result)

except ZeroDivisionError as b:
    print("the error is",b)

except ValueError:
    print("invalid error")

except:
    print("invalid input")

else:
    print("no error")

finally:
    print("this line can excecute any how")