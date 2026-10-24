valid = False
while not valid:
    try:
        n = int(input("enter a number:"))
        while n%2 == 0:
            print("bye")
            n = int(input("enter the number:"))
        valid = True
    except ValueError:
        print(" invalid")
    