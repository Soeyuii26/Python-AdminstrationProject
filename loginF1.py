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
 
# while gmail.endswith("@gmail.com") and gmail == admin_info.values():
#     print("Success")
#     continue

# for x in admin_info: 
#     if gmail != admin_info[x]:
#         print(" type again carefully")
#         gmail = input("Enter gmail here >>> ")
#     else:
#         print("Success")

# admin = (gmail, password)  
# for i in admin_info: 
#     if password == admin_info[i]: 
#         print("[+] Suscessfully logged in to your account!")
#     else: 
#         print("[-] Sorry , Your Gmail and Password didn't match. Try again!") 
#         password = input("Enter password here >>> ")
#functions

"""Email Validation and Checking"""
gmail = input("Enter gmail here >>> ")

while gmail.endswith("@gmail.com") and gmail == admin_info["admin1"][0] and gmail == admin_info["admin2"][0]:
    print("[+]Email Success.")

while gmail != admin_info["admin1"][0] and gmail != admin_info["admin2"][0]: 
        print("[-]Type again carefully!")
        gmail = input("Enter gmail here >>> ") 

"""Password Checking with while loops""" 
password = input("Enter password here >>> ")  
while password == admin_info["admin1"][1] and password == admin_info["admin2"][1]:
    print("[+] Suscessfully logged in to your account!") 

while password != admin_info["admin1"][1] and password != admin_info["admin2"][1]: 
    print("[-]Type again carefully!")
    password = input("Enter password here >>> ")

   #both password and email will ask again and again until admin enters correct information
def functionOne():  
  
    print("Adding User Account")  
    print("======================")  
 
def new_user_info(): 
    new_userId = int(input("Enter User ID  >>>")  )
    new_userName = input("Enter User Name >>>")  
    new_userAge = int(input("Enter User Age >>>"))
    new_userAddr = input("Enter User Address >>>") 
    new_userPhone = int(input("Enter User Phone >>>")  )
    #setting int type to variables which must be numbers, others are string type
    #new_user_info = new_userId and new_userName and  new_userAge and new_userAddr and new_userPhone

    new_user_info = {"User ID": new_userId,"Name" : new_userName, "Age" : new_userAge, "Address" : new_userAddr, "Phone" :new_userPhone }
    keep_new_info = {  "User ID": new_userId,"Name" : new_userName, "Age" : new_userAge, "Address" : new_userAddr, "Phone" :new_userPhone }
    Adding_User_Account = user_info.update(keep_new_info)  
     
    print("[+]Suscessfully added new user's account!")
    for x,y in new_user_info.items():  
        print(f"{x} : {y}")   
    # print(new_user_info)
    
    def functionTwo():  
    print("Modifying User Account")  
    print("======================")  
    askUserID = input("Enter User ID to modify >>>")  
    while askUserID == user_info.keys():  
        print(f"user_info[{askUserID}]")  
        modify = input("Enter Information's Title to modify >>>")
        modify_two = input("Enter ??? to modify >>>")

        while modify_two == user_info["{askUserID}"]
        """if modify == user_info[{askUserID}][]  
        print(f"Enter {modify} to modify >>>")"""  
        # if modify != user_info[{askUserID}]:  
        #     print(modify)  
        # else:  
        #     update = input("Enter {modify} to modify >>>")  
        #     continue  
        # print("[+] Suscessfully Changed!")  
        # print(f"{user_info[{askUserID}]}")  
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

print("Here are the functions you can do as an Admin:")     
functions = { "1)" : "Add User", "2)" : "Modify User", "3)" : "Remove User"}  
  
def new_func(functions):
    for key,value in functions.items():  
        print(f"{key} : {value}") #to show what functions are available one by one in the order

#first time function for Admin
new_func(functions) 
chooseNum = int(input("Choose a number>>>"))  
if chooseNum != type(chooseNum):
    print("Enter a number - 1,2 or 3")

if chooseNum == "1":  
    functionOne()
    new_user_info() 
elif chooseNum == "2": 
    functionTwo() 
else: 
    functionThree() 
 
askAdmin = input("Would you like to do some tasks again? Type Y for 'yes' or N for 'no' >>>")  

# Asking if perform again or not with For looping- for everytime a function has done
for answer in askAdmin:
    if askAdmin == "Y" or "y":
        new_func(functions)
        chooseAgain = int(input("Choose a number>>>"))
        print(chooseAgain)

        if chooseAgain != type(chooseAgain):
            print("Enter a number - 1,2 or 3")

        if chooseAgain == "1":  #1 >> function one will work
            functionOne()
            new_user_info() 
        elif chooseAgain == "2": #2 >> function two will work
            functionTwo() 
        else: 
            functionThree() #else >> the only other left is 3 >> function three will work

    if  askAdmin == "N" or "n": 
        break    #if No,then program will take a break
    else: 
        print( "Please retype Y or N")
      
      """Sorry teacher - function 2 and 3 are having errors *sad noises*"""
