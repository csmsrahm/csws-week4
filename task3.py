current_users = ['admin', 'alice', 'bob', 'charlie', 'david']
new_users = ['charlie', 'emma', 'frank', 'harry', 'alice']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user}, that username is taken. Please enter a new username.")
    else:
        print(f"Great, {new_user} is available.")