#! C:\Users\MOULERAJAN G\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n\r")

import cgi

n=cgi.FieldStorage()

k1=n.getvalue('uname1')
k2=n.getvalue('pword1')

data1=[]
data2=[]

from mysql.connector import connect
db=connect(
            host='localhost',
            user='root',
            password='Gmoule@123',
            database='ssms'
    )
mycursor=db.cursor()
sql=("SELECT uname,pword FROM ssms.signup")

mycursor.execute(sql)
data=mycursor.fetchall()
db.commit()
for m,n in data:
    data1.append(m)
    data2.append(n)
mycursor.close()
db.close()

if k1 in data1 and k2 in data2:
    print(
        '''
        <!DOCTYPE html>
<html>

    <link rel="stylesheet" href="./3.welcome_style.css">
    <link rel="stylesheet" href="./2.png">

<head>
    <title>abc Learning Academy</title>
</head>
<body style="background-image:url('./2.png'); background-repeat: no-repeat; background-attachment: fixed; background-size: cover;">    
<center>
    <div class="center">
    <h1>ABC Learning Academy</h1>
    <h2> welcome to python developer course </h2>
    <div class="abc">  
    <h3>Select the topic here</h3>
    <ol class="pad">
        <a href="5.datatypes.html"> Data types</a><br><br>
        <a href="4.control_statements.html">Control statements</a><br><br>
        <a href="6.oops.html">Oops concept</a>
    </ol>
</div>
</div>
</center>
</body>
</html>
        ''')
