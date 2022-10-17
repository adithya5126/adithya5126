import re
import paramiko
import datetime
import sys
a=[r"C:\Users\rahul\OneDrive\Desktop\testing\a1.txt",r"C:\Users\rahul\OneDrive\Desktop\testing\b1.txt"]
for i in a:
 with open(i,"r") as e:
    k=e.readlines()
    d1={}
    for i in k:
      spliting=i.split("=")
      d1[spliting[0]]=spliting[-1]
   # print(d1)
    print(d1["hosttype"])
    if "filer-cmode" in d1["hosttype"]:
        print("i am processing the filermode")
        pattern="((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])[.]){3})([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])"
        res=re.match(pattern,d1["default_ip"])
        if res==None:
            print("the given ip address is not valid")
           # n=input("enter the correct ip adress=")
            #d1["default_ip"]=n
            i
        else:
           print("ip adress is valid only")
           try:
               ssh=paramiko.SSHClient()
               ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
               print("trying to connect to host")
               ssh.connect(hostname=d1["default_ip"],username=d1["username"],password=d1["password"])
               print("connected to host",datetime.datetime.now().time())
               k=""
               for j in d1["owner"]:
                   if i!="@":
                       k=k+i
                   else:
                       print("the owner this host is",k)
                       break

                       
           except Exception as error:
                print(error)
                print("connection failed=",datetime.datetime.now().time())
                k=""
                for j in d1["owner"]:
                    if j!="@":
                        k=k+j
                    else:
                        print("the owner this host =",k)
                        #sys.exit()
                
                        
    elif "rhel-8.5" in d1["hosttype"]:
         print("i am processing the rhel-8.5")
         pattern="((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])[.]){3})[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5]"
         res=re.match(pattern,d1["default_ip"])
         if res==None:
             print("the given ip address is not valid")
         else:
            print("ip adress is valid only")
            try:
                ssh=paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print("trying to connect to host")
                ssh.connect(hostname=d1["default_ip"],username=d1["username"],password=d1["password"])
                print("connected to host",datetime.datetime.now().time())
                k=""
                for j in d1["owner"]:
                    if i!="@":
                        k=k+i
                    else:
                        print("the owner this host is",k)
                        sys.exit()

                        
            except Exception as error:
                 print(error)
                 print("connection failed=",datetime.datetime.now().time())
                 k=""
                 for j in d1["owner"]:
                     if j!="@":
                         k=k+j
                     else:
                         print("the owner this host =",k)
                     sys.exit()