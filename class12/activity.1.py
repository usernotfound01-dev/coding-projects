def greeting():
    print("welcome to the lemonade stand")
    print("Freash lemonade, made just for you")

greeting()

price=float(input("enter the price per cup"))
cup=int(input("Enter the price per cup in dollars:"))

def calculate_amount(price,cup):
    total=price*cup
    return total

bill_amount=calculate_amount(price,cup)
rounded_amount=round(bill_amount,2)

print(f"total bill is {rounded_amount} :")
pay=float(input("Enter the amount paid by the customer"))

def calculate_change(bill,paid):
    money=paid-bill
    return money

store_change=calculate_change(rounded_amount,pay)
rounded_change=round(store_change,2)

def thank_you_message(num_cups):
    if num_cups>=5:
        return"wow thank you for you suppoting us:"
    else:
        return("thank you for stopping by:")

thankyou=thank_you_message(cup)

print("lemonade recipte:")
print("total amount",rounded_amount)
print("total cups",cup)
print("change",rounded_change)
print(thankyou)