#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
def saas_log() :
   os.system("iptables -F")
   os.system("setenforce 0")
   user=os.environ.get("HTTP_COOKIE")
   passw="maestro"
   soft=form.getvalue('soft')
   print "Set-cookie: software=%s"% soft
   if user:
     flag=0
     for item in os.listdir("/var/www/cgi-bin/scripts") :
        if item == "saas_"+soft+"_"+user+".py" :
          flag=1
          break
     if flag == 0 :
        f1=open("/var/www/cgi-bin/scripts/saas_"+soft+"_"+user+".py","a+")
        f1.write("#!/usr/bin/python\nimport cgi\nimport cgitb\ncgitb.enable()\nprint 'Content-type: application/download'\nprint '' \n\n")
        f1.write("print '#!/usr/bin/python'\nprint 'import os'\nprint 'import cgi'\nprint'import cgitb'\nprint'cgitb.enable()'\n\n")
        f1.write("passw ='%s'\n" %(passw))
        f1.write("soft = '%s'\n" % (soft))
        f1.write("print \"os.system('iptables -F')\"\n\nprint \"os.system('setenforce 0')\"\n")
        f1.write("print \"os.system('sshpass -p \"+passw+\" ssh -X root@192.168.0.100 \"+soft+\"')\"")
       # f1.write(passw)
       # f1.write(" ssh -X root@192.168.0.100 ")
       # f1.write(soft)
       # f1.write("print \"')\"\n")
        f1.close()
        os.system("chmod 755 scripts/saas_"+soft+"_"+user+".py")
        os.system("chown -R root:root scripts/saas_"+soft+"_"+user+".py")
     print "Status: 303 See other"
     print "Location: http://192.168.0.100/cgi-bin/saasclient.py"
     print ""
  # else:
      # print "Status: 301 See other"
      # print "Location: http://192.168.0.100/cgi-bin/saasclient.py?stat='0'"
       #print ""
   else :
     print "Status: 303 See other"
     print "Location: http://192.168.0.100"
     print ""


saas_log()
