#!/usr/bin/python
import os
import MySQLdb
import cgi, cgitb
cgitb.enable()
form1=cgi.FieldStorage(keep_blank_values=True)
db=MySQLdb.connect("192.168.0.100","clouduser","maestro","cloud")
cursor=db.cursor()
name=form1.getvalue('fname')
email=form1.getvalue('email')
passw=form1.getvalue('password')
mob=form1.getvalue('phno')
user=form1.getvalue('user')

cursor.execute("INSERT INTO cloudsignup(name,email,password,mob,statusobj,statusbl,user) VALUES('%s','%s','%s','%s','%s','%s','%s');" % (name,email,passw,mob,'0','0',user))
db.close()

#os.system("sudo iptables -F")
#os.system("sudo setenforce 0")
os.system("useradd %s"% user)
os.system("echo %s | passwd %s --stdin" % (user,passw))
print "Set-Cookie: %s" % (email)
print "Status: 303 See other"
print "Location: http://192.168.0.100/cgi-bin/home.py"
print ""


