#!/usr/bin/python
import MySQLdb
import cgi
import cgitb
import os
cgitb.enable()
user=os.environ.get("HTTP_COOKIE")
#print "Content-type: text/plain"
#print ""
#
db=MySQLdb.connect("192.168.0.100","clouduser","maestro","cloud")
cursor=db.cursor()
cursor.execute("select statusbl from cloudsignup where email='%s'" %(user))
(data,)=cursor.fetchone()
#print data
if data=='0':
    print "Status: 303 See other"
    print "Location: http://192.168.0.100/cgi-bin/blcreate.py"
    print ""
else :
    print "Status: 303 See other"
    print "Location: http://192.168.0.100/cgi-bin/blhome.py"
    print ""

