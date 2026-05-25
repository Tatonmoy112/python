# print("Create your account")
# create_user = input("Enter your username: ")
# create_pass = input("Enter your password: ")
# with open("database.txt", "a") as file:
#     file.write(f"{create_user}:{create_pass}\n")
# print("Account created successfully")

with open("database.txt", "r") as file:
    database = file.read()

print("Login now")
login_user = input("Enter your username: ")
login_pass = input("Enter your password: ")

if(login_user in database and login_pass in database):
    print("Login successful")
else:
    print("Login failed")