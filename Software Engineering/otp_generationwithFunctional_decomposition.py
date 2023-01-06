# Program to generate one time password and send it to registered email id

import math
import random
import senders_data
import smtplib  #simple message transfer protocol library to send email to users

n=(int(input("Enter your range of otp ")))  #Taking input for length of otp

#function to generate otp
def generateOTP(n):
    OTP=""

    for i in range(n):
        OTP+=str(random.randint(0,9))   #OTP will take any random digits from(0,9)
    return (OTP)

#create gmail server    
server = smtplib.SMTP('smtp.gmail.com', 587)
    
#get senders email from another file
Email_id = senders_data.email
password = senders_data.password
    
#function to login and add tls to the server
def login_Email_id():
    server.starttls()           #transfered layer security
    server.login(Email_id,password=password)

r_name=input("Enter receivers name: ") 
r_email=input("Enter receivers email: ")

#function to send email
def send_email():
    login_Email_id()
    otp_var=generateOTP(n)
    msg=("Hi "+ r_name +"\n"+ str(otp_var)+" is your OTP ")
    print(msg)
    server.sendmail(Email_id,r_email,msg)
    server.quit() #to quit the server
    print("OTP is verified")

#function calling
send_email()
