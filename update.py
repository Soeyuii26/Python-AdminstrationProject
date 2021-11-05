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
  
 #ADMIN_LOGIN 
 
gmail = input("Enter gmail here >>> ") 
# if gmail.endswith("@gmail.com"): 
#     print(" Success") 
# else:
while gmail.endswith("@gmail.com") and gmail == admin_info.values[1]:
    continue

for x in admin_info: 
    if gmail != admin_info[x]:
        print(" type again carefully")
        gmail = input("Enter gmail here >>> ")

password = input("Enter password here >>> ") 
# admin = (gmail, password) 

for i in admin_info: 
    if password == admin_info[i]: 
        print("[+] Suscessfully logged in to your account!")
        continue
    else: 
        print("[-] Sorry , Your Gmail and Password didn't match. Try again!") 
        password = input("Enter password here >>> ")
#functions  
  
def functionOne():  
  
    print("Adding User Account")  
    print("======================")  
 
def new_user_info(): 
    new_userId = input("Enter User ID  >>>")  
    new_userName = input("Enter User Name >>>")  
    new_userAge = input("Enter User Age >>>")  
    new_userAddr = input("Enter User Address >>>")  
    new_userPhone = input("Enter User Phone >>>")  
     
    new_user_info = new_userId and new_userName and  new_userAge and new_userAddr and new_userPhone 
    Adding_User_Account = user_info.update (new_user_info)  
     
     
    #[{"name": new_userName }, {"age": new_userAge}, 
     #                    {"addr": new_userAddr }, {"phone": new_userPhone}] 
    print("Suscessfully added new user's account!")   
    print({new_user_info})
    

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
  
#for key,value in functions.items():  
#    print(f"{key} : {value}")  
  
chooseNum = int(input("Choose a number>>>"))  
print(functions)

if chooseNum == 1:  
    functionOne()
    new_user_info() 
if chooseNum == 2: 
    functionTwo() 
if chooseNum == 3: 
    functionThree() 
 
 
askAdmin = input("Would you like to do some tasks again? Type Y if yes or N ,if no>>>")  

while askAdmin == True:
    if askAdmin == "Y" or "y":  
        print({chooseNum})  
    if  askAdmin == "N" or "n": 
        break 
    else: 
        print( "Please just retype Y or N")