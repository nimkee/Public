username = "James"
password = "myPasswordIsDog!"
tries = 0

while tries < 3:
    user_in = input("Enter the username: ")
    print(f"Entered Username: {user_in}")
    pass_in = input("Enter the password: ")

    if user_in == username:
        print("Debug - Username matches")
        if pass_in == password:
            print("Logged in")
            break
        else:
            print("Incorrect password")
    else:
        print("Incorrect Username")
    tries += 1
