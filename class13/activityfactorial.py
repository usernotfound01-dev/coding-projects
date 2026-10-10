def factorial(y):
    if y == 0 or y == 1:
        return 1
    else:
        return y * factorial(y-1)

print("the factorial of 7 is:",factorial(7))
print("the factorial of 67 is:",factorial(67))
print("the factorial of 0 is:",factorial(0))

