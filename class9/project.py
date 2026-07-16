print("=== Holiday Activity Planner ===")

holiday = input("What type of holiday are you planning? (beach/mountain/city): ").lower()

if holiday == "beach":
    weather = input("Will it be sunny? (yes/no): ").lower()

    if weather == "yes":
        print("Activity Plan: Go swimming, build sandcastles, and have a picnic!")
    else:
        print("Activity Plan: Visit an aquarium or relax at a beach café.")

elif holiday == "mountain":
    season = input("Is it winter? (yes/no): ").lower()

    if season == "yes":
        print("Activity Plan: Go skiing or snowboarding.")
    else:
        print("Activity Plan: Go hiking and enjoy the scenery.")

elif holiday == "city":
    budget = input("Is your budget high? (yes/no): ").lower()

    if budget == "yes":
        print("Activity Plan: Visit museums, restaurants, and shopping centres.")
    else:
        print("Activity Plan: Explore parks, free attractions, and local markets.")

else:
    print("Sorry, I don't recognise that holiday type.")