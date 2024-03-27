# Define a list of usernames
usernames = ['admin', 'alice', 'bob', 'charlie', 'david']

# Greet each user
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Remove all usernames from the list
usernames.clear()

# Check if the list is empty after removal
if not usernames:
    print("We need to find some users!")