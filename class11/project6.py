# Grocery Cost Comparison Tool

# Step 2: Grocery Variables
rice = 5.0
milk = 3.0
fruit = 4.0

baskets = 2
family_members = 4

# Step 3: Use Operator Precedence
basket_cost_per_person = ((rice + milk + fruit) * baskets) / family_members

print("Basket cost per person:", basket_cost_per_person)

# Step 4: Read Distribution Values
total_items = int(input("Enter total number of grocery items: "))
people = int(input("Enter number of family members: "))

# Step 5: Check Divisibility
if total_items % people == 0:
    print("Items can be divided equally.")
else:
    print("Items cannot be divided equally.")

# Step 6: Store Recorded Average Details
recorded_average = 120
wrong_weekly_cost = 150
correct_weekly_cost = 100
weeks = 4

# Step 7: Reconstruct the Recorded Total
recorded_total = recorded_average * weeks
print("Recorded total:", recorded_total)

# Step 8: Correct the Total and Mean
corrected_total = recorded_total - wrong_weekly_cost + correct_weekly_cost
corrected_average = corrected_total / weeks

print("Corrected total:", corrected_total)
print("Corrected average:", corrected_average)

# Step 9: Create Three Store Averages
store_a = 110
store_b = 125
store_c = 140

# Step 10: Compare the Corrected Average
if corrected_average < store_a and corrected_average < store_b and corrected_average < store_c:
    print("Corrected average is lower than all store averages.")

elif corrected_average > store_a and corrected_average > store_b and corrected_average > store_c:
    print("Corrected average is higher than all store averages.")

else:
    print("Corrected average is between the store averages.")

# Step 11: Run and Test Program
print("Program finished.")