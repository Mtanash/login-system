commands = [
    "exit > exit the program",
    "help > show all the commands",
    "create account > to create a new user",
    "login > to login to your account",
    "logout > to logout your account"
]

current_user = {
    "name": None,
    "password": None,
}


def save_user_data(username, email, password):
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(f"{username} {email} {password} \n")
    accounts_file.close()
    print("Account created sucessfully!")


def user_exist(username, password):
    accounts_file = open("accounts.txt", "r")
    accounts_file_data = accounts_file.readlines()
    exist = False
    for i in range(len(accounts_file_data)):
        splited_data = accounts_file_data[i].split()
        if username == splited_data[0] and password == splited_data[2]:
            exist = True
            break
    accounts_file.close()
    return exist


def log_in():

    user_name = input("Enter your user name:>> ")
    password = input("Enter your user password:>> ")
    # read data
    if user_exist(user_name, password):
        current_user["name"] = user_name
        current_user["password"] = password
        print("You logged in sucessfully. Welcome %s" % user_name)
    else:
        print("Account does not exist or you entered user name or password wrong!")


def log_out():
    current_user["name"] = None
    print("You logged out.")


while True:
    if current_user["name"] == None:
        user_input = input("Enter a command or type help :>> ").lower()
    else:
        user_input = input(
            "(Welcome: %s) Enter a command or type help :>> " % current_user["name"]).lower()

    if user_input == "exit":
        break
    elif user_input == 'help':
        for i in range(len(commands)):
            print(commands[i])
    elif user_input == "create account":
        user_name = input("Enter user name :>> ")
        if len(user_name) < 4:
            print("this user name is too short. Enter a valid user name")
            user_name = input("Enter user name :>> ")
        email = input("Enter a valid email :>> ")
        if "@" not in email:
            print("The email you entered is not valid. Please enter email again")
            email = input("Enter a valid email :>> ")
        password1 = input("Enter password :>> ")
        password2 = input("Confirm password :>> ")
        if password2 != password1 or len(password1) < 4:
            print(
                "password does not match or it's too small. Please enter password again")
            password1 = input("Enter password :>> ")
            password2 = input("Confirm password :>> ")
        # save data
        save_user_data(user_name, email, password1)

    elif user_input == "login":
        log_in()
    elif user_input == "logout":
        log_out()
    else:
        print("I don't understand.\
        Please enter a valid command or type 'help'.")
