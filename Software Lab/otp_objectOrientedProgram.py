import random
import senders_data as Get
import smtplib
import unittest

class otp_generation(unittest.TestCase):
    
    #Getting Login credentials from sender_data file
    Email_id=Get.email
    password=Get.password

    def __init__(self,r_name,r_email,n):
        self.receivers_name=r_name
        self.receivers_email=r_email
        self.n=n
        OTP=self.genrate_otp(self.n)
        

        #Testing OTP's length
        self.assertBetween(self.n,4,8)

        #Validation of Email ID
        self.email_validation()

        self.send_email(OTP)
    
    def genrate_otp(self,n):
        self.n=n
        OTP=""
        for i in range(self.n):
            OTP+=str(random.randint(0,9))
        return (OTP)    
    
    def assertBetween(self, n, low, hi):
        if not (low <= n <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (n, low, hi))
        print("\n")
    
    def email_validation(self):
        email="pooja.pmd25@gmail.com"
        check_email =("@" and "gmail" and "." and "com") in email #self.receivers_email
        if check_email:
            print("No error in email")
            print("\n")
        else:
            self.assertTrue(check_email)

    def send_email(self,OTP):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.Email_id,self.password)
        
        msg=("Hi {}\n{} is your otp. Don't share your OTP with anyone !".format(self.receivers_name,OTP))
        print(msg)
        server.sendmail(self.Email_id,self.receivers_email,msg)
        server.quit()
        print("Email is send  kindaly check your email.")

g=otp_generation('Pooja','pooja.pmd25@gmail.com',4)
