import os,sys
import json
from random import randint
from datetime import timedelta, date
from logins import *
# function to approve new registration requests
def approve_req(data):
    with open('./txts/reg_user.txt','r+') as f:
        try:
            obj = json.load(f)
        except:
            obj = {}
        data['loan_id'] = randint(100000, 999999)
        end_date = date.today() + timedelta(days=randint(1,10))
        data['instal_date'] = str(end_date)
        data['instal_amt'] = randint(20,40)*100
        data['transaction_history'] = {}
        info = {}
        email = data['email']

        info[email] = data
        obj.update(info)
        f.seek(0)
        json.dump(obj, f)
        return True
        
        
# function to handle new registration requests
def new_requests():
# File Handling to see new requests
    with open('./txts/new_user.txt') as json_file:
        data = json.load(json_file)
        for lines in data:
        # Printing the new requests
            print(data[lines])
        choice = int(input('''
            ============================
            | 1. Approve Requests       |
            | 2. Go to Previous Menu    |
            ============================
        '''))
        while(True):
            if (choice == 1):
                email = input("Enter Email id of the customer : ")
                flag = approve_req(data[email])
                if flag:
                    data[email] = {}
            else:
                return
            choice = int(input('''
            ============================
            | 1. Approve Requests       |
            | 2. Go to Previous Menu    |
            ============================
        '''))


# Function to see Transaction customer specific using email id 
def customer_specific_transaction():
    with open('./txts/reg_user.txt','r+') as f:
        try:
            obj = json.load(f)
        except:
            print("No customer is registered yet")
            obj = {}
            return
        choice = input("Enter Customer Email id : ")
        data = obj[choice]
        print(data['transaction_history'])

# Function to see Transaction loan specific using email id 
def loan_specific_transaction():
    with open('./txts/reg_user.txt','r+') as f:
        try:
            obj = json.load(f)
        except:
            print("No loan transaction is done yet")
            obj = {}
            return
        choice = input("Enter Code of Loan (EL , HL , CL , PL) : ")
        for lines in obj:
            info = obj[lines]
            if(info['loan_type']==choice):
                print(info['transaction_history'])

# Function to see all Transactions
def customer_all_transaction():
    with open('./txts/reg_user.txt','r+') as f:
        try:
            obj = json.load(f)
        except:
            print("No transaction is done yet")
            obj = {}
            return
    for lines in obj:
        info = obj[lines]
        print(lines)
        print(info['transaction_history'])


# Function to see all loan Transactions 
def loan_all_transaction():
    with open('./txts/reg_user.txt','r+') as f:
        print('yes')
        obj = json.load(f)
        loan_type = ['EL','PL','CL','HL']
        for data in loan_type:
            print(data)
            for lines in obj:
                info = obj[lines]
                if(info['loan_type']==data):
                    print(info['transaction_history'])


# Admin Panel 
def admin():
    if(login('admin')==True):
        print('''
        ======================
        Welcome to Admin Panel
        ======================
        ''')
        while(True):
            # Menu driven approach for admin panel
            print(''' 
            ==================================================================
            | Enter What you want to do                                       |
            | 1. See and Approve new Requests                                 |
            | 2. See all transaction made by specific customer using email id |
            | 3. See all transactions of specific Loan type (EL/CL/HL/PL)     |
            | 4. See all transaction of all customer                          |
            | 5. See all transaction of all loan types                        |
            | 6. Logout                                                       |
            ==================================================================
            ''')
            # Taking input from user
            choice = int(input("Enter your Choice : "))
            # Calling functions based on input from the user
            if(choice == 1):
                new_requests()
            if(choice == 2):
                customer_specific_transaction()
            if(choice == 3):
                loan_specific_transaction()
            if(choice == 4):
                customer_all_transaction()
            if(choice == 5):
                loan_all_transaction()
            if(choice == 6):
                break
    else:
        print('Invalid Login Credentials \n Try again')
