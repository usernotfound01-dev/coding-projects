print("welcome to our joruney")
print("enter a 1 for a car and 2 for a bike")
choice=int(input("choose 1 or 2:"))

if choice==1:
    print("Nice choice now choose the type of car u want:")
    print("enter 1 for BMW")
    print("enter 2 for toyota")
    choice2=int(input("Choose one:"))

    if choice2==1:
        print("BMW is a nice choice to pick if you want to impress your friends")
        print("looks great too")
        
    elif choice2==2:
        print("great choice u went for the nice old classy style")

elif choice==2:
    print("Nice you went for th bike choose a style")
    print("enter 1 for BMX bike")
    print("enter 2 for a normal sports bike")
    choice2=int(input("choose one"))

    if choice2==1:
        print("BMX is a nice choice to pick if you want to impress your friends")
        print("looks great too")
        
    elif choice2==2:
        print("great choice u went for a sporty style")
else:
    print("Invalid input")
print("Have a great day with your vehicle")


    
    



