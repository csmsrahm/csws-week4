while True:
    age = input("Enter your age (type 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    elif age.isdigit():
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs £10.")
        else:
            print("Your ticket costs £15.")
    else:
        print("Invalid input. Please enter a valid age or 'quit'.")18