shopping_list = [1,2,3,7,6,4]
print("original list:",shopping_list)

count = 0
for i in shopping_list:
    count = count+i

avg = count/len(shopping_list)
print("The sum of the number is:",count)
print("your average is:",avg)

print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[4])