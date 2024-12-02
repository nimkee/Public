def user_name(forename, surname, year):
    username_out = year[2:4] + forename[0] + surname

    return username_out

def main():

    forename = input("Enter your first name: ")
    surname = input("Enter your last naem: ")
    joined = input("Enter the year you joined the school: ")

    gen_user_name = user_name(forename, surname, joined)
    print("Your user name is " + gen_user_name)


if __name__ == '__main__':
    main()