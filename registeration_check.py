#!/usr/bin/python3
import cgi
import cgitb
import smtplib
cgitb.enable()
print('Content-type:text\html')
print("")

getdata = cgi.FieldStorage()
user_email = getdata.getvalue('useremail')

# creating smtp server instance
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
link = #enter the database registeration link
message = 'Click on the link below to successfully complete your registeration'+link

s.sendmail("piyushmittal.agarwal2@gmail.com",user_email,message)
s.quit()

print('Hey Welcome , Wanna test yourself?')
print('</br> just click on the link send to your mail to successfully register yourself and start the test')
