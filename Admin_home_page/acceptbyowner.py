#!C:\Users\chand\AppData\Local\Programs\Python\Python310/python.exe

print("content-type:text/html\r\n")
import cgi
import pymysql
form=cgi.FieldStorage()
oid=form.getvalue('q')
oemail=form.getvalue('sid')

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="sugumar",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        updatequery="update tbl_register set status='%s' where userid=%d  and email_id='%s' "%('Accept',int(oid),oemail)
        res=cursor.execute(updatequery)
        if(res==1):
            dbcon.commit()
##            squery="select username,usertype from tbl_register where userid=%d and email_id='%s' "%(int(oid),oemail)
##            cursor.execute(squery)
##            result=cursor.fetchone()
##            sname=result[0]
##            stype=result[1]
            print("<script>alert('Updated success');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
        else:
            dbcon.rollback()
            print("<script>alert('Error in Updation');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
    else:
        print("<script>alert('Error in Updation');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
except Exception as e:
    print(e)
              
    
            
                                                                                                                                                                                                                                                                             
