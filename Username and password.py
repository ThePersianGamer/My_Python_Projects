print("Hello! This is a python course for begginers to help people learn python. Make an account to get started.")
user = input("Enter a username: ")
password = input("Enter a password: ")
usercheck = input("Enter your username: ")
passwordcheck = input("Enter your password: ")
if usercheck == user and passwordcheck == password:
    print("Access granted! Enjoy your courses")
else:
    if usercheck != user:
        print("Wrong username. Try again.")
    if passwordcheck != password and usercheck != user:
        print("Wrong password and username. Try again.")