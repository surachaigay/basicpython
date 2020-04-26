# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# print(name)
# print(age + 5)

set_user = "admin"
set_pass = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == set_user and pwd == set_pass:
    print("Yeh! login success")
else:
    print("Opp! login fail!!!")
