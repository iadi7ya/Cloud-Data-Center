#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
user=os.environ.get('HTTP_COOKIE')
if user :
  print "Content-type: text/html\n\n"


  print "<html>"
  print "<head>"
  print "<title>SRMS Cloud Services</title>"
  print "<script type='text/javascript'>"
  print "window.history.forward(1);"
  print "function noBack()\n"
  print "{\n"
  print " window.history.forward();\n"
  print "}"
  print "</script>"

  print "</head>"

  print "<body onload='noBack();' onpageshow='if (event.persisted)noBack();' onunload=''>"

  print "<div id='header' style='height:75px; background-color:orange;'>"
  print "<span style='font-size:30px;'><center>SRMS CLOUD SERVICES</center></span><span style='margin-left:700px;margin-top:-1px'>"+user+"&nbsp;&nbsp;<a href='logout.py'>Logout</a></span>"
  print "</div>"
  print "<div id='body'>"
  print "<div id='body1'>"

  print "<br/><br/>"
  print "<p><center>Your Available Services are : <br/><br/></p> "
  print "<a href='saashome.py' id='saas' name='saas'>Software as a Service</a>&nbsp;&nbsp;"
  print "<a href='objfirst.py' id='obj' name='obj'>Object Storage</a>&nbsp;&nbsp;"
  print "<a href='blfirst.py' id='block' name='block'>Block Storage</a>&nbsp;&nbsp;"
  #print "<a href='iaashome.py' id='iaas' name='iaas'>Infrastructure As A Service</a></center>"
  print "</body>"
  print "</html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""
