#!/usr/bin/python
import os
import cgi
import cgitb
import thread
import MySQLdb
cgitb.enable()
form=cgi.FieldStorage()
def create_obj() :
   
   os.system("iptables -F")
   os.system("setenforce 0")
   flav=form.getvalue('obj')
   if flav == 'flavour1' :
      size='1'
   elif flav == 'flavour2' :
      size='2'
   else :
      size='5'
   user=os.environ.get("HTTP_COOKIE")
   os.system("lvcreate --size "+size+"G --name "+user+" staas_vg")
   os.system("mkfs.ext4 /dev/staas_vg/"+user)
   os.system("mkdir -p /staas/"+user)
   os.system("mount /dev/staas_vg/"+user+" /staas/"+user)
   f1=open("/etc/exports","a+")
   f1.write("/staas/"+user+"  *(rw,no_root_squash)\n")
   f1.close()
   os.system("service nfs restart")
   f2=open("/var/www/cgi-bin/scripts/mountobj_"+user+".py","a+")
   f2.write("#!/usr/bin/python\nimport os\n\import cgi\nimport cgitb\ncgitb.enable()\nprint 'Content-type: application/download'\nprint ''\n\n")
   f2.write("print '#!/usr/bin/python\nimport os'\n")
   f2.write("user = '%s'\n" % (user))
   f2.write("print \"os.system('iptables -F')\"\nprint \"os.system('setenforce 0')\"\nprint \"os.system('mkdir /media/\"+user+\"')\"\n")
   f2.write("print \"os.system('mount 192.168.0.100:/staas/\"+user+\" /media/\"+user+\"')\"\n")
   f2.close()
   os.system("chmod 555 /var/www/cgi-bin/scripts/mountobj_"+user+".py")
   db=MySQLdb.connect("192.168.0.100","clouduser","maestro","cloud")
   cursor=db.cursor()
   cursor.execute("update cloudsignup set statusobj=\"1\" where email='%s'" % (user))
   print "Status: 303 See other"
   print "Location: http://192.168.0.100/cgi-bin/objmount.py"
   print ""

create_obj()
   
