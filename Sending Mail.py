import smtplib
import getpass
import imaplib
import email
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
email=input("Enter your email: ")
password=getpass.getpass("Enter your password: ")
try:
    
    server.login(email,password)
except:
    print("Sorry! Invalid Credentials.")
    exit()
else:
    from_add=email
    to_add=input("Recipent: ")
    subject = input('Subject : ')
    message = input('Body : ')
    msg = "Subject: " +subject+'\n'+message
    server.sendmail(from_add,to_add,msg)
    print("Mail Sent Successully!")
server.quit()
