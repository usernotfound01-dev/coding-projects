def cube(num):
    cube_of_num=num**3
    return cube_of_num

def div_by_3(x):
    if x % 3 == 0:
        return cube(x)
    else:return False

print(div_by_3(6))
print(div_by_3(55))