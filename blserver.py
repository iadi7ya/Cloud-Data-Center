#!/usr/bin/python
import os
import commands
import cgi
import cgitb
import MySQLdb
cgitb.enable()
form=cgi.FieldStorage()
def create_bl() :
   os.system("iptables -F")
   os.system("setenforce 0")
   flav=form.getvalue('block')
   if flav == 'flavour1' :
      size="3"
   elif flav == 'flavour2' :
      size="5"
   else :
      size="8"
   count=1
   user=os.environ.get('HTTP_COOKIE')
  # os.system("lvcreate --size "+size+"G --name "+user+" staas_blockvg")
  # for item in os.listdir("/dev/staas_blockvg"):
    #   count=count+1
   tid=str(count)
   os.system("sudo tgtadm --lld iscsi --mode target --op new --tid 1  --targetname "+user)
   os.system("sudo tgtadm --lld iscsi --op bind --mode target --tid 1 -I ALL")
   os.system("sudo tgtadm --lld iscsi --mode logicalunit --op new --tid 1 --lun 1  --backing-store /dev/sda6")
   os.system("sudo tgt-admin --dump 2>"+user+".txt")
   f4=open("/etc/tgt/targets.conf","a+")
   (a,b)=commands.getstatusoutput("cat "+user+".txt")
   f4.write(b)
   f4.close()
   os.system("service tgtd restart")
   os.system("rm -f "+user+".txt")
   f2=open("scripts/bl_connect_"+user+".py","a+")
   f2.write("#!/usr/bin/python\nimport os\nimport cgi\nimport cgitb\ncgitb.enable()\nprint 'Content-type: application/download'\nprint ''\n\n")
   f2.write("print '#!/usr/bin/python'\nprint 'import os'\nprint 'import cgi'\nprint 'import cgitb'\nprint 'cgitb.enable()'\n")
   f2.write("user= '%s'\n" % (user))
   f2.write("print \"os.system('iptables -F')\"\nprint \"os.system('setenforce 0')\"\nprint \"os.system('service iscsi restart')\"\n")
   f2.write("print \"os.system('iscsiadm --mode discoverydb --types sendtargets --portal 192.168.0.29 --discover')\"\n")
   f2.write("print \"os.system('iscsiadm --mode node --targetname \"+user+\" --portal 192.168.0.100:3260 --login')\"")
   f2.close()
   os.system("chmod 555 /var/www/cgi-bin/scripts/bl_connect_"+user+".py")
   f3=open("/var/www/cgi-bin/scripts/bl_logout_"+user+".py","a+")
   f3.write("#!/usr/bin/python\nimport os\nimport cgi\nimport cgitb\ncgitb.enable()\nprint 'Content-type: application/download'\nprint ''\n\n")
   f3.write("print '#!/usr/bin/python'\nprint 'import os'\nprint 'import cgi'\nprint 'import cgitb'\nprint 'cgitb.enable()'\nprint ''\n\n")
   f3.write("user = '%s'" % (user))
   f3.write("print \"os.system('iptables -F')\"\nprint \"os.system('setenforce 0')\"\n\n")
   f3.write("print  \"os.system('iscsiadm --mode node --targetname \"+user+\" --portal 192.168.0.100:3260 --logout')\"")
   f3.close()
   os.system("chmod 555 /var/www/cgi-bin/scripts/bl_logout_"+user+".py")
   db=MySQLdb.connect("192.168.0.100","clouduser","maestro","cloud")
   cursor=db.cursor()
   cursor.execute("update cloudsignup set statusbl='1' where email= '%s'" % (user)) 
   print "Status: 303 See other"
   print "Location: http://192.168.0.100/cgi-bin/blclient.py"
   print ""
create_bl()

