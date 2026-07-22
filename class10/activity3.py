print("Welcome to Vrisha's Power Calculator!")
print("Vrisha is very good at maths.")
print("She made this program to help her friends calculate powers.\n")

number = int(input("Enter the number: "))
power = int(input("Enter the power: "))

answer = 1

for i in range(power):
    answer = answer * number

print("\nThe answer is:", answer)
print(number, "raised to the power", power, "is", answer)
print("\nThank you for using Vrisha's Power Calculator!")