users = {}
userIdGenerator = 0

def register():
    global userIdGenerator
    print("================Register===============")

    username = input("Enter choosen username: ")

    if any(user_data['username'] == username for user_data in users.values()):
        print("Username already been used")
    else:
        password = input("Enter your choosen password: ")
        userIdGenerator += 1
        users[userIdGenerator] = {
            "username": username,
            "password": password
        }

def login():
    print("===============Enter your username and password================")
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users.values():
        if(user['username'] == username and user['password'] == password):
            return True
        else:
            return False

def  userList():
    for user in users.values:
        print(user)

def main():
    while True:
        print("===========Welcome!=================")
        print("1. Register")
        print("2. Login")
        print("3. User List")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                register()
            case 2:
                if(login()):
                    print("Successfully logon..............")
                else:
                    print("Invalid credentials.................")
            case 4:
                print("Logging out..........")
                break
            case _:
                print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()