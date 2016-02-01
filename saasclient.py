#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
form=cgi.FieldStorage()
#stat=form.getvalue('stat')
#if stat=='1048':
 # soft="firefox"
#else :
 # soft="gedit"
  
user=os.environ.get("HTTP_COOKIE")
(soft_name,soft)=os.environ.get("HTTP_COOKIE['software']")
if user:
  print "Content-type: text/html\n\n"
  print ""


  print "<html>"
  print "<head>"
  print "<title>SRMS Cloud Services</title>"
  print "<script type='text/javascript'>"
  print "window.history.forward(1);\n"
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
  print "<p><center>Click on the Download Link to download the script.</center><br/><center>Execute the Script by double clicking it to access your softwares!!!</center> </p><br/><br/><center>"
  print "<center><a href='http://192.168.0.100/scripts/saas_"+soft+"_"+user+".py'>Download Script</a></center><br/><br/>"
  print "<center><a href='home.py'>Home</a></center>"
  print "</body></html>"
else :
  print "Status: 303 See other"
  print "Location: http://192.168.0.100"
  print ""

