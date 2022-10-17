import re
import paramiko
import datetime
import sys
a=[r"C:\Users\rahul\OneDrive\Desktop\testing\a1.txt",r"C:\Users\rahul\OneDrive\Desktop\testing\b1.txt"]
for j in a:   
    class connectingtohost:
        s=open(j,"r")
        details={}
        for i in s.readlines():
            splits=i.split("=")
            details[splits[0]]=splits[1].strip("\n")
        s.close()
        #print(details)
        def __init__(self):
            print("\n")
            hostname=self.details["hosttype"].split("-")
            print("i am connecting to",hostname[0])
        def ipvalidation(self):#ip validation
            print("validating the ip address")
            print("##############################")
            #print(self.details["default_ip"])
            pattern="((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])[.]){3})([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])"
            res=re.fullmatch(pattern,self.details["default_ip"])
            if res==None:
                print("ipaddress is not avalid ip address")
                ipaddress=input("provide a valid ip address=")#asking the user to provide correct ip address
                
                self.details["default_ip"]=ipaddress
                obj1.ipvalidation()#checking the ip validation again 
                #print(self.details)
                
            else:
                print(res.group(0),"is a valid ip address")
                obj1.connecting()#connecting to ssh
        def connecting(self):#connecting to ssh
          try:
            print("Trying to connect a remote server...")
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.details["default_ip"].strip("\n"),username=self.details["username"].strip("\n"),password=self.details["password"].strip("\n"))
            print("ssh connection established",datetime.datetime.now().time())
            ssh.close()
          except Exception as error:
              print("##########")
              print("connection failed due to",error)
              print("\n")
              print("connetion failed at",datetime.datetime.now().time())
              obj1.owner()#provide the owner name of the host
            
        def owner(self):
          # print(self.details["owner"])
          k=self.details["owner"].split("@")
          print("owner of this host is=",k[0])
          print("------------------------------------")
          if "b1.txt" in j:
              sys.exit()
    
    obj1=connectingtohost()
    obj1.ipvalidation()