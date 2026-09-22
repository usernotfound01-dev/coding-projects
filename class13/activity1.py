def calc_amount(tip_perc,amt):
    tip_pound=tip_perc*amt/100
    total_bill=tip_pound+amt
    print(f"your total bill is {total_bill} pounds")

calc_amount(amt=60,tip_perc=70)