# Challenge 2: Unqiue Username

def generate_username(firstname, lastname):
    username = lastname + firstname[0]

    # Check to see if the username already exists
    users_file = open("users.txt", "r")
    usernames = eval(users_file.read())
    users_file.close()

    for count in range(len(usernames)):
        if usernames[count][0] == username:
            username = username + '#'
        return username

first = input("What is your first name?")
last = input("And your last?")
print(generate_username(first, last))