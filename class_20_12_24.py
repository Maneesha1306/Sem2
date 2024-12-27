import re
def verify_password(passwd):
    ex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*["!@#$%^&*()+_-]).{8,}$'
    if re.match(ex,passwd):
        print("Strong")
    else:
        print("Not strong")

verify_password("Mic1306#")