def user_name(forename, surname, year):
    username_out = year[2:4] + forename[0] + surname

    print(f"Your username is {username_out}")

user_name("Thunder", "VanBrocklin", "2024")

forename = input("Enter your first name: ")
surname = input("Enter your last naem: ")
joined = input("Enter the year you joined the school: ")

user_name(forename, surname, joined)