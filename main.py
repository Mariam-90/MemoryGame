from SystemForLogin import System

def Choose_number():
    print("Choose  number to :\n"
          "1. Login to your account\n"
          "2. Register account\n")

if __name__ == '__main__':
    sys = System()
    while(True):
        Choose_number()
        num = input("Enter number: ")
        print("\n")
        if int(num) == 1:
            username = input("Enter username")
            password = input("Enter password")
            sys.login(username, password)
            #Choose_number()

        elif int(num) == 2:
            username = input("Enter username")
            password = input("Enter password")
            sys.new_accunt(username, password)
            username = input("Enter username")
            password = input("Enter password")
            sys.login(username,password)
            Choose_number()



"""
#print for the client as a message to welcoe to hin in our website
print ("welcome in login page ")

#varibles:
#client / custmoers

#username
username=input("Enter your username:")
#password
password=input("Enter your password :")
#repeat password
repeat_password=input("Enter your password again:")
#phone
phone_number=input("Enter your phone number :")
#birthday
birth_day=input("Enter your birthday :")

#if & else:
if password==repeat_password:
    print("welcome sure!")
    print("your username is :"+username)
    print("your password is created")
    print("your phone is save")
    print("your birthday is save")
else:
    print("Error, your password didn't have the same values, please return again")
"""