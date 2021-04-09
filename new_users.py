# importing libraries and modules
import os,sys
import json
from random import randint
from datetime import timedelta, date
from loan_calculator import *

# Function to get data from user for registration purpose
def get_data():
    data = {}
    email = input("Enter your Email ID : ")
    
    data[email] = {
        "email" : email,
       "name" : input("Enter your name : "),
       "adress" : input("Enter your address : "),
       "contact" : input("Enter your contact number : "),
       "gender" : input('''
       Enter Gender as 
       M for Male
       F for Female
       T for Transgender 
       O for Other

       '''),
       "dob" : input("Enter your Date of Birth as [dd/mm/yyyy] : "),
       "loan_type" : input('''
       Enter code of type of loan you want
        1. Education Loan (EL)
        2. Car Loan (CL)
        3. Home Loan (HL)
        4. Personal Loan (PL)

       '''),
       "loan_term" : input("Enter the time period of loan in years : "),
       "instal_amt" : int(input("Enter the Instalment Amount : ")),
       "user_id" : input("Enter user id : "),
       "password" : input("Enter Password : "),
       "re_pass" : input("Re-Enter Password : "),
    }
    update = data[email]
    while(update['password'] != update['re_pass']):
        update['password'] = input("Enter Password")
        update['re_pass'] = input("Re-Enter Password")
    data[email] = update
    return data

# Function to handle Registration process
def register():
    data = get_data()
    with open("./txts/new_user.txt", "r+") as f:
        obj = json.load(f)
        obj.update(data)
        f.seek(0)
        json.dump(obj, f)

# Function to print loan Details 
def loan_details():
# Menu Driven approach
    print('''
             ====================================================
            | Enter What type  of loan details you want to see   |
            | 1. Education Loan (EL)                             |
            | 2. Car Loan (CL)                                   |
            | 3. Home Loan (HL)                                  |
            | 4. Personal Loan (PL)                              |
             ====================================================
            ''')
    choice = input("Enter your Choice code such as EL , CL , HL , PL : ")
    with open('./txts/loan_info.txt') as json_file:
        data = json.load(json_file)
        info = data[choice]
# Printing loan info like loan type, ROI, Eligibility Criteria, Time Period
        print(f'''
            Loan Type 
                {info['loan_type']}
            Rate of Interest
                {info['interest']} 
            Eligibility Criteria 
                {info['eligibility_criteria']}
            Time Period
                {info['time_period']}
        ''')

# Function to handle loan calculation

def loan_calc():
    amt = int(input('Enter the Loan Amount : '))
    loan_type = input('Enter code of Loan type such as EL,CL,HL,PL : ')
    instal_amt = int(input('Enter the Instalment amount to pay per month : '))
    pay_day = int(input('Enter day of month you want to make payment on : '))
    date_end = date.today() + timedelta(days=randint(1,10))
    if loan_type == 'EL':
        car = Loan('Education Loan', amt, 0.08, date_end)
        car.pay(instal_amt, pay_day, Loan.PaymentFrequency.monthly)
    if loan_type == 'CL':
        car = Loan('Car Loan', amt, 0.12, date_end)
        car.pay(instal_amt, pay_day, Loan.PaymentFrequency.monthly)
    if loan_type == 'HL':
        car = Loan('Home Loan', amt, 0.07, date_end)
        car.pay(instal_amt, pay_day, Loan.PaymentFrequency.monthly)
    if loan_type == 'PL':
        car = Loan('Personal Loan', amt, 0.06, date_end)
        car.pay(instal_amt, pay_day, Loan.PaymentFrequency.monthly)     

# New User Panel
def new_user():
    while(True):
    # Menu Driven Approach 
        print(''' 
         ================================================
        | Enter What you want to do                      |
        | 1. Register                                    |
        | 2. Check Loan Details                          |
        | 3. Calculate Loan Amount using Loan Calculator |
        | 4. Return to main menu                         |
         ================================================
        ''')
        choice = int(input("Enter your Choice : "))
        if(choice == 1):
            register()
        if(choice == 2):
            loan_details()
        if(choice == 3):
            loan_calc()
        if(choice == 4):
            break