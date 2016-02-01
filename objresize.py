#!/usr/bin/python
import cgi
import cgitb
import os
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
  print "<h3><center>Resize Drive</center></h3>"
  print "<form id='obj' method='post' action='/cgi-bin/objresizeserver.py'><center>"
  print "Extra Size&nbsp;&nbsp;<input type='text' id='res' name='res' placeholder='Extra Size Required in GiB'</input>&nbsp;&nbsp;"
  print "<input type='submit' name='Submit' value='Submit' /></input><br/><br/></center>"
  print "<center><a href='home.py'>Home</a>&nbsp;&nbsp;"
  print "<a href='objhome.py'>Object Storage Home</a></center>"
  
  print "</form>"
  print "</body>"
  print "</html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""


