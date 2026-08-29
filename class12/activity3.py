rows=int(input("Enter the number of rows"))
if rows%2==0:
    hdr=rows//2
else:
    hdr=rows//2+1

space=hdr-1
for i in range(1,hdr+1):
    for j in range(space):
        print(end=" ")
    space-=1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num+=1
    print()
space=1
for i  in range(1,hdr):
    for j in range(space):
        print(end=" ")
    space+=1
    num=1
    for j in range(1,2*(hdr-i)):
        print(end=str(num))
        num+=1
    print()
    
        


