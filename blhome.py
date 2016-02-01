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
  print "<h2><center>BLOCK STORAGE AS A SERVICE</center></h2><br/>"
  print "<p id='Storage Services'><center>Your Available Storage Services</center></p><br/><br/>"
  print "<center><a href='blclient.py' id='block' name='block'>Connect to Drive</a>&nbsp;&nbsp;"
  print "<a href='blresize.py' id='block' name='block'>Resize Drive</a>&nbsp;&nbsp;"
  print "<br/><br/><center><a href='home.py'>Home</a>&nbsp;&nbsp;"

  print "</body>"
  print "</html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""

