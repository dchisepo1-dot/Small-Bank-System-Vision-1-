🏦 INDI Bank — Vision 1

A Python-based banking management system built as a personal learning and software-development project.

INDI Bank Vision 1 is a command-line banking system developed in Python. The project simulates the core operations of a banking system, including account creation, authentication, deposits, withdrawals, money transfers, account management, transaction tracking, account suspension, and system administration.

This project is part of my journey of learning Python, Object-Oriented Programming, file handling, authentication concepts, data management, and software development through practical projects.

📌 Project Information

Project Name	INDI Bank
Version:	Vision 1
Language:	Python
Application Type:	Command-Line / Console Application
Storage:	Local text files
Architecture:	Object-Oriented + Functional
Developer:	Divine Chisepo
Project Status:	Development / Learning Project

📖 About the Project

INDI Bank is a simulated banking management system written in Python.
The project started as a simple banking program and has developed into a more advanced system containing different account types, authentication, transaction management, account security mechanisms, administrative functions, and persistent data storage.

The system uses Python classes to represent bank accounts and inheritance to create specialized account types.

The main account class is:

class BankAccount:

with specialized account classes:

BankAccount
│
├── Student_account
├── Business_account
└── Savings_account

The main BankAccount class stores information such as the account holder's name, balance, password, account number, account type, account status, identity information, and registration number.

🎯 Purpose of the Project

The main purpose of this project is learning through building.

Instead of learning Python concepts separately, I wanted to combine them into a practical application that resembles a real-world banking system.

Through this project I am practicing:

Python programming
Object-Oriented Programming
Classes and objects
Inheritance
Methods
Functions
File handling
Data validation
Authentication
Error handling
Transaction management
Application logic
Git and GitHub
Software project organization
Creativity

The project is continuously evolving as I learn new programming concepts.

✨ Main Features
👤 1. Account Creation

Users can create a new bank account through the main menu.

The system asks for:

Full name
Password
Identity number
Account type

The available account types are:

1. Savings account
2. Student account
3. Business account

The system also generates an account number and registration number for the account.

Account creation and account-type selection are implemented in the create_account() function.

🔐 2. Password Authentication

Users must provide their account number and password when logging in.

The entered password is processed before being compared with the stored account password.

The project also contains password validation rules.

For example, the password validation checks:

Minimum length
Maximum length
Number of digits
Alphabetic characters

The current validation requires a password between 8 and 15 characters, with at least 5 numbers and at least 3 alphabetic characters.

🏦 3. Multiple Account Types

One of the main improvements in Vision 1 is the use of different account classes.

Student Account
class Student_account(BankAccount):

The student account is designed with additional withdrawal restrictions.

The current implementation includes a withdrawal limit and a daily withdrawal-count concept.

Business Account
class Business_account(BankAccount):

The business account contains different withdrawal rules, including a maximum withdrawal amount and a balance-related restriction.

Savings Account
class Savings_account(BankAccount):

The savings account contains rules intended to maintain a minimum balance after withdrawals.

💰 4. Deposit Money

Logged-in users can deposit money into their account.

The system:

Receives the amount.
Validates the input.
Checks the transaction limit.
Updates the account balance.
Saves the account.
Generates a transaction ID.
Records transaction statistics.

The current program limits a single deposit to 50,000.

💸 5. Withdraw Money

Users can withdraw money from their account.

The basic withdrawal function also applies a 6% charge to the withdrawal amount:

charge = amount * (6/100)
new_amount = charge + amount

The account balance is then reduced by the total amount.

The different account classes can apply their own withdrawal rules before calling the main withdrawal functionality.

🔄 6. Send Money / Transfers

Users can send money to another registered account.

The transfer process includes:

Sender
   │
   ▼
Enter Amount
   │
   ▼
Check Balance
   │
   ▼
Enter Receiver Account
   │
   ▼
Verify Receiver
   │
   ▼
Withdraw From Sender
   │
   ▼
Deposit Into Receiver
   │
   ▼
Generate Transaction ID

The project prevents a user from intentionally transferring money to the same account.

Transfers are also recorded with a transaction ID.

🧾 7. Transaction IDs

Transactions receive unique IDs generated by the transactionID() function.

The current format is:

TRS1001
TRS1002
TRS1003
...

The system stores the latest transaction number in:
transferID.txt

and increments it whenever a new transaction ID is generated.

📜 8. Transfer History

Users can access their transfer history through:

Account Services
        ↓
Transfer History

The project stores transfer information in:

transactions.txt

and retrieves the stored transaction information when requested.

🔒 9. Account Suspension

The system includes a failed-password attempt mechanism.

When incorrect passwords are entered repeatedly, the account status is increased.

After three failed attempts, the account is treated as suspended.

The system records a time associated with the suspension and uses a 2-day suspension period in the current implementation.
Users can also check whether an account is suspended from the main menu.

🔓 10. Suspended Account Recovery

A suspended account can be checked for recovery.

The system requests:

Identity card number
Registration number

If the information matches the account information, the account can be activated and the password is temporarily set to:

0000

The user is instructed to change the password afterward.

👨‍💼 11. System Administrator

Vision 2 includes a separate system administrator section.

The main menu contains:

5. System Admin login
6. Recover Admin System Account

The administrator can access system-level information after authentication.

The administrator menu contains:

1. Change password
2. Most active Bank account
3. Highest transaction
4. Least and most balance Bank account
5. Number of withdrawals and deposits
6. Total number of transactions
7. Banned accounts
8. Back

These options provide basic administrative statistics and account monitoring.

📊 12. Banking Statistics

The system keeps track of several statistics.

These include:

Total deposits
totaldeposits.txt
Total withdrawals
totalwithdrawals.txt
Total transactions
totaltransactions.txt
Highest transaction
highestTransaction.txt
Total accounts
totalaccounts.txt

The program contains functions for updating and displaying these statistics.

📈 13. Most Active Account

The administrator can check which account has generated the highest number of tracked activities.

The system uses:

activeaccount.txt

to maintain activity counts.

The most_active() function then searches for the account with the highest activity count.

💵 14. Highest Transaction

The system can record and display the largest transaction amount.

The information is stored in:

highestTransaction.txt

The program compares a new transaction amount with the previously recorded highest amount and updates the record when appropriate.

💰 15. Highest and Lowest Balance

The administrator can also inspect accounts based on their balances.

The system contains a function called:

least_most()

which examines account balances and reports accounts associated with the largest and smallest balances.

🚫 16. Suspended / Banned Accounts

The administrator can check accounts whose password-failure status has reached the suspension threshold.

The system checks the account files and reports suspended accounts.

👨‍💻 17. Account Services

After logging in, users have access to:

1. Deposit Money
2. Withdraw Money
3. Delete Account
4. Balance Request
5. Send Money
6. Account Services
7. Exit

Account Services currently contains:

1. Change password
2. Change user name
3. Suspended account recovery
4. Transfer history
This provides users with basic account-management functionality.
🗑️ 18. Delete Account

Users can delete their account.

However, the current system requires the account balance to be zero before deletion.

Balance = 0
        ↓
Delete Account

If money remains in the account, the system asks the user to withdraw the remaining amount first.

📚 19. About, User Guide and Terms

The system contains separate information files for:

aboutbank.txt
user_guide.txt
termsandconditions.txt

The main menu allows users to access:

4. About INDI Bank?
7. User guide info
8. Terms and conditions

The program reads these files and displays their contents to the user.

💾 Data Storage

Vision 2 currently uses local text files rather than a database.

Account information is saved using account-specific files such as:

account1.txt
account2.txt
account3.txt
...

The save_account() method stores account information in a comma-separated format.

The project also uses several supporting files for different types of information.

Examples include:

account1.txt
account2.txt
account3.txt
account4.txt

admin.txt
transactions.txt
transferID.txt
highestTransaction.txt

totalaccounts.txt
totalwithdrawals.txt
totaldeposits.txt
totaltransactions.txt

activeaccount.txt
time.txt
student_withdraw.txt
names.txt

aboutbank.txt
user_guide.txt
termsandconditions.txt
🧱 Object-Oriented Design

One of the important parts of Vision 2 is the use of Object-Oriented Programming.

The main class is:

class BankAccount:

Specialized accounts inherit from it:

class Student_account(BankAccount):
    ...

class Business_account(BankAccount):
    ...

class Savings_account(BankAccount):
    ...

This allows different account types to have their own behavior while sharing functionality from the main BankAccount class.

This is one of the areas of the project where I am practicing inheritance and polymorphism.

🔄 Application Flow

The overall application begins with the main banking menu:

================ BANK MENU ================

1. Create Account
2. User Login
3. Suspended Account?
4. About INDI Bank?
5. System Admin Login
6. Recover Admin System Account
7. User Guide Info
8. Terms and Conditions
9. Exit

After logging in, the user enters the account services menu.

             INDI BANK
                 │
        ┌────────┴────────┐
        │                 │
   Create Account     User Login
        │                 │
        ▼                 ▼
 Account Type       Authentication
        │                 │
        │          ┌──────┴──────┐
        │          │             │
        │       Success        Failure
        │          │             │
        │          ▼             ▼
        │      User Menu     Attempt Count
        │          │             │
        │          ▼             ▼
        │    Banking Services  Suspension
        │
        ▼
   Account Created
🛠️ Technologies and Concepts Used
Programming Language
Python 🐍

The entire current application is written in Python.

Python Concepts

The project uses:

Variables
Strings
Integers
Floats
Lists
Conditional statements
Loops
Functions
Classes
Objects
Constructors
Inheritance
Methods
File handling
Exception handling
String manipulation
os module
time module
📁 Project Architecture

The current project is primarily a Python source file combined with local text files used for persistent storage.

A conceptual structure is:

INDI_BANK/
│
├── main.py
│
├── account1.txt
├── account2.txt
├── account3.txt
├── account4.txt
│
├── admin.txt
├── names.txt
├── transactions.txt
├── transferID.txt
├── highestTransaction.txt
│
├── totalaccounts.txt
├── totalwithdrawals.txt
├── totaldeposits.txt
├── totaltransactions.txt
│
├── activeaccount.txt
├── time.txt
├── student_withdraw.txt
│
├── aboutbank.txt
├── user_guide.txt
└── termsandconditions.txt

The exact filenames and number of account files can change as the project develops.

▶️ How to Run
Requirements

You need:

Python 3.x
A computer capable of running Python
The project source file
The required supporting text files
Step 1 — Download or Clone the Repository
git clone https://github.com/YOUR-USERNAME/INDI-Bank.git

Then enter the project directory:

cd INDI-Bank
Step 2 — Run the Program

Run the Python file:

python "Divine chisepo project vision2.py"

Depending on your Python installation, you may also use:

python3 "Divine chisepo project vision2.py"
⚠️ Important Security Notice

This project is an educational banking simulation.

It is NOT a real banking system and should not be used to store real:

Bank account information
Passwords
PINs
Identity numbers
Financial information

The current project uses local text files for storage and implements a custom password transformation system. This is suitable for learning programming concepts but should not be considered production-grade security.

⚠️ Current Development Limitations

Vision 2 is still a learning project.

Some areas of the current implementation require further development, testing, and security improvements.

Examples include:

Text-file storage instead of a database
Custom password hashing instead of an established password-hashing library
Limited input validation
Console-based interface
No real banking API
No encrypted database
No production authentication system
Limited transaction rollback/error recovery
Limited automated testing
Some features are still under development

These limitations are part of the reason I am continuing to develop the project.

🚀 Future Development

The project is intended to continue evolving.

🗄️ Database Integration

A future version can replace the current text-file system with:

SQLite

This would provide structured storage for:

Users
Accounts
Transactions
Account types
Authentication information
Administrative data
🌐 Web Application

A future version may transform the console application into a web application.

Possible architecture:

HTML
  +
CSS
  +
JavaScript
       │
       ▼
Python Backend
       │
       ▼
SQLite / Database
🔐 Improved Security

Future versions can use established security practices such as:

Secure password hashing
Salted password storage
Better authentication
Input sanitization
Access control
Secure sessions
Database security
Better account recovery
💳 Advanced Transaction System

Future development can include:

Complete transaction history
Transaction timestamps
Deposit records
Withdrawal records
Transfer records
Transaction status
Transaction references
Better failed-transaction handling
🧪 Automated Testing

Future versions can include tests for:

Account creation
Login
Password validation
Deposits
Withdrawals
Transfers
Account deletion
Account suspension
Account recovery
📈 Vision 2 Development Path
                    INDI BANK
                       │
                       ▼
                Vision 1
            Basic Banking System
                       │
                       ▼
                Vision 2
          ┌────────────┼────────────┐
          │            │            │
       Accounts     Transfers    Admin
          │            │            │
          ▼            ▼            ▼
      3 Account     Transaction   Statistics
        Types          IDs
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                Future Versions
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         SQLite Database     Web Application
             │                   │
             └─────────┬─────────┘
                       ▼
                Advanced System
🧠 What I Learned From Building This

This project has helped me understand that building software is different from simply learning programming syntax.

While developing INDI Bank, I have had to think about:

How data should be stored
How different classes interact
How users authenticate
How account types can behave differently
How transactions affect multiple accounts
How to handle invalid input
How to track system statistics
How to structure a larger Python program
How bugs can appear when different functions interact
How a project can be improved step by step

The project is therefore not just a banking program; it is also a practical learning environment for my development as a programmer.

📌 Project Status
🟡 Vision 2 — In Development

Current major components include:

Account Creation              ✅
User Login                    ✅
Password Validation           ✅
Multiple Account Types        ✅
Deposit                       ✅
Withdrawal                    ✅
Money Transfer                ✅
Transaction IDs               ✅
Transfer History              ✅
Account Deletion              ✅
Account Suspension            ✅
Account Recovery              ✅
Admin Login                   ✅
Admin Password Change         ✅
Bank Statistics               ✅
About Bank                    ✅
User Guide                    ✅
Terms & Conditions            ✅

Database                      🔄
Web Interface                 🔄
Advanced Security             🔄
Automated Testing             🔄
📜 Version History
Vision 1

The original project focused on creating a basic banking system and learning fundamental Python concepts.

Vision 2

Vision 2 expands the project with:

Object-oriented account classes
Student accounts
Savings accounts
Business accounts
Authentication
Password validation
Account suspension
Account recovery
Deposits
Withdrawals
Money transfers
Transaction IDs
Transfer history
Administrative functions
Banking statistics
Account activity tracking
👨‍💻 Developer
Divine Chisepo

BCA Student | Aspiring Software Developer | Technology Enthusiast

I am learning software development by building practical projects and gradually improving them as I learn new technologies.

Current areas of interest
🐍 Python
🌐 HTML
🎨 CSS
⚡ JavaScript
🗄️ Databases
💻 Software Development
🔧 Git & GitHub
🧠 Data Structures & Algorithms
⭐ Project Philosophy

Learn → Build → Find Problems → Improve → Build Again

INDI Bank is a project that will continue changing as my programming knowledge grows.

Vision 2 is not intended to be the final version.

It is another step in my journey toward becoming a software developer.

⚖️ Disclaimer

INDI Bank is an educational and experimental software project.

It is not affiliated with, connected to, or operated by any real bank or financial institution.

It does not process real-world financial transactions.

Do not use real personal, banking, identity, password, or financial information with this application.

🏦 INDI Bank — Vision 2

Built with Python 🐍 | Built for Learning 📚 | Built to Improve 🚀

© Divine Chisepo
👨‍💼 Manager/Admin Concept

The project includes a manager-related component for handling administrative functionality.
This provides a foundation for eventually adding features such as:

Viewing accounts
Managing users
Account administration
Monitoring transactions
Viewing user actions 
etc

📚 About / User Guide / Terms

The project also includes informational sections such as:
About
User Guide
Terms and conditions

These sections are intended to make the application easier to understand and use.

🛠️ Technologies Used
Current Technologies
Technology	Purpose
🐍 Python	Main programming language
📁 File Handling	Data storage
💻 Object-Oriented Programming	Planned/ongoing architecture
🔐 PIN Authentication	Basic account security
Planned Technologies
Technology	Planned Use
SQLite	Database storage
HTML	Web structure
CSS	Web design
JavaScript	Front-end functionality
Git	Version control
GitHub	Project hosting
GUI/Web Framework	Future user interface
⚙️ How the System Works

The basic workflow is:

                    ┌─────────────────┐
                    │    Indi_Bank    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Start Program  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  User Account   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Authentication  │
                    │     / PIN       │
                    └────────┬────────┘
                             │
                             ▼
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       Account Operations            Account Information
              │                             │
              ▼                             ▼
       Balance / Banking              Name / Account No.
              │                             │
              └──────────────┬──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      Exit       │
                    └─────────────────┘
👤 Account Information

An account can contain information similar to:

Name
Balance
PIN
Account Number
Account Type
Reg number
ID number
etc

Example:

Account Holder : Example User
Account Number : account123
Account Type   : Indi_Bank
Balance        : ₹0
ID Number      : ************
PIN            : ****

📂 Project Structure

The structure may change as the project develops.

A simplified representation is:

Indi_Bank/
│
├── main.py
│
├── programs/
│   ├── account1
│   ├── account2
│   ├── account3
│   ├── account4
│   └── manager
    and more
│
├── ABOUT
├── USER_GUIDE
├── TERMS
│
└── README.md

As the project develops, the structure can be reorganized into a cleaner architecture.

For example:

Indi_Bank/
│
├── main.py
├── bank/
│   ├── bank_account.py
│   ├── student_account.py
│   ├── savings_account.py
│   └── business_account.py
│
├── database/
│   └── bank.db
│
├── authentication/
│   └── auth.py
│
├── transactions/
│   └── transactions.py
│
├── ui/
│   └── ...
│
├── README.md
└── requirements.txt
🔄 Example Operations

A future version of Indi_Bank is planned to support operations such as:

Create Account
Enter your name:
Enter your PIN:
Create account
Check Balance
Account Number: 100001

Available Balance: ₹5,000
Deposit
Deposit Amount: ₹2,000

Updated Balance: ₹7,000
Withdraw
Withdrawal Amount: ₹1,000

Updated Balance: ₹6,000
Transfer

Future versions can allow better services
Security is an important area for future development.
The current project is not intended for real financial use.
The first version is primarily designed to demonstrate programming concepts.
Future versions will improve security through techniques such as:

Secure password/PIN hashing
Better authentication
Input validation
Database security
Session management
Transaction verification
Improved error handling
Protection against unauthorized access

⚠️ Current Limitations

Indi_Bank is still a developing learning project.
Current limitations may include:

File-based data storage
Basic authentication
Limited transaction functionality
Limited input validation
No real banking API
No connection to real bank accounts
No production-grade security
No real financial transactions

The system should therefore be considered a simulation/educational project.

🚀 Future Improvements

The project is intended to grow significantly beyond Vision 1.

Version 2 — Database

Planned improvements:

SQLite database
Structured account tables
Automatic account numbers
Persistent transaction records
Improved data management
Version 3 — Transactions

Deposit
Withdrawal
Money transfer
Transaction history
Transaction IDs
Transfer between accounts
Transaction timestamps

Example:

Transaction ID: TXN10001
Type: Transfer
From: 100001
To: 100002
Amount: ₹1,000
Status: Successful
Version 4 — Object-Oriented Architecture

The project can be redesigned using classes and inheritance.

Possible structure:

                 BankAccount
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Student      Savings     Business
      Account      Account      Account

Possible classes:

class BankAccount:
    pass

class StudentAccount(BankAccount):
    pass

class SavingsAccount(BankAccount):
    pass

class BusinessAccount(BankAccount):
    pass

This will allow the project to demonstrate:

Classes
Objects
Constructors
Inheritance
Polymorphism
Encapsulation
Method overriding
🌐 Web Version

One of the long-term goals is to transform Indi_Bank into a web-based application.

Possible technologies:

Frontend
HTML + CSS + JavaScript

        ↓

Backend
Python

        ↓

Database
SQLite / Other Database

The web version could include:

Login page
Dashboard
Account profile
Balance display
Deposit/withdrawal
Transfers
Transaction history
Account management
📊 Possible Dashboard

A future dashboard could look conceptually like:

╔══════════════════════════════════════╗
║             INDI_BANK                ║
╠══════════════════════════════════════╣
║ Welcome, User                        ║
║                                      ║
║ Available Balance                    ║
║ ₹25,000                              ║
║                                      ║
║ [Deposit] [Withdraw] [Transfer]     ║
║                                      ║
║ Recent Transactions                  ║
║ ───────────────────────────────────  ║
║ Deposit       +₹5,000                ║
║ Transfer      -₹1,000                ║
║ Withdrawal    -₹500                  ║
╚══════════════════════════════════════╝
🧠 Learning Outcomes

Working on Indi_Bank helps me practice several programming concepts.

Python
Variables
Data types
Conditions
Loops
Functions
Exception handling
File handling
Classes and objects
Inheritance
Polymorphism
Software Development
Project organization
Debugging
Version control
Git/GitHub
User input validation
Application design
Problem solving
Future Learning

The project will also give me practical experience with:

SQL
Databases
Web development
APIs
Authentication
Backend development
Software architecture
▶️ How to Run
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/Indi_Bank.git
2. Enter the Project Directory
cd Indi_Bank
3. Run the Program

If the main Python file is main.py:

python main.py

or:

python3 main.py
💻 Requirements

For the current version, you may only need:

Python 3.x

Check your Python installation:

python --version

If future versions use external Python packages, a requirements.txt file will be added.

📌 Project Status

Current Status: 🟡 In Development

Vision 1
████████████████░░░░

File-based system       ✅
Basic account system    ✅
Basic authentication    ✅
Information sections    ✅
SQLite database         🔄
Transactions            🔄
OOP architecture        🔄
Web interface           🔄
Advanced security       🔄

The project will continue to evolve as I learn new technologies and programming concepts.

⚖️ Disclaimer

Indi_Bank is an educational software project.

It is not connected to any real bank or financial institution and does not process real financial transactions.

Do not use real banking credentials, passwords, PINs, or financial information with this project.

👨‍💻 Author
Divine Chisepo

BCA Student | Aspiring Software Developer | Technology Enthusiast

Interested in:

🐍 Python
🌐 Web Development
💻 Software Development
🗄️ Databases
🧠 Problem Solving
🚀 Building practical projects

This project represents part of my journey from learning programming concepts to building practical software applications.

⭐ Support the Project

If you find this project useful for learning, feel free to:

⭐ Star the repository
🍴 Fork the project
💡 Suggest improvements
🐛 Report issues
🔧 Contribute ideas

📜 Version History
Vision 1.0
Initial banking system
File-based data management
Basic account structure
PIN-based access
Manager/admin concept
User information and guide sections
Future

The project will gradually move toward:

File-Based Banking System
          ↓
SQLite Database
          ↓
Object-Oriented Architecture
          ↓
Transaction Management
          ↓
Web Application
          ↓
Full Banking Management Simulation

Made with Python and a lot of learning. 🐍💻

Indi_Bank — Vision 1
* File handling
* Data storage
* User input
* Conditional statements
* Functions
* Loops
* Basic authentication
* Account management
* Python programming
* Program organization

The project is intentionally designed as a learning project rather than a real banking application.

---

# 🎯 Why I Built This

I built Indi_Bank to move beyond simply learning programming syntax and start building something practical.
Instead of learning concepts independently, I wanted to combine them into one project that could continue growing as my programming skills improve.
The project also gives me an opportunity to practice software development concepts that are useful for future projects and professional development.
My long-term goal is to develop this project from a simple file-based application into a more complete banking management system.

---

# ✨ Features

## 👤 Account Management

The system supports the basic concept of creating and managing bank accounts.
Account information can include:

* Account holder name
* Account number
* PIN
* Balance
* Account type

---

## 💰 Balance Management

The system maintains an account balance and provides functionality related to the user's available funds.
The default balance for a new account can be set to 0


## 🔐 PIN Authentication

Accounts use a PIN-based authentication system.

Users are required to provide their PIN when accessing protected account functionality.

---

## 🏦 Account Types

The project is designed to support different types of accounts which are:
* Student Account
* Savings Account
* Business Account

---

## 📁 File-Based Data Storage

The first version of the project uses files to store information.

This allowed me to practice Python file-handling concepts such as:

* Reading files
* Writing files
* Appending data
* Managing stored information
The project may eventually migrate from file-based storage to a database.

---

## 👨‍💼 Manager/Admin Concept

The project includes a manager-related component for handling administrative functionality.

This provides a foundation for even

