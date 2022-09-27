users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "Username", "1234")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Bob"])

for user in users:
    if user[1] == "Jose":
        print(user)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print(f"Welcome {username} you have been missed!")
else:
    print("I am sorry, that seems to be incorrect. Please try again!")
