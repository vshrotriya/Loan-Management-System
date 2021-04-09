# importing libraries and modules
import os,sys
import json
from random import randint
from datetime import timedelta, date
import datetime
from enum import Enum
import locale
from admin_panel import *
from reg_user import *
from new_users import *

print('''
    ===============================================================
    Welcome to Malaysia Bank Online Loan Management System (MBOLMS)
    ===============================================================
    ''')
while(True):
# Menu Driven approach 
    print('''
    =======================
    | 1. Admin             |
    | 2. Registered User   |
    | 3. New User          |
    | 4. Exit              |
    =======================
    ''')
    # Taking input from user 
    choice = int(input("Enter your Choice : "))
    if(choice == 1):
        admin()
    if(choice == 2):
        user()
    if(choice == 3):
        new_user()
    if(choice ==4):
        print("Thanks for Visiting Malaysia Bank")
        break