users = {
    1: {
        "username": "admin",
        "password": "admin",
        "first_name": "Arcris",
        "last_name": "Silang",
        "address": "dasma cavite",
        "age": 23,
        "pets": {
            1:{
                "name": "Brunox",
                "type": "Dragon"
            },
            2: {
                "name": "Phoenixie",
                "type": "Phoenix"
            }
        }
    },
    2:{
        "username": "admin1",
        "password": "1234",
        "first_name": "Ashley",
        "last_name": "Ochoa",
        "address": "dasma cavite",
        "age": 23,
        "pets": {
            1:{
                "name": "Bruno",
                "type": "Dragon"
            },
            2: {
                "name": "Phoenixy",
                "type": "Phoenix"
            }
        }
    },
}

for user in users.values():
    for pet in user['pets'].values():
        print(pet['name'])
    


# print(users[2]["pets"][1]["name"])

# def login(username, password): 


    
#     for user in users:
#         if users[user]['username'] == username and users[user]['password'] == password:
#             print(f"Welcome to NCST Mr. {users[user]['first_name']} {users[user]['last_name']}")
#             break
#         else:
#             print("Invalid username or password")


# if __name__ == "__main__":
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     # Execute the login function
#     login(username, password)


