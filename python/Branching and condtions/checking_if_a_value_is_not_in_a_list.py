
# Checking if a value is not in a list

# Admin users
admin_users = ['Mark', 'Tony', 'Steve']

username = input("Please enter your username?")
if username not in admin_users:
    print("You do not  have access.")
else:
    print("Access Granted.")

