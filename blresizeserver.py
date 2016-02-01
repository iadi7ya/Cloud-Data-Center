#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
def resize() :
   user=os.environ.get("HTTP_COOKIE")
   size=form.getvalue('res')
   os.system("lvextend --size +"+size+"G /dev/staas_blockvg/"+user)
   os.system("resize2fs /dev/staas_blockvg/"+user)
   print "Status: 303 See other"
   print "Location: http://192.168.0.100/cgi-bin/home.py"
   print ""
resize()

