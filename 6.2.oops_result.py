#! C:\Users\MOULERAJAN G\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n\r")

import cgi

f=cgi.FieldStorage()

k=[]

k1=f.getvalue('a1')
k2=f.getvalue('a2')
k3=f.getvalue('a3')
k4=f.getvalue('a4')
k5=f.getvalue('a5')
k6=f.getvalue('a6')
k7=f.getvalue('a7')
k8=f.getvalue('a8')
k9=f.getvalue('a9')
k10=f.getvalue('a10')
k11=f.getvalue('a11')
k12=f.getvalue('a12')
k13=f.getvalue('a13')
k14=f.getvalue('a14')
k15=f.getvalue('a15')
k16=f.getvalue('a16')
if k1=='1':
    k.append(1)

if k2=='1':
    k.append(1)

if k3=='1':
    k.append(1)

if k4=='1':
    k.append(1)

if k5=='1':
    k.append(1)

if k6=='1':
    k.append(1)

if k7=='2':
    k.append(1)

if k8=='3':
    k.append(1)

if k9=='3':
    k.append(1)

if k10=='3':
    k.append(1)

if k11=='3':
    k.append(1)

if k12=='1':
    k.append(1)

if k13=='3':
    k.append(1)

if k14=='1':
    k.append(1)

if k15=='1':
    k.append(1)

l=sum(k)
x=[]
y=[]

from mysql.connector import connect

db=connect(
            host='localhost',
            user='root',
            password='Gmoule@123',
            database='ssms'
        )
mycursor=db.cursor()

sql=("SELECT time,concept FROM ssms.time")

mycursor.execute(sql)
data=mycursor.fetchall()
for i,j in data:
    x.append(i)
    y.append(j)


total_time=str(x[-1])
concept=str(y[-1])

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("gmoulerajan@gmail.com", "yzddqrsuotakchow")

# message to be sent
message = f'''Hi. we are from Abc learning academy. Your son studying python developer course in our academy. Well, your son takes {total_time} seconds study the {concept}. Then he takes {k16} time to take quiz test and he got {l} marks out of 20. thank you '''

# sending the mail
s.sendmail("gmoulerajan@gmail.com", "janarithish@gmail.com", message)

# terminating the session
    
#s.quit()

print('''
<html>
<head>
<style>
.center {
  background-image: linear-gradient(-225deg,#E3FDF5 50%, #FFE6FA 40%);  position: relative;
  top:120px;
  z-index: 1;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  color:blue;
  box-shadow: 0 0 20px 0 rgba(55, 55, 55, 0.2), 0 5px 5px 0 rgba(55, 55, 55, 0.24);
  }
body {
    background-image: linear-gradient(-225deg, #E3FDF5 0%, #FFE6FA 100%);
background-image: linear-gradient(to top, #e757b0 0%, #4758b8 100%);
background-attachment: fixed;
  background-repeat: no-repeat;

    font-family: 'Vibur', cursive;
/*   the main font */
    font-family: 'Abel', sans-serif;
opacity: .95;
/* background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%); */
}
</style>
</head>
<body>
<div class='center' style='background-color:pink'>
<h2><center>
Quiz concept :      oops <br><br>

Total Question :  15 <br><br>
''')
print(f'''
Correct Answer :  {l} <br><br>

Score :           {l}/15

<br>
<br>
<br>
<a href='1.signup.html'>Signup</a> &emsp;&emsp;&emsp; <a href='7.logout.html'>Logout</a>
</center>
</h2>
</div>
</body>
</html>''')

