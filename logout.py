#!/usr/bin/python
import cgi
import cgitb
import os
import datetime
cgitb.enable()
user=os.environ.get("HTTP_COOKIE")
print "Set-Cookie: %s; Expires: datetime.datetime.now().time();"% user
print "Status: 303 See other"
print "Location: http://192.168.0.100/index.py"
print ""
