weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
BMI=weight/(height/100)**2
if BMI<=18.4:
    print("you are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("you are obese")
else:
    print("you are severely obese")