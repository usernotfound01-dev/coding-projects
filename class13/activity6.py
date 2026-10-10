def total_calc(bill_amount,tip_value):
    tip = bill_amount * tip_value /100
    total_amount = bill_amount + tip

    print("your bill amount is:",bill_amount)
    print("tip amount is :",tip)
    print("your total amount is:",total_amount)

total_calc(100,50)
total_calc(500,5)