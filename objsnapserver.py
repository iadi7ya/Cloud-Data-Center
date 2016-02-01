#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
os.system("iptables -F")
os.system("setenforce 0")
def snap() :
   user=os.environ.get("HTTP_COOKIE")
   if user:
     flag=0
     for item in os.listdir("/var/www/cgi-bin/scripts") :
        if item == "mountobjsnap_"+user+".py" :
          flag=1
          break

   name=form.getvalue('snap')
   os.system("lvcreate --size +1G  --name "+name+"/dev/staas_vg/"+user)
   os.system("mkfs.ext4 /dev/staas_vg/"+user)
   os.system("mkdir -p /staas/"+user+"_"+name)
   os.system("mount /dev/staas_vg/"+name+" /staas/"+user+"_"+name)
   f1=open("/etc/exports","a+")
   f1.write("/staas/"+user+"_"+name+"  *(rw,no_root_squash)\n")
   f1.close()
   os.system("service nfs restart")
   if flag==0:
     f2=open("/var/www/cgi-bin/scripts/mountobjsnap_"+user+".py","a+")
     f2.write("#!/usr/bin/python\nimport os\n\import cgi\nimport cgitb\ncgitb.enable()\nprint 'Content-type: application/download'\nprint ''\n\n")
     f2.write("print '#!/usr/bin/python\nimport os'\n")
     f2.write("user = '%s'\n" % (user))
     f2.write("name = '%s'\n" % (name))
     f2.write("print \"os.system('iptables -F')\"\nprint \"os.system('setenforce 0')\"\nprint \"os.system('mkdir /media/\"+user+\"/\"+name+\"')\"\n")
     f2.write("print \"os.system('mount 192.168.0.100:/staas/\"+user+\"/\"+name+\" /media/\"+user+\"/\"+name+\"')\"\n")
     f2.close()

     os.system("chmod 555 /var/www/cgi-bin/scripts/mountobjsnap_"+user+".py")
   print "Status: 303 See other"
   print "Location: http://192.168.0.100/cgi-bin/objsnapmount.py"
   print ""
snap()

