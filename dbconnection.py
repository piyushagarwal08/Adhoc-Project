#!/usr/bin/python
import mysql.connector as mysql
import cgi
# RDS information
username='root'
password='vijay'
database_name='project1'
host='localhost'

# Now connecting the Database
conn=mysql.connect(user=username,password=password,database=database_name,host=host)

# Now generating a SQL language cursor 
cur = conn.cursor()

# gat value from form
form = cgi.FieldStorage()
first_name = form.getvalue("firstname")
last_name = form.getvalue("lastname")
user_email = form.getvalue("useremail")
mobile = int(form.getvalue("mobile"))
user_password = form.getvalue("userpassword")

# insert
sql = "INSERT INTO userInfo (user_first_name, user_last_name, user_email, user_phone, user_password) VALUES (%s, %s, %s, %s, %s)"
val = (first_name,last_name,user_email,mobile,user_password)
cur.execute(sql, val)

conn.commit()    
# closing connection
conn.close()
