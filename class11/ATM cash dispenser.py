pound100=0
pound50=0
pound20=0
pound10=0
pound5=0
pound1=0
cash_dispensed=0
customer_served=0

served= True
while served:
    customer_name=input("Hello please tell me your name")
    amount=int(input(f"{customer_name} Enter the money you want to withdraw "))
    if amount<=0:
        print("that's and invalid option")
        continue
    print(f"dispensing {amount} for {customer_name} ")
    remaning=amount

    ixl=1
    while ixl<=6:
        if ixl==1: value=100
        elif ixl==2: value=50
        elif ixl==3: value=20
        elif ixl==4: value=10
        elif ixl==5: value=5
        elif ixl==6: value=1
        count=remaning // value

        if count>0:
            print(f"{count} bills have been dipensed of {value} = {count * value}")
            remaning-=value * count
            if value==100: pound100 +=count
            elif value==50: pound50 +=count
            elif value==20: pound20 +=count
            elif value==10: pound10 +=count
            elif value==5: pound5 +=count
            elif value==1: pound1 +=count
        ixl+=1
    customer_served+=1
    cash_dispensed+=amount
    print(f"transaction complete {customer_name}")

    next_customer=input("is there anyone else that wants to use the ATM?(yes/no)").strip().lower()
    if next_customer!="yes":
        served=False
    
for note in range(1,7):
    if note==1: value,total=100,pound100
    elif note==2: value,total=50,pound50
    elif note==3: value,total=20,pound20
    elif note==4: value,total=10,pound10
    elif note==5: value,total=5,pound5
    elif note==6: value,total=1,pound1

    if total>0:
        print(f"{value} pounds note dispenced: {total}")
        for i in range (total):
            print("=",end="")
        print("")

print(f"customer served was {customer_served} and total cash dispenced {cash_dispensed}")
