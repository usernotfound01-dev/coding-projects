completed_count=0
total_chores=4
print (f"you shall complete {total_chores} chores today")
chore_num=1
while completed_count < total_chores:
    if chore_num ==1:
        chore="make your bed"
    elif chore_num==2:
        chore="feed your pet"
    elif chore_num==3:
        chore="take out the trash"
    else:
        chore="cleaned the house"
    ans=input(f"have you finished {chore} yes/no")
    if ans =="yes":
        completed_count +=1
        chore_num+=1

        print("great job chores completed")
    else:
        print("go back and complete them all")
    print("chores remaining",total_chores - completed_count)

test_value=0
saftey_counter=0

while test_value <=1 :
    print("this statment is going to be printed infinite times")
    saftey_counter +=1

    if saftey_counter==3 :
        break

print("the total number of chores you had was",total_chores)
print("the chores you've done was",completed_count)
print("the total number of chores left was",total_chores - completed_count)