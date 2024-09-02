#!C:\Users\chand\AppData\Local\Programs\Python\Python310/python.exe

print("content-type:text/html\r\n")
import cgi
import os,random
remoteurl=random.choice(os.listdir("DecoyFiles/"))
print(remoteurl)

