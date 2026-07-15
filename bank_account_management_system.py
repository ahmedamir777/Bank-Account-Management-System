registered_users = {}
def Register():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if username == "0" or password == "0":
        print("The operation is cancelled")
    elif username in registered_users.keys():
        print("There is an account with this username")
    elif len(username)==0:
        print("Please enter a valid username")
    elif len(password)<6:
        print("The password must be at least 6 char lenght long")
    else:
        registered_users[username] = {"Password":password,"Balance":0,"LastTransaction":["none",0,0,"none"]}
        print("The account created successfully")


def Login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if username in registered_users.keys():
        if registered_users[username]["Password"] == password and (username!= "0") and (password != "0"):
            print(f"Welcome Mr {username} Your Balance is {registered_users[username]["Balance"]}")
            Bankmenu(username)
            return 0
        else :
            print("Invalid Password")
            return 1   
    elif username == "0" or password == "0":
        print("The operation is cancelled")
        return 1
    else:
        print("Invalid Username")
        return 1


def Bankmenu(username):
    menu_flag = True
    while menu_flag:
        print("\n================ Bank Menu ================\n")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Change Password")
        print("6. Change Username")
        print("7. Get Last Transaction")
        print("8. Logout")
        bank_menu_choice = input("Please Enter your choice (1-8) ")
        if bank_menu_choice == "1":
            CheckBalance(username)
        elif bank_menu_choice == "2":
            Deposit(username)
        elif bank_menu_choice == "3":
            Withdraw(username)
        elif bank_menu_choice == "4":
            Transfer(username)
        elif bank_menu_choice == "5":
            ChangePassword(username)
        elif bank_menu_choice == "6":
            ChangeUsername() 
        elif bank_menu_choice == "7":
            GetLastTransaction(username)       
        elif bank_menu_choice == "8":
            menu_flag = False

        elif bank_menu_choice == "0":
            print("The operation is cancelled")
            menu_flag = False    
        else:
            print("Invalid Choice")


def CheckBalance(username):
    print(f"Your Balance : {registered_users[username]["Balance"]} EGP")


def Deposit(username):
    amount = int(input("Enter the amount you want to Deposit : "))
    if amount>0:
        registered_users[username]["LastTransaction"][0] = "Deposit"
        registered_users[username]["LastTransaction"][1] = amount
        registered_users[username]["LastTransaction"][2] = registered_users[username]["Balance"]
        registered_users[username]["Balance"]+=amount
        Receipt(username=username,operationType="Deposit",amount=amount,reciever="none")
    elif amount <0:
        print("Cannot Deposit a negative number")
    else :
        print("The operation is cancelled")


def Withdraw(username):
    amount = int(input("Enter the amount you want to Withdraw : "))
    if registered_users[username]["Balance"] >= amount and amount >0:
        registered_users[username]["LastTransaction"][0] = "Withdraw"
        registered_users[username]["LastTransaction"][1] = amount
        registered_users[username]["LastTransaction"][2] = registered_users[username]["Balance"]
        registered_users[username]["Balance"]-=amount
        Receipt(username=username,operationType="Withdraw",amount=amount,reciever="none")
    elif amount == 0:
        print("The operation is cancelled")    
    elif amount<0:
        print("Cannot Withdraw a negative number")
    else:
        print("Insufficicent Balance")


def Transfer(username):
        reciever = input("Enter the username you want to transfer money to : ")
        amount = int(input("Enter the amount you want to Transfer : "))
        if (registered_users[username]["Balance"] >= amount) and (reciever in registered_users.keys()) and (username!=reciever) and (amount >0) and (reciever != "0") :
            registered_users[username]["LastTransaction"][0] = "Transfer"
            registered_users[username]["LastTransaction"][1] = amount
            registered_users[username]["LastTransaction"][2] = registered_users[username]["Balance"]
            registered_users[username]["LastTransaction"][3] = reciever
            registered_users[username]["Balance"]-=amount
            registered_users[reciever]["Balance"]+=amount
            Receipt(username=username,operationType="Transfer",amount=amount,reciever=reciever)
        elif amount == 0 or reciever == "0":
            print("The operation is cancelled")    
        elif reciever not in registered_users.keys():
            print("Invalid Reciever username")
        elif username == reciever :
            print("Cannot transfer money to the same account")
        elif amount <0:
            print("Cannot Transfer a negative number")
        else:
            print("Insufficicent Balance")


def ChangePassword(username):
    password = input("Enter your old Password : ")
    if registered_users[username]["Password"] == password and password != "0":
        new_password = input("Enter your new Password : ")
        if len(new_password) >6:
            registered_users[username]["Password"] = new_password
            print("The Password Updated Successfully")
        else:
            print("The Password must be at least 6 characters long")
    elif password == "0":
        print("The operation is cancelled")        
    else:
        print("Wrong Password")   


def Receipt(operationType,amount,reciever,username):
    if operationType == "Deposit":
        print("==========================")
        print(f"You Deposited {amount}")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================")
    elif operationType == "Withdraw":
        print("==========================")
        print(f"You Withdrawed {amount}")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================")
    else:
        print("==========================")
        print(f"You Transfered {amount} to {reciever}")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================")    


def ChangeUsername():
    username = input("Enter your current username : ")
    password = input("Enter your password : ")
    if (username!= "0") and (password != "0") and (registered_users[username]["Password"] == password) and (username in registered_users.keys()):
        new_username = input("Enter your new username : ")
        if len(new_username) >0:
            registered_users[new_username] = registered_users[username]
            del registered_users[username]
            print("The Username Updated Successfully")
        else:
            print("The Username is Invalid")
    elif username == "0" or password == "0":
        print("The operation is cancelled")
    elif username not in registered_users.keys():
        print("Wrong Username")        
    else:
        print("Wrong Password")   


def GetLastTransaction(username):
    if registered_users[username]["LastTransaction"][0] == "Deposit":
        print("==========================")
        print(f"Your Last Successful Transaction")
        print(f"The transaction type was {registered_users[username]["LastTransaction"][0]}")
        print(f"You Deposited {registered_users[username]["LastTransaction"][1]}")
        print(f"Your balance was {registered_users[username]["LastTransaction"][2]} before this transaction")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================")
    elif registered_users[username]["LastTransaction"][0] == "Withdraw":
        print("==========================")
        print(f"Your Last Successful Transaction")
        print(f"The transaction type was {registered_users[username]["LastTransaction"][0]}")
        print(f"You Withdrawed {registered_users[username]["LastTransaction"][1]}")
        print(f"Your balance was {registered_users[username]["LastTransaction"][2]} before this transaction")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================")
    elif registered_users[username]["LastTransaction"][0] == "Transfer":
        print("==========================")
        print(f"Your Last Successful Transaction")
        print(f"The transaction type was {registered_users[username]["LastTransaction"][0]}")
        print(f"You Transfered {registered_users[username]["LastTransaction"][1]} to {registered_users[username]["LastTransaction"][3]}")
        print(f"Your balance was {registered_users[username]["LastTransaction"][2]} before this transaction")
        print(f"Your current balance is {registered_users[username]["Balance"]}")
        print("==========================") 

    else :
        print("==========================")
        print(f"You didn't do any recent Transactions")
        print("==========================") 

main_flag = True
login_counter = 0
while main_flag:
    print("\n================ Welcome to Python Bank ================\n")
    print("(note: You can cancel any operation by entering 0)\n")
    print("1. Register")
    print("2. Login")
    print("3. The number of our Registered Users")
    print("4. Exit")
    choice = input("Please Enter your choice (1-4) ")
    if choice == "1":
        Register()
    elif choice == "2":
        attempts = Login()
        if attempts == 1:
            login_counter+=attempts
        else:
            login_counter = attempts
    elif choice == "3":
        print(f"The number of our Registered users is {len(registered_users.keys())}")    
    elif choice == "4":
         main_flag = False
    elif choice == "0":
        print("The operation is cancelled")
        main_flag = False     
    else :
        print("Invalid Choice")
    if login_counter >=3 :
        print("Too many unsuccessful login attempts the program will close :(")
        main_flag = False                

































      

      


