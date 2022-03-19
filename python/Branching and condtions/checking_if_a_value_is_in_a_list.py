# Names registered

registered_names = ['tony', 'john', 'mike', 'sam']

username = input("Please enter the username would you like to use.")
if username in registered_names:
    print("Username is not available")
else:
    print("username is available")
