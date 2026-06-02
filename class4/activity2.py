amount=int(input("enter the amount you want to withdraw:"))
pound100=amount//100
pound50=(amount%100)//50
pound10=(amount%50)//10

print("the number of fifty pound notes is",pound50)
print("the number of hundred pound notes is",pound100)
print("the number of ten pound notes is",pound10)