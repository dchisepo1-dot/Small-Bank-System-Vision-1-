close=0
import os
import time
path=os.getcwd()
path=path.replace("\\","/") + "/"
#path="C:/Users/HP/Desktop/programs/"
# MAIN CLASS
class BankAccount:

    # Constructor
    def __init__(self, name, balance, password, account_number, account_type, status, identity, registration):
        self.name = name
        self.balance = balance
        self.password = password
        self.account_number = account_number
        self.account_type = account_type
        self.status=status
        self.identity=identity
        self.registration=registration

    # Display account details
    def display_account(self):
        print("\nYOUR ACCOUNT DETAILS")
        print("Name:", self.name)
        print("Balance:", self.balance)
        print("Account Number:", self.account_number)
        print("Registration number :", self.registration)
        print("Account type : ", self.account_type)

    # Deposit money
    def deposit_money(self, amount):
        self.balance = self.balance + amount
        balance=self.balance
        ID=self.identity
        return ID, balance
    # Withdraw money
    def withdraw(self, amount):
        charge=amount * (6/100)
        new_amount=charge+amount
        
        self.balance = self.balance - new_amount
        account.save_account()
        self.status1=True
    # Save account into file
    def save_account(self):
        file = open(path + self.account_number + ".txt", "w")
        data = (
            self.name + "," +
            str(self.balance) + "," +
            self.password + "," +
            self.account_number + "," +
            self.account_type + "," +
            self.status+ ","+
            self.identity + "," +
            self.registration
        )
        file.write(data)
        file.close()
    # wrong pin counting
    def pass_count(self):
        self.status=int (self.status)+1
        if self.status>=3:
            file=open(path + "time.txt", "r")
            data=file.read()
            file.close()
            index=int(account_number[-1])-1
            current_time=time.time()
            data=data.split(",")
            data[index]=str(current_time)
            data=",".join(data)
            file=open(path + "time.txt", "w")
            file.write(data)
            file.close()
        self.status=str(self.status)
        self.save_account()
        
    # Delete account
    def delete_account(self):
        if os.path.exists(path + self.account_number + ".txt"):
            os.remove(path + self.account_number + ".txt")
            print("Account deleted successfully")
        else:
            print("Account not found")

class Student_account(BankAccount):
    def __init__(self, name, balance, password, account_number, account_type, status, identity, registration):
        super().__init__(name, balance, password, account_number, account_type, status, identity, registration)
        self.account_type="Student account"
    def withdraw_money(amount):
        if int(amount)>10000:
               print("You can not withdraw more than $10000 at once")
        else:
            index=int(self.account_number[-1])-1
            file=open(path + "student_withdraw.txt", "r")
            data=file.read()
            data=data.split(",")
            info=float(data[index])
            file.close()
            limit=86400
            current_time=time.time()
            day=info + limit          
            if info<10:
                
                file=open(path + "student_withdraw.txt", "w")
                currenttime=str(time.time())
                info[index]=currenttime
                data=",".join(info)
                data=file.write()
                file.close()
                withdraw_money(amount)
            
            elif current_time>=day:
                BankAccount.withdraw(self,amount)
            else:
                print("You can not have more than 3 withdrawals per day")
class Business_account(BankAccount):
    def _init_(self, name, balance, password, account_number, account_type, status, identity, registration):
        super()._init_(name, balance, password, account_number, account_type, status, identity, registration)
        self.account_type="Business account"
    def withdraw_money(amount):
        value=True
        if int(amount)>50000:
            print("You can not withdraw more than 50000")
            value=False
        elif self.balance< -20000:
            print("Your account balance is now too low, you can not withdraw any money")
            value=False
        else:
            BankAccount.withdraw(self,amount)
        return value

class Savings_account(BankAccount):
    def _init_(self, name, balance, password, account_number, account_type, status, identity, registration):
        super()._init_(name, balance, password, account_number, account_type, status, identity, registration)
        account_type="Savings account"
    def withdraw_money(self,amount):
        if self.balance<amount + 10000:
            print("Your account should have at least $10000 remaining")
        elif self.balance<10000:
            print("Your account balance is too low, at least 10000 is required")
        else:
            BankAccount.withdraw(self,amount)
                    
# FUNCTION TO LOAD EXISTING ACCOUNT
def load_account(account_number):
    if not os.path.exists(path + account_number + ".txt"):
        print("Account not found")
        return None

    file = open(path + account_number + ".txt", "r")
    data = file.read()
    file.close()
    name, balance, password, account_number, account_type, status, identity, registration = data.split(",")
    if account_type=="Student account":
        return Student_account(
            name,
            float(balance),
            password,
            account_number,
            account_type,
            status,
            identity,
            registration
        )
    elif account_type=="Business account":       
        return Business_account(
            name,
            float(balance),
            password,
            account_number,
            account_type,
            status,
            identity,
            registration
        )
    elif account_type=="Savings account":
        return Savings_account(
            name,
            float(balance),
            password,
            account_number,
            account_type,
            status,
            identity,
            registration
        )
    else:
        print("Account requested is not found, or an error occured", account_type)


# FUNCTION TO CREATE NEW ACCOUNT

def create_account(count):
    count=count+1
    if count!=4:
            char=','
            space=' '
            numbers=["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
            name = str(input("Enter your full name (Full name should contain proper spacing: "))
            password = input("Create your Password (Password should contain at least 5 numbers and 5 other characters) (: ")
            identity=input("Enter your ID number (ID number should appear as on your ID card")
            
            print()
            print("1: Saving account")
            print("2:Student account ")
            print("3: Business account")
            try:
                option=int(input("Select account type: "))
            except ValueError:
                print("You chose an invalid option")
                create_account(count)
            except Exception:
                print("An unknown error occurred")
                
            else:
                if option==1:
                    account_type="Savings account"
                elif option==2:
                    account_type="Student account"
                elif option==3:
                    account_type="Business account"
                else:
                    print("Your choice is unknown, try again")
                    create_account(count)
                
            status="0"
            valid_name= validate_name(name)
            valid_pass= validate_pass(password)
            if valid_name==0:
                create_account(count)
            elif valid_pass==0:
                create_account(count)
            elif len(identity)<10:
                print("Your id number is too short, try again")
                create_account(count)
            elif not identity[9].isalpha():
                print("A letter character is expected before last two digits")
                create_account(count)      
            else:
                password=pin_hashing(password)
                i = 1
                while i < 10:
                    account_number = "account" + str(i)
                    if not os.path.exists(path + account_number + ".txt"):
                        j=int(i)
                        gen=((j + j + 3)*4426)
                        gen1=str(gen)
                        gen2=gen1[2:4]
                        gen3=j%2
                        gen4=str(gen3)
                        gen5=gen4[-1]
                        registration=str('IND'+ gen2  + gen5 + account_number[5:6] + name[1:3] + 'bn' + identity[1:3])

                        account = BankAccount(
                            name,
                            0,
                            password,
                            account_number,
                            account_type,
                            status,
                            identity,
                            registration   
                        )
                        if not os.path.exists(path + "transactions.txt"):
                            j=0
                            data='0,'
                            while j<10:
                                data=(data + '0,')
                                j=j+1
                            
                            file=open(path + "transactions.txt", "w")
                            file.write(data)
                            file.close()

                            file=open(path + "deposits.txt", "w")
                            file.write(data)
                            file.close()

                            file=open("highestTransaction.txt", "w")
                            file.write('0,0,0')
                            file.close()                            

                            file=open(path + "admin.txt", "w")
                            data1="indi bank,9213439899213439909213439919213439929213439939213439946273,0,142162992532329949791997134323399462361000i1343233997n1421621000d6273,indianbank345"
                            file.write(data1)
                            file.close()

                            file=open(path + "names.txt", "w")
                            info=data.split(",")
                            info[0]=identity
                            data1=",".join(info)
                            file.write(data)
                            file.close()

                            

                            file=open(path + "totalaccounts.txt", "w")
                            file.write("1")
                            file.close()

                            
                            file=open(path + "transferID.txt", "w")
                            info='1000'
                            file.write(info)
                            file.close()

                            file=open(path + "totalwithdrawals.txt", "w")
                            info='0'
                            file.write(info)
                            file.close()

                            file=open(path + "totaldeposits.txt", "w")
                            info='0'
                            file.write(info)
                            file.close()

                            file=open(path + "totaltransactions.txt", "w")
                            info='0'
                            file.write(info)
                            file.close()

                            file=open(path + "activeaccount.txt", "w")
                            file.write(data)
                            file.close()

                            file=open(path + "time.txt", "w")
                            file.write(data)
                            file.close()

                            file=open(path + "student_withdraw.txt", "w")
                            file.write(data)
                            file.close()
                            
                            account.save_account()
                            save_names(identity, account_number)
                            print("\nAccount created successfully")
                            print()
                            print("Thank you for Creating an INDI Bank account")
                            account.display_account()
                            break
                        else:
                            found=existing_accounts(identity)
                            if found==1:
                                print("You have an existing account, visit nearest bank for activation")
                                opt=print("Enter 1 to try again and 0 to cancel")
                                if opt==1:
                                    create_account(count)
                                else:
                                    break
                                break
                            else:
                                
                                account.save_account()
                                save_names(identity, account_number)
                                print("\nAccount created successfully")
                                account.display_account()
                                addaccounts()
                                break
                    i = i + 1
                else:
                    print("Maximum account limit reached")
                
    else:
        print("Too many invalid input, the system will close")
        close=1
        return close
def validate_pass(password):
    numbers=["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
    length=len(password)
    check=0
    check1=0
    valid=0
    i=1
    pass_number=""
    while i<length:
        j=0
        while j<10:
            if password[i].isalpha():
                check=check+1
            else:
                pass
            j=j+1
        i=i+1
    j=0
    digits=""
    while j<length:
        i=0
        while i<10:
            if password[j]==numbers[i]:
                check1=check1 + 1
            else:
                pass
            i=i+1
        j=j+1
    if len(password)<8:
        print("Your Password is too short")
    elif len(password)>15:
        print("Your password is too long, try a shorter one")
    elif check1<5:
        print("Your password is weak, it should have at least 5 numbers")
    elif check<3:
        print("Password too weak, it should have a combination of at least 3 alphabet letters")      
    else:
        valid=1
    return valid
def validate_name(name):
    i=0
    valid=0
    space=" "
    length=int(len(name))
    for i in range(0,length):
        if name[i].isalpha or " ":
            pass
        else:
            print("Only Alphabet letters are allowed in name")
            return valid
            break
    numbers=["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]     
    if len(name)<6:
        print("Your name is too short")
    elif space not in name:
        print("Full name is required and with proper spacing")
    elif any(num in numbers for num in name):
        print("Numbers are not allowed in name")
    elif len(name)>25:
        print("Name is too long , try again ")
    else:
        valid=1
    return valid
#save transfers function
def save_transfers(sender_name, receiver_name, sender_number, amount, choice):
    file=open(path + "transactions.txt", "r")
    person=int(sender_number[-1])
    person=person-1
    data=file.read()
    file.close()
    ID=transactionID()
    transaction=sender_name + ' successfully sent $' + str(amount) + ' to ' + receiver_name + ' with transaction ID ' + ID + ' using INDI Bank'
    collect=data.split(",")
    collect[person]=transaction
    save_collect=",".join(collect)
    file=open(path + "transactions.txt", "w")
    file.write(save_collect)
    file.close()
    print(collect[person])

# saved transfers    
def saved_transfers(sender_name, sender_number):
    file=open(path + "transactions.txt", "r")
    data=file.read()
    file.close()
    person=int(sender_number[-1])
    person=person-1
    info=data.split(",")
    collect=info[person]
    if collect=='0':
        print("No transfer history yet")
    else:
        print(collect)
def transactionID():  
    file=open(path + "transferID.txt", "r")
    data=file.read()
    data1=int(data)
    data2=data1 + 1   
    ID="TRS" + str(data2)
    file.close()
    file=open(path + "transferID.txt", "w")
    data=str(data2)
    file.write(data)
    file.close()
    return ID
# Validate amount 
def validate_input(amount):
    amount = str(amount)
    length=len(amount)
    numbers=["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]
    if length==0:
        valid=0
    for i in range(0,length):
        for j in range(0,10):
            if amount[i]!=numbers[j]:
                valid=0
            else:
                valid=1
                break
        if valid==0:
            break
        else:
            pass
    return valid
#save names
def save_names(identity, account_number):
    file=open(path + "names.txt", "r")
    person=int(account_number[-1])
    person=person-1
    data=file.read()
    file.close()
    collect=data.split(",")
    collect[person]=identity
    save_collect=",".join(collect)
    file=open(path + "names.txt", "w")
    file.write(save_collect)
    file.close()
# existing accounts
def existing_accounts(identity):
    with open(path + "names.txt", "r") as file:
        data = file.read()
    info = data.split(",")

    found = 0
    i = 0
    while i < len(info):
        collect = info[i].strip()  # remove spaces/newlines
        if collect == identity:
            found = 1
            return found
        i = i + 1

    return found
def transfer_number():
    file=open("transferID.txt", "r")
    data=int(file.read)
    total=data-1000
    print("Total number of all transactions is ", total)

def system_pass(password):
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",") 
    pas=(info[1])
    
    if password==pas:
        return True
        
    else:
        return False
def check_status():
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",") 
    pas=int(info[2])
    if pas >=3:
        return False
    else:
        return True
def change_pass(new_password):
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",") 
    file=open(path + "admin.txt", "w")
    info[1]=new_password
    info1=",".join(info)
    file.write(info1)
    file.close()
    print("Password was changed")
def pass_count(count):
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",") 
    file=open(path + "admin.txt", "w")
    count1=int(info[2]) + count
    info[2]=str(count1)
    info1=",".join(info)
    file.write(info1)
    file.close()
def active_account(account_number):
    account=int(account_number[-1])
    file=open(path + "activeaccount.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",")
    collect=int(info[account-1])
    file=open(path + "activeaccount.txt", "w")
    data1=int(collect)+1
    info[account-1]=str(data1)
    info1=",".join(info)
    file.write(info1)
    file.close()
def most_active():
    file=open(path + "totalaccounts.txt","r")
    maxi=file.read()
    max1=int(maxi) 
    file.close()
    file=open(path + "activeaccount.txt", "r")
    data=file.read()
    data1=data.split(",")
    file.close()
    largest=0
    i=0
    j=0
    k=0
    while i<=max1:
        data2=int(data1[i])
        if data2>largest:
            largest=data2
            k=j+1
        else:
            largest=largest
        i=i+1
    file=open(path + "account" + str(k) + ".txt", "r")
    data=file.read()
    file.close()
    data1=data.split(",")
    name=data1[0]
    account_number=data1[3]
     
    print(f"Transaction with most active is {name} with account number {account_number} and {largest} transactions")

def banned_accounts(): 
    file=open(path + "totalaccounts.txt", "r")
    data=file.read()
    file.close()
    total=int(data)
    if total==0:
        return print("No accounts yet")
    else:
        i=1
        count=0
        while i<=total:
            j=str(i)
            if os.path.exists(path + "account" + j + ".txt"):
                file=open(path + "account" + j + ".txt", "r")
                data=file.read()
                file.close()
                info=data.split(",")
                status=info[5]
                name=info[0]
                status=int(status)
                account_number=info[3]
                if status>=3:
                    count=count+1
                    print(f"{name} was suspended with account number {account_number}")
                else:
                    pass
            i=i+1
        if count==0:
            return print("No suspended accounts found")
        else:        
            return print(f"We have {count} suspended accounts")
        
def addaccounts():
    file=open(path + "totalaccounts.txt", "r")
    data=file.read()
    file.close()
    info=int(data)+1
    file=open(path + "totalaccounts.txt", "w")
    file.write(str(info))
    file.close()
def after_delete():
    file=open(path + "totalaccounts.txt", "r")
    data=file.read()
    file.close()
    info=int(data)-1
    file=open(path + "totalaccounts.txt", "w")
    file.write(str(info))
    file.close()
def highest_transaction():
    file=open(path + "highestTransaction.txt", "r")
    data=file.read()
    file.close()
    account_number, amount, status=data.split(",")
    print(f"The highest transaction is account number {account_number} with amount ${amount}")
def record_highest_transaction(account_number, amount):
    file=open(path + "highestTransaction.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",")
    amount1=int(info[1])
    amount=int(amount)
    
    if amount>amount1:
        file=open(path + "highestTransaction.txt", "w")
        info[1]=str(amount)
        info[0]=account_number
        
        info1=",".join(info)
        print("info is : ", info1)
        file.write(info1)
        file.close()
def total_withdrawals():
    file=open(path + "totalwithdrawals.txt", "r")
    data=file.read()
    file.close()
    info=int(data)
    record=info+1
    file=open(path + "totalwithdrawals.txt", "w")
    file.write(str(record))
    file.close()
def  deposits_withdrawals():
    file=open(path + "totaldeposits.txt", "r")
    data=file.read()
    file.close()
    file=open(path + "totalwithdrawals.txt", "r")
    data1=file.read()
    file.close()
    return print(f"Total number of deposits are {data} and total withdrawals are {data1}")
def total_deposits():
    file=open(path + "totaldeposits.txt", "r")
    data=file.read()
    file.close()
    info=int(data)
    record=info+1
    file=open(path + "totaldeposits.txt", "w")
    file.write(str(record))
    file.close()
def total_transactions():
    file=open(path + "totaltransactions.txt", "r")
    data=file.read()
    file.close()
    info=int(data)
    record=info+1
    file=open(path + "totaltransactions.txt", "w")
    file.write(str(record))
    file.close()
def check_total_transactions():
    file=open(path + "totaltransactions.txt", "r")
    data=file.read()
    file.close()
    return print(f"We have {data} total transactions yet") 
def least_most():
    file=open(path + "totalaccounts.txt", "r")
    data=file.read()
    file.close()
    total=int(data)
    if total==0:
        return print("No accounts yet")
    else:
        i=1
        while i<=total:
            j=str(i)
            if os.path.exists(path + "account" + j + ".txt"):                
                file=open(path + "account" + j + ".txt", "r")
                data=file.read()
                file.close()
                info=data.split(",")
                balance=info[1]
                balance=float(balance)
                smallest=balance
                largest=balance
                break
            else:
                i=i+1
        i=2
        while i<=total:
            j=str(i)
            file=open(path + "account" + j + ".txt", "r")
            data=file.read()
            file.close()
            info=data.split(",")
            balance=info[1]
            name=info[0]
            balance=float(balance)
            account=1
            if balance>=largest:
                account1=i
                largest=balance               
            elif balance<=smallest:
                account2=i
                smallest=balance
            i=i+1
        print(f"Account with the largest amount is {name} with account{account1} and balance ${largest}")
        print(f"Account with the smallest amount is account{account2} with ${smallest}")
        
def pin_hashing(password):
    harsh ={0:'921343', 1:'343852', 2:'1343233', 3:'142162', 4:'53232', 5:'893794',6:'9791', 7:'6236', 8:'7934683', 9:'190112'}
    numbers=['0','1','2','3','4','5','6','7','8','9']
    password=str(password)
    converted=""
    pass_number=""
    pass_char=""
    length=len(password)
    j=0
    while j<length:
        if password[j] in numbers:
            pass_number=pass_number + password[j]
        else:
            pass_char=pass_char + password[j]
        j=j+1
    if pass_number!="":       
        pass_number=int(pass_number) + 9898
    password=str(pass_number) + pass_char
    length=len(password)
    for i in range(0,length):
        for j in range(0,10):
            if password[i]==numbers[j]:
                number=int(password[i])
                new_harsh=(harsh[number])
                add = i + j + 9
                converted=converted + new_harsh + str(add)
                break
            else:
                if password[i] not in numbers:
                    converted=converted + password[i]
                    break
                
    converted=converted+"6273"
    return converted
def back_up_pin(back_up, company_id):
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",")
    if info[3]==back_up:
        return True
    elif info[4]==company_id:
        return True
    else:
        return False
        print("value of hashed pin is ", info[4])
        print("value of company id is", info[5])
def recover_admin(hashed):
    file=open(path + "admin.txt", "r")
    data=file.read()
    file.close()
    info=data.split(",")
    info[3]==hashed
    info[2]='0'
    file=open(path + "admin.txt", "w")
    info1=",".join(info)
    file.write(info1)
    file.close()
def about_bank():
    new_path=path + "aboutbank.txt"
    if os.path.exists(new_path):  
        file=open(path + "aboutbank.txt", "r")
        data=file.read()
        file.close()
        print(data)
    else:
        print("About section is not found, try to reach out through website")
def user_guide():
    new_path=path + "user_guide.txt"
    if os.path.exists(new_path): 
        file=open(path + "user_guide.txt", "r")
        data=file.read()
        file.close()
        print(data)
    else:
        print("Information not found, try again later")
def terms_conditions():
    new_path=path + "termsandconditions.txt"
    if os.path.exists(new_path): 
        file=open(path + "termsandconditions.txt", "r")
        data=file.read()
        file.close()
        print(data)
    else:
        print("System could not find the information requested")
def attempts(account_number):
    file=open(path + account_number + ".txt" , "r")
    data=file.read()
    file.close()
    data=data.split(",")
    attempt=2-int(data[5])
    if attempt==0:
        print("You have entered wrong Password 3 times, your account will be suspended for 2 days")
    return print(f"NOTE: You have {attempt} more attempts left ")
def correct_pass(account_number):
    
    file=open(path + account_number + ".txt" , "r")
    data=file.read()
    file.close()
    data=data.split(",")
    (data[5])="0"
    file=open(path + account_number + ".txt" , "w")
    info=",".join(data)
    file.write(info)
    file.close()
    
    
# MAIN PROGRAM LOOP
count=0
while count<4 and close!=1:
    print()
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. User Login ")
    print("3. Suspended Account?")
    print("4. About INDI Bank?")
    print("5. System Admin login")
    print("6. Recover Admin System Account")
    print("7. User guide info")
    print("8. Terms and conditions")
    print("9. Exit ")
    choice = int(input("Enter your choice: "))

    # CREATE ACCOUNT
    if choice == 1:
        count=0
        create_account(count)

    # VIEW ACCOUNT
    elif choice == 2:
        account_number = input("Enter account number: ")
        password=input("Enter your password")
        password=pin_hashing(password)
        account = load_account(account_number)

        if account:
            
                
            if account.status=='3':
                file=open(path + "time.txt", "r")
                data=file.read()
                file.close()
                data=data.split(",")
                index=int(account_number[-1])-1
                stored_time=float(data[index])
                date=stored_time + 172800.000
                current_time=time.time()
                if current_time < date:
                    print("Your account was suspended, will be activated after 2 days or visit any nearest INDI BANK")
                else:
                    print("You can now activate your account online")
            else:
                    if password==account.password:
                        print("......... WELCOME TO INDI BANKING SYSTEM.........")
                        correct_pass(account_number)
                        count=0
                        while count<4:
                            print()
                            print("1. Deposit Money")
                            print("2. Withdraw Money")
                            print("3. Delete Account")
                            print("4. Balance request")
                            print("5. Send money")
                            print("6. Account services")
                            print("7. Exit")
                            choice=input("Select choice")
                            # DEPOSIT MONEY
                            if choice == '1':
                                            
                                amount =(input("Enter amount to deposit: "))
                                valid=validate_input(amount)
                                if valid==1:
                                    if int(amount)>50000:
                                        print("You can not deposit more than 50000 at once")
                                    else:
                                        amount=float(amount)
                                        account.deposit_money(amount)
                                        newBalance=account.balance
                                        account.save_account()
                                        active_account(account_number)
                                        ID=transactionID()
                                        record_highest_transaction(account_number, int(amount))
                                        total_deposits()
                                        total_transactions()
                                        print(f"You have successfully deposited {amount} with transaction ID {ID} new balance is ${newBalance}")
                                elif valid==0:
                                    print("ERROR: Amount should contain whole numbers only")
                                else:
                                    print("Unknown error occurred, try again ") 

                            # WITHDRAW MONEY
                            elif choice == '2':
                                amount = (input("Enter amount to withdraw: "))
                                valid=validate_input(amount)
                                if valid==1:
                                    if int(amount)>50000:
                                        print("You can not withdraw more than 50000")
                                    else:
                                        amount=float(amount)
                                        value=account.withdraw_money(amount)
                                        if account.status is False:
                                            print("Withdrawal failed")
                                        elif value==False:
                                            continue
                                        else:
                                            newBalance=account.balance
                                            account.save_account()
                                            active_account(account_number)
                                            #save_withdraw(amount)
                                            ID=transactionID()
                                            record_highest_transaction(account_number, int(amount))
                                            total_withdrawals()
                                            total_transactions()
                                            
                                            print(f"You have successfully withdrawed {amount} with transaction ID {ID} new balance is ${newBalance}")
                                            
                                elif valid==0:
                                    print("ERROR: Amount should contain whole numbers only")
                                else:
                                    print("Unknown error occurred, try again ")
                                    
                            

                            # DELETE ACCOUNT
                            elif choice == '3':

                                if account.balance!=0:
                                    print("Withdraw all the money in your account first") 
                                else:
                                    account.delete_account()
                                    identity="0"
                                    save_names(identity, account_number)
                                    after_delete()
                            # balance request
                            elif choice=='4':
                                print("Your current balance is : $", account.balance)
                            # SEND MONEY
                            elif choice =='5':
                                amount=(input("Enter amount"))
                                valid=validate_input(amount)
                                if valid==1:
                                    amount=int(amount)
                                    if int(amount)>50000:
                                        print("You can not withdraw more than 50000")
                                    else:
                                        if amount<=0:
                                            print("0 amount is not allowed")
                                        elif account.balance==0 or account.balance<(amount):
                                             print("Insufficient balance")
                                                
                                        else:
        
                                            sender_name=account.name
                                            sender_number=account.account_number   
                                            account.withdraw_money(amount)
                                            record_highest_transaction(sender_number, int(amount))
                                            receiver_number=input("Enter receiver account number: ")
                                            account=load_account(receiver_number)
                                            receiver_name=account.name
                                            if sender_number==receiver_number:
                                                print("You can not transfer money to same account")
                                            else:
                                                if account:
                                                    account.deposit_money(amount)
                                                    account.save_account()
                                                    save_transfers(sender_name, receiver_name,sender_number, amount, choice)
                                                    active_account(sender_number)
                                                    total_transactions()
                                                else:
                                                    print("Receiver account is not registered")                          
                                elif valid==0:
                                    print("ERROR: Amount should contain whole numbers only")
                                else:
                                    print("Unknown error occurred, try again ")
                                
                            # ACCOUNT SERVICES
                            elif choice=='6':
                                print()
                                print("1. Change password?")
                                print("2. Change user name?")
                                print("3. Suspended account recovery")
                                print("4. Transfer history")
                                option=input("Select option")
                                # CHANGE PASSWORD
                                valid=validate_input(option)
                                if valid==1:                               
                                    if option=='1':
                                        pin=input("Enter your current password first")
                                        if pin==account.password:
                                            newPin=input("Enter new pin")
                                            account.password=newPin
                                            account.save_account()
                                            print("Your password was changed")
                                        else:
                                            print("Password does not match")
                                            account.pass_count()
                                    # CHANGE USER NAME        
                                    elif option=='2':
                                        
                                        newName=input("Enter new name: ")
                                        account.name=newName
                                        account.save_account()
                                        print("Your Name was changed")
                                    # TANSACTION HISTORY
                                    elif option=='3':
                                        identity=input("Enter your ID card number: ")
                                        regNumber=input("Enter registration number: ")
                                        if identity==account.id and regNumber==account.regration:
                                            hashed=pin_hashing(0000)
                                            account.password=hashed
                                            account.save_account()
                                            print("Your account was activated ")
                                            print("Your PIN is 0000, make sure to change it")
                                        else:
                                            print("ID or Registration number is incorrect")
                                    elif option=='4':
                                        sender_name=account.name
                                        sender_number=account.account_number
                                        print("Password correct")
                                        saved_transfers(sender_name, sender_number)
                                                    
                                    else:
                                        print("Service is not yet available")
                                else:
                                    print("Unknown or invalid choice")
                            elif choice=='7':
                                print("Services will be closed")
                                break
                            else:
                                print("Unknown choice")
        
                    else:
                        print("Password is incorrect, try again")
                        attempts(account_number)
                        account.pass_count()
                        
        else:
            print("Account not found")
    # SUSPENDED ACCOUNT
    elif choice==3:
        account_number=input("Enter your account number: ")
        account=load_account(account_number)
        if account:
            if account.status=='3':
                file=open(path + "time.txt", "r")
                data=file.read()
                file.close()
                data=data.split(",")
                index=int(account_number[-1])-1
                stored_time=float(data[index])
                date=stored_time + 172800.000
                current_time=time.time()
                if current_time < date:
                    print("Please wait for 2 days or visit any nearest INDI BANK for activation")
                else:            
                    identity=input("Enter your ID card number: ")
                    regNumber=input("Enter registration number: ")
                    if identity==account.identity and regNumber==account.registration:
                        account.password='0000'
                        account.save_account()
                        print("Your account was activated ")
                        print("Your PIN is 0000, make sure to change it")
                    else:
                        print("ID or Registration number is incorrect")
            else:
                print("Your account is not suspended")
        else:
            print("Account not found, try again")
        
    # ABOUT BANK
    elif choice==4:
        about_bank()
    elif choice==5:
        status=check_status()
        if not status:
            print("This admin was suspended")
        else:
            count=0
            pass_count(count)
            pin=input("Enter System PIN ")
            hashed=pin_hashing(pin)
            check=system_pass(hashed)
            if not check:
                count=1
                pass_count(count)
                print("Password wrong, try again")
            else:
                
                while True:
                    print()
                    print("........WELCOME TO INDI BANK SYSTEM......")
                    print("1. Change password")
                    print("2. Most active Bank account")
                    print("3. Highest transaction")
                    print("4. Least and most balance Bank account")
                    print("5. Number of withdrawals and deposits")
                    print("6. Total number of transactions")
                    print("7. Banned accounts")
                    print("8. Back ")
                    choice1=(input("Select your option? "))
                    valid=validate_input(choice1)
                    if valid==0:
                        print("Invalid or unknown choice ")
                    elif valid==1:
                        if choice1=='1':
                            old_pin=input("Enter System old PIN to confirm ")
                            hashed=pin_hashing(old_pin)
                            check=system_pass(hashed)
                            if check:
                                new_pin=input("Enter 6 digits new PIN")
                                valid=validate_input(new_pin)
                                if valid==0:
                                    print("PIN should contain numbers only retry later")
                                else:
                                    pin=str(pin)
                                    if len(new_pin)!=6:
                                        print("Enter only 6 digits pin")
                                    else:
                                        final_pin=pin_hashing(new_pin)
                                        change_pass(final_pin)
                            else:
                                count=1
                                pass_count(count)
                                print("Password is wrong, try again")
                        elif choice1=='2':
                            most_active()
                        elif choice1=='3':
                            highest=highest_transaction()
                        elif choice1=='4':
                            least_most()
                        elif choice1=='5':
                            deposits_withdrawals()
                        elif choice1=='6':
                            check_total_transactions()
                        elif choice1=='7':
                            banned_accounts()
                            
                        elif choice1=='8':
                            break
                        else:
                            print("Unknown option ")
                            break
                    else:
                        print("An unknown error occured")
                            
                            
    elif choice==6:
        file=open(path + "admin.txt", "r")
        data=file.read()
        file.close()
        data1=data.split(",")
        status=int(data1[2])
        if status<3:
             print("This admin is not suspended")
        else:
            back_up=input("Enter back_up PIN to recover")
            back_up=pin_hashing(back_up)
            company_id=input("Enter company id")
            check=back_up_pin(back_up, company_id)
            if check:
                hashed=pin_hashing(00000)
                recover_admin(hashed)
                print("System Admin is activated")
                print("Pin is 00000 by default")
            else:
                print("Your details does not match")

    elif choice==7:
        user_guide()
    elif choice==8:
        terms_conditions()
    # EXIT
    elif choice == 9:
        break
    else:
        count=count+1
        if count==3:
            print("You have choosen an invalid choice 3 times, the program will end ")
            break
        print("Invalid choice")
print()
print("        ........THE SYSTEM TERMINATED.......    ")

# back_up pin 34627i2n3d
# company id = indianbank345
# adminpass 000000


                            

                        
