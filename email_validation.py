# email validation using regex

import re

email_condition = r"^[a-z]+[._]?[a-z0-9]+@\w+\.\w{2,3}$"

email = input("enter your email: ")
if re.search(email_condition,email):
    print("valid email")
else:
    print("invalid email")




















