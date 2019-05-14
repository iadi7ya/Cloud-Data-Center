#!/usr/bin/python
import cgi
import cgitb
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

print "<link rel='stylesheet' type='text/css' href='login.css' />"
print "</head>"
print "<body onload='noBack();' onpageshow='if (event.persisted)noBack();' onunload=''>"

print "<div id='header' style='height:50px; background-color:orange;'>"
print "<span style='font-size:35px;'><center>SRMS CLOUD SERVICES</center></span>"
print "</div>"
print "<div id='body'>"
print "<div id='body1'>"


print "<p id='heading'>Log in</p>"

print "<form id='login' method='post' action='/cgi-bin/login.py' >"

print "<table><tr><td>Email</td><td><input type='email' id='email' name='email' placeholder='someone@example.com' maxlength='30' /></td></tr>"
print "<tr><td>Password</td><td><input type='password' id='password' name='password' placeholder='Password' maxlength='15' /></td></tr>"
print "<tr><td colspan='2'><input type='submit' name='Submit' value='Login' /></td></tr></table>"

print "</form>"

print "<a href='cpass.py' id='cpass' name='cpass'>Forgot your password?</a><br/>"


print "</div>"

print "<div id='body2' style='position:relative; margin-left:450px; margin-top:-160px;'>"
print "<form id='signup' method='post' action='/cgi-bin/signup.py' >"

print "<table><tr><td colspan='2'>SignUp</td></tr><tr><td>Full Name</td><td><input type='text' id='fname' name='fname' placeholder='full name' /></td></tr>"
print "<tr><td>Email</td><td><input type='email' id='email' name='email' placeholder='someone@example.com' /></td></tr>"
print "<tr><td>Password</td><td><input type='password' id='password' name='password' placeholder='Password' /></td></tr>"
print "<tr><td>Retype Password</td><td><input type='password' id='cpassword' name='cpassword' placeholder='Re-enter Password' /></td></tr>"
print "<tr><td>SAAS username</td><td><input type='text' id='user' name='user' placeholder='eg. ab12 etc. .,_not allowed' /></td></tr>"
print "<tr><td>Mobile Number</td><td><input type='tel' pattern='[0-9]{10,10}' maxlength='10'  id='phno' name='phno' placeholder='Mobile Number' /></td></tr>"
print "<tr><td colspan='2'><input type='submit' name='Submit' value='SignUp'/></td></tr></table>"
print "</div>"
print "</div>"
print "<div id='footer' style='margin-top:310px'>"
print "<p>&copy;SRMS Cloud Services.</p>"
print "</div>"
print "</body>"
print "</html>"
