import os,sys
import json
from random import randint
from datetime import timedelta, date
from logins import *

# Fuunction to print loan details of logged in customer 
def loan_details_user(email):
    with open('./txts/reg_user.txt') as json_file:
        data = json.load(json_file)
        data = data[email]
        print(f'''
        Loan Details                                  
        Loan type           : {data['loan_type']}     
        Loan term           : {data['loan_term']}     
        Instalment Amount   : {data['instal_amt']}    
        Loan ID             : {data['loan_id']}       
        ''')

# Function to pay Instalment by Reg user 
def pay_instalment(email):
    with open('./txts/reg_user.txt','r+') as json_file:
        data = json.load(json_file)
        info = data[email]
        instal_amt = int(input('Enter the Instalment Amount'))
        loan_stat = info['loan_status']
        left =  int(loan_stat['Left_Amt'])
        # Menu driven Approach
        choice = int(input('''
         ========================
        | Enter                  |
        | 1. Complete Payment    |
        | 2. Cancel              |
         ========================
         '''))
        if(choice == 1):
            # Updating data in left balance 
            left = left - instal_amt
            loan_stat['Left_Amt'] = left
            info['loan_status'] = loan_stat
            data[email] = info
            json.dumps(data)
        else:
            return

# Function to see own transactions 
def see_transactions_user(email):
    with open('./txts/reg_user.txt') as json_file:
        data = json.load(json_file)
        data = data[email]
        print(data['transaction_history'])

# Function to see loan status 
def loan_status_user(email):
    with open('./txts/reg_user.txt') as json_file:
        data = json.load(json_file)
        data = data[email]
        data = data['loan_status']
        print(f'''
         ============================================
        | Loan Status                                |
        | Initial Amount   : {data['Initial_Amt']}   |
        | Left Amount      : {data['Left_Amt']}      |
         ============================================
        ''')

# User Panel 
def user():
    email,flag = login('user')
    if(flag==True):
        print('Welcome to User panel')
        while(True):
            # Menu driven approach for user panel
            print(''' 
             =============================
            | Enter What you want to do   |
            | 1. See Loan Details         |
            | 2. Pay Loan Instalment      |
            | 3. See Transactions         |
            | 4. Check status of Loan     |
            | 5. Logout                   |
             =============================
            ''')
            choice = int(input("Enter your Choice : "))
            # Calling functions based on input from the user
            if(choice == 1):
                loan_details_user(email)
            if(choice == 2):
                pay_instalment(email)
            if(choice == 3):
                see_transactions_user(email)
            if(choice == 4):
                loan_status_user(email)
            if(choice == 5):
                break
    else:
        print('Invalid Login Credentials \n Try again')
