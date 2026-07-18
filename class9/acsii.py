print("=== ASCII Value Checker ===")

# Ask the user for one character
character = input("Enter a single character: ")

# Check if only one character was entered
if len(character) == 1:

    # Show the data type
    print("Data type:", type(character))

    # Check the type using the 'is' operator
    if type(character) is str:

        # Find the ASCII value
        ascii_value = ord(character)

        print("Character:", character)
        print("ASCII Value:", ascii_value)

        # Categorise the character
        if character.isalpha():
            print("Category: Letter")

        elif character.isdigit():
            print("Category: Digit")

        elif character.isspace():
            print("Category: Space")

        else:
            print("Category: Symbol")

else:
    print("Please enter only ONE character.")