import random
otp = random.randint(100000,999999)
input_name = str(input("Enter your name: "))
if input_name.isalpha() == False:
    print("Enter a valid name")
    input_name = str(input("Enter your name: "))
input_email = str(input("Enter your email: "))
if "@" not in input_email:
    print("Enter a valid email")
    input_email = str(input("Enter your email: "))
#use can use import smtplib for sending otp to email
#from that you can send otp to email 
print(otp)
input_otp = int(input("Enter the otp: "))
if otp == input_otp:
    print("You have successfully logged in")
else:
    print("You have entered wrong otp")
