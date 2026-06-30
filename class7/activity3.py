#membership operators
print("please enter the marks")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())
tot=markone+marktwo+markthree+markfour+markfive
avg=int(tot/5)
valid_range=range(0,101)
if avg not in valid_range:
    print("invalid option")
elif avg in range(75,101):
    print("excellent")
elif avg in range(50,75):
    print("good")
elif avg in range(0,50):
    print("poor")


