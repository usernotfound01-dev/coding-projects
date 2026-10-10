def cube(x):
    return x*x*x

def check(y):
    if y % 3 == 0:
        return cube(y)
    else:
        return False

print(check(27))
print(check(5))
print(cube(5))
