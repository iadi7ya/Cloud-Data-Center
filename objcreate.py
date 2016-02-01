#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
user=os.environ.get("HTTP_COOKIE")
if user:
  print "Content-type: text/html\n\n"


  print "<html>"
  print "<head>"
  print "<title>SRMS Cloud Services</title>"
  print "<script type='text/javascript'>"
  print "window.history.forward(1);"
  print "function noBack(){ window.history.forward();}"
  print "</script>"

  print "</head>"
  print "<body onload='noBack();' onpageshow='if (event.persisted)noBack();' onunload=''>"

  print "<div id='header' style='height:75px; background-color:orange;'>"
  print "<span style='font-size:30px;'><center>SRMS CLOUD SERVICES</center></span><span style='margin-left:700px;margin-top:-1px'>"+user+"&nbsp;&nbsp;<a href='logout.py'>Logout</a></span>"

  print "</div>"
  print "<div id='body'>"
  print "<div id='body1'>"
  print "<h2><center>OBJECT STORAGE AS A SERVICE</center></h2><br/>"
  print "<h3><center>Create Drive</center></h3>"
  print "<p id='Storage Flavours'><center>Your Available Storage Flavours</center></p><br/><br/>"
  print "<form id='obj' method='post' action='/cgi-bin/objserver.py'><center>"
  print "<input type='radio' id='obj' name='obj' value='flavour1'>Flavour 1: 1 GiB Storage Space</input><br/><br/>"
  print "<input type='radio' id='obj' name='obj' value='flavour2'>Flavour 2: 2 GiB Storage Space</input><br/><br/>"
  print "<input type='radio' id='obj' name='obj' value='flavour3'>Flavour 3: 5 GiB Storage Space</input><br/><br/>"
  print "<input type='submit' name='Submit' value='Submit' /></input><br/><br/>"

  print "</center></form>"
  print "</body>"
  print "</html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""

