import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""

for i in range(4):
    OTP+=digits[math.floor(random.randint(0,9))]
otp = OTP + "is your OTP"
msg = otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("pooja.pmd25@gmail.com", "nhng bebp acuh awjt")
emailid = "poojadeokar96@dbatu.ac.in"

s.sendmail('pooja.pmd25@gmail.com', emailid, msg)
a = input("Enter Your OTP >>: ")

if a == OTP:
    print("Verified")
else:
    print("Please check your OTP again")
