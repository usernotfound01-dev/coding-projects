total_homework=4
original_count=total_homework
print(f"you have {original_count} homework task to finish today")

completed_count=0
task_num=1

while task_num<=total_homework:

    if task_num==1:
        next_task="maths paper"
    elif task_num==2:
        next_task="science reading"
    elif task_num==3:
        next_task="English reading"
    else:
        next_task="coding practice"

    answer=input(f"have you completed your {next_task}? (yes/no):").strip().lower()
    if answer =="yes":
        completed_count+=1
        print(f"good job you have completed {completed_count} out of {original_count} homework tasks")
    else:
        print(f"you have {original_count-completed_count} homework left to complete")


    print("homewwork tasks remaining:",total_homework-task_num)
    print() 

print("all homework completed! good job!")
print("great work finishing your homework today! you can now enjoy")

print("now let safley look into infinte loop")
test_value=0
safety_counter=0

while test_value<0:
    print("this is an infinte loop")
    safety_counter+=1

    if safety_counter>3:
        print("saftey counter reached limit,breaking out of loop")
        break

print("Homework completion summary")
print(f"Total tasks: {original_count}")
print(f"Completed tasks: {completed_count}")
print(f"Remaining tasks: {original_count - completed_count}")
