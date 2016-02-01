#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
user=os.environ.get('HTTP_COOKIE')
if user :
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

  print "<h2><center>SOFTWARE AS A SERVICE</center></h2><br/><br/>"
  print "<p id='heading'><center>AVAILABLE SOFTWARES</center></p><br/><br/>"

  print "<form id='soft' method='post' action='/cgi-bin/saas.py'><center>"
  print "<input type='radio' id='soft' name='soft' value='firefox'>Mozilla Firefox</input>&nbsp;&nbsp;"
  print "<input type='radio' id='soft' name='soft' value='gedit'>Gedit Text-Editor</input>&nbsp;&nbsp;"
  print "<input type='submit' name='Submit' value='Generate Script' /></input><br/><br/></center>"
  print "<center><a href='home.py'>Home</a>&nbsp;&nbsp;"

  print "</form>"
  print "</body>"
  print "</html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""

