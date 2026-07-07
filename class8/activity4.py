a=int(input("enter a value:"))
b=int(input("enter a value for b:"))
c=int(input("enter a value for c:"))

avg=(a+b+c)/3
print("the avrage is ",avg)

if avg >a and avg >b and avg >c:
    print(f"{avg} is higher than {a} and {b} and {c}")
elif avg >a and avg >b:
    print(f"{avg} is higher than {a} and {b}")
elif avg >a and avg >c:
    print(f"{avg} is higher than {a} and {c}")
elif avg >b and avg >c:
    print(f"{avg} is higher than {b} and {c}")
elif avg >a:
    print(f"{avg}is just higher than {a}")
elif avg >b:
    print(f"{avg}is just higher than {b}")
elif avg >c:
    print(f"{avg}is just higher than {c}")



