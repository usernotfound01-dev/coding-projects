import random
player = True
number = str(random.randint(0,3))

print("i have generated a number between 0-3 you'll have to guess it.")
print("if you guess the number correctly you win.")

while player:
    game = input("guess a number between 0-3:")
    if number == game:
        print("you win")
        print("the number was:",number)
        break
    else:
        print("try again")