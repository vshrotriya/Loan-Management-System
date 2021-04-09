import os,sys
import json
from random import randint
from datetime import timedelta, date

# function to handle login requests from admin and user 
def login(user_type):
    user_email = input("Email : ")
    password = input("Password : ")
    # snippet to handle admin login
    if(user_type == 'admin'):
        with open('./txts/admin.txt') as json_file:
            data = json.load(json_file)
            # verifying if login credentials are valid 
            if(user_email == data['admin_email']and password == data['admin_password']):
                return True
            else:
                return False 
    else:
    # snippet to handle user login 
        with open('./txts/reg_user.txt') as json_file:
            data = json.load(json_file)
            data = data[user_email]
            try:
            # verifying if login credentials are valid 
                if(user_email == data['email']and password == data['password']):
                    return user_email , True
            except:
                    return False 