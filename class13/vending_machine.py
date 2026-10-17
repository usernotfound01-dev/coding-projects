def calculation_change(paid,price):
    change=paid - price
    return change

snack_price= 75

print("-------Welcome to the vending machine-------")
print(f"the cost of the snacks is £{snack_price}")
print("you can only enter 1,5, 10 and 25 coins")

total_insertedcoins = 0
coins_inserted = 0

while True:
    coins = int(input("enter 1,5,10 or 25"))

    if coins != 1 and coins != 5 and coins !=10  and coins !=25:
        print("invalid coins try again")
        continue

    total_insertedcoins += coins
    coins_inserted += 1
    print(f"inserted {coins} ,total inserted coins so far {total_insertedcoins}")

    if total_insertedcoins >= snack_price:
        print("enough money")
        break

change_due=calculation_change(total_insertedcoins,snack_price)

print("dispensing your snack price")

if change_due == 0:
    pass
else:
    print(f"here is your change{change_due}")

print("purchase summary")
print("snack price",snack_price)
print("coins inserted",coins_inserted)
print("total paid",total_insertedcoins)
print("change given",change_due)
print("thank for coming")