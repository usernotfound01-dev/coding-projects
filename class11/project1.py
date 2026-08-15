print("Grocery Billing Queue")

low_price_item=0
medium_price_items=0
high_priced_item=0

customer_served=0
total_sales=0

billing=True

while billing:
    name=str(input("enter customer name:"))
    item_count=int(input(f"hello {name} how many item are u buying?"))

    if item_count<=0:
        print("invalid option please try again.")
        continue

    print(f"billing items for {name}: ")
    customer_total=0
    item_number=1

    while item_number <= item_count:
        item_name=input("enter item name:")
        price=int(input("enter item price:"))
        quantity=int(input("enter item quantity:"))

        if price<=0 or quantity<=0:
            print("invalid option try again")
            continue

        item_total=price*quantity
        print(f" {item_name}: {quantity}: {price} = {item_total}")
        customer_total+= item_total

        if price<50:
            low_price_item += quantity
        elif price<=100:
            medium_price_items += quantity
        else:
            high_priced_item += quantity

        item_number +=1

        customer_served +=1
        total_sales+=customer_total

        print(f"total bill for {name}: {customer_total} ")
        print("billing complete!")

        again=input("next customer? (yes/no):").strip().lower()

        if again!="yes":
            billing=False
        else:
            billing=True

print(" grocery category report")

for slot in range(1,4):
    if slot==1:
        label,total="low price items",low_price_item
    elif slot==2:
        label,total="medium price items",medium_price_items
    else:
        label,total="high price item",high_priced_item

    if total>0:
        print(f" {label}: {total} ",end="")

        for item in range(total):
            print("*",end="")

        print()

print(f"customers served: {customer_served}")
print(f"total sales : {total_sales}")
print("Grocery billing closed. Goodbye")