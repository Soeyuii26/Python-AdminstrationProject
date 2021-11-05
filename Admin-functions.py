admin_info = {"admin1": ("admin0001@gmail.com", "admin%0001"),
 "admin2": ("admin0002@gmail.com", "admin%0002")}
user_info = {"0001": [{"name": "Sue"},
 {"age": 20},
 {"addr": "No1 ABC st, ABC"},
 {"phone": "091234567"}],
 "0002": [{"name": "Mike"},
 {"age": 24},
 {"addr": "No34 DEF st, DEF"},
 {"phone": "092233112"}],
 "0003": [{"name": "Sunny"},
 {"age": 27},
 {"addr": "No302 GHI st, GHI"},
 {"phone": "093423432"}],
 "0004": [{"name": "John"},
 {"age": 22},
 {"addr": "No523 JKL st, JKL"},
 {"phone": "093423535"}],
 "0005": [{"name": "Mark"},
 {"age": 26},
 {"addr": "No783 MNO st, MNO"},
 {"phone": "095378489"}]}


#functions

def functionOne():
    print("Adding User Account")
    print("======================")
    userID = input("Enter User ID")
    userName = input("Enter User Name")
    userAge = input("Enter User Age")
    userAddr = input("Enter User Address")
    userPhone = input("Enter User Phone")
    newUser = {"Name":"{userName}", "Age":{userAge}, "Address":{userAddr}, "Phone":{userPhone}}
    print(f"user_Info + {newUser}")
    
def functionTwo():
    print("Modifying User Account")
    print("======================")
    askUserID = input("Enter User ID to modify >>>")
    while askUserID == user_info.keys():
        print(f"user_info[{askUserID}]")
        modify = input("Enter Information's Title to modify >>>")
        # dict >> list >> dict's key
        """if modify == user_info[{askUserID}][]
        print(f"Enter {modify} to modify >>>")"""
        if modify != user_info[{askUserID}]:
            print(modify)
        else:
            update = input("Enter {modify} to modify >>>")
            continue
        print("[+] Suscessfully Changed!")
        print(f"{user_info[{askUserID}]}")
        #how to show the modified result back??
        
def functionThree():
    print("Removing User Account")
    print("======================")
    remove = input("Enter User ID to delete >>>")
    while remove == True:
        user_info.pop("{remove}")
        print(f"Removing User ID > {remove}")
        print("[+] Suscessfully deleted!")
        for theRest in user_info:
            theRest == user_info.pop("{remove}")
            print (theRest)
    
functions = [ "1) Add User", "2) Modify User", "3) Remove User"]

for key,value in functions.items():
    print(f"{key} : {value}")

chooseNum = int(input("Choose a number>>>"))

while chooseNum == functions.keys[0]:
    print({functionOne})
while chooseNum == functions.keys[1]:
    print({functionTwo})
while chooseNum == functions.keys[2]:
    print({functionThree})

askAdmin = input("Would you like to do some tasks again? Anwer Y/N >>>")
while askAdmin == "Y":
    print({chooseNum})
while askAdmin == "N":
    break

