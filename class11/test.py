number=21
guess=5

while guess>0:
    num=int(input("Enter a number:"))

    if num ==number:
        print("welldone you guessed it")
        break
    elif num<1:
        print("your five tries are up")
    elif num in range(1,11):
        print("your far off")
    elif num in range(11,19):
        print("your close")
    elif num in range (19,21):
        print("your very close")
    elif num in range (22,30):
        print("your very close")
    else:
        print("your far off")
