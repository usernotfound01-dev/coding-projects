rows=int(input("Enter a number of rows:"))
number=1

print("welcome to Floyd's triangle")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number,end="\t")
        number+=1
    print()
