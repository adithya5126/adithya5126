import re
import paramiko
import datetime
import sys
a=[r"C:\Users\rahul\OneDrive\Desktop\testing\a1.txt",r"C:\Users\rahul\OneDrive\Desktop\testing\b1.txt",r"C:\Users\rahul\OneDrive\Desktop\testing\c1.txt"]
for j in a:   
    print(j)

    class connectingtohost:
        s=open(j,"r")
        details={}
        for i in s.readlines():
            splits=i.split("=")
            details[splits[0]]=splits[1].strip("\n")
        s.close()
        
        
        def __init__(self):
            print("\n")
            hostname=self.details["hosttype"].split("-")
            print("i am connecting to",hostname[0])
            print("_____________________________")
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
                selection=input("enter yes want to connect remote server =")
                if selection=="yes" or selection=="YES" or selection=="y":
                    obj1.connecting()#connecting to ssh
                else:
                    obj1.p()
        def p(self):#connect to server without password
          try:
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("trying to connect...")
            ssh.connect(hostname=self.details["default_ip"],username=self.details["username"],key_filename=self.details["key_filename"])
            print("conneted to remote server successfully",datetime.datetime.now().time())
            commands=input("do you want excute a command on connected server=")
            while True:
                if commands=="yes":
                    stdin,stdout,stderr=ssh.exec_command(input("enter your command:"))
                    print(stdout.readlines())
                    ssh.close()
                elif commands=="quit":
                    sys.exit()
            obj1.owner()
          except Exception as error:
             print("#######")
             print(error)
             obj1.owner()
           
                
        def connecting(self):#connecting to ssh
          try:
            print("Trying to connect a remote server...")
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.details["default_ip"].strip("\n"),username=self.details["username"].strip("\n"),password=self.details["password"].strip("\n"))
            print("ssh connection established",datetime.datetime.now().time())
            obj1.owner()
            
          except Exception as error:
              print("##########")
              print("connection failed due to",error)
              print("\n")
              print("connetion failed at",datetime.datetime.now().time())
              obj1.owner()
             
            
        def owner(self):
          # print(self.details["owner"])
          k=self.details["owner"].split("@")
          print("owner of this host is=",k[0])
          print("------------------------------------")
          
    
    obj1=connectingtohost()
    obj1.ipvalidation()