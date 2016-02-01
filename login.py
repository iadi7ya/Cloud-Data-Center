#!/usr/bin/python
import cgi
import cgitb
import MySQLdb
cgitb.enable()
form1 = cgi.FieldStorage()
email=form1['email'].value
passw=form1['password'].value
user=''
db=MySQLdb.connect("192.168.0.100","clouduser","maestro","cloud")
cursor=db.cursor()
cursor.execute("Select * from cloudsignup where email = '%s' and password = '%s'" % (email,passw))
data=cursor.fetchall()
for i in email:
    if i == '@' :
             break
    else :
             user=user+i
db.close()
if data :
    print "Set-Cookie: %s" % user
    print "Status: 303 See other"
    print "Location: http://192.168.0.100/cgi-bin/home.py"
    print ""

else :
   print "Status: 303 See other"
   print "Location: http://192.168.0.100/cgi-bin/index.py"
   print ""

