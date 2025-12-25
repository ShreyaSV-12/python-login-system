# Python File-Based Login System
# Description: Simple authenticationsystem using file handling


def load_users():
    users={}
    with open("project 2/users.txt","r") as file:
        for line in file:
            username,password=line.strip().split(",")
            users[username]=password
        return users
    
def login(users):
    try:
        username=input("enter username: ")
        password=input("enter password: ")

        if username in users and users[username]==password:
            print("login successful")
        else:
            print("invalid username or password")

    except Exception as e:
        print("error occured:",e)



users=load_users()
login(users)