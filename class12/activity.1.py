def greeting():
    print("welcome to the lemonade stand")
    print("Freash lemonade, made just for you")

greeting()

price=float(input("enter the price per cup"))
cup=int(input("Enter the price per cup in dollars:"))

def calculate_amount(price,cup):
    total=price*cup
    return total

