import re
import paramiko
class connectingtohost:
    s=open(r"C:\Users\rahul\OneDrive\Desktop\testing\a1.txt","r")
    details={}
    for i in s.readlines():
        splits=i.split("=")
        details[splits[0]]=splits[1]
    print(details)
    def __init__(self):
        print("i am connecting to",self.details["hosttype"])
    def ipvalidation(self):
        print("validating the ip address")
        print(self.details["default_ip"])
        pattern="((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])[.]){3})([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])"
        res=re.fullmatch(pattern,self.details["default_ip"])
        if res==None:
            print("ipaddress is not avalid ip address")
            ipaddress=input("provide a valid ip adress")
            self.details["default_ip"]=ipaddress
            
        else:
            print(res,"is a valid ip address")
            obj1.connecting()
    def connecting(self):
      try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.details["default_ip"],username=self.details["username"],password=self.details["password"])
        print("ssh connection established")
      except Exception as error:
          print(error)
        
        
        

obj1=connectingtohost()
obj1.ipvalidation()