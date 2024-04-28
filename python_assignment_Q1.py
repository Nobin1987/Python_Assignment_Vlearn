#  In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

# ●       Implement a Python function called check_password_strength that takes a password string as input.

# ●       The function should check the password against the following criteria:

# ○       Minimum length: The password should be at least 8 characters long.

# ○       Contains both uppercase and lowercase letters.

# ○       Contains at least one digit (0-9).

# ○       Contains at least one special character (e.g., !, @, #, $, %).

# ●       The function should return a boolean value indicating whether the password meets the criteria.

# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

# ●       Provide appropriate feedback to the user based on the strength of the password.  

import re as R
def check_password_strength(y)  :
    if len(y) < 9 : 
        print (" Your password length is  " , str(len(y)))
        result_pass = False
    elif len(R.findall("[!@#$%^&*]", y))< 1 :
        print (" Your password is missing special char  " )
        result_pass = False
    elif len(R.findall("[a-z]",y)) < 1 : 
        print (" Your password is missing lower case char  " )
        result_pass = False
    elif len(R.findall("[A-Z]",y))  < 1 : 
        print (" Your password is missing upper case char  " )
        result_pass = False
    else:
        result_pass = True
    return result_pass

pass1=str(input("Please enter the passwdord which needs to be checked :" ))
if check_password_strength(pass1) :
    print("your password has been validated and meets the required strength")
else:
    print("""
          Your password failed to meet the required strength.Your password should meet following criteria.
          Minimum length: The password should be at least 8 characters long.
          Contains both uppercase and lowercase letters.
          Contains at least one special character (e.g., !, @, #, $, %).
          Contains at least one digit (0-9).
          """)


