#! C:\Users\MOULERAJAN G\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n\r")

import cgi
import webbrowser

f=cgi.FieldStorage()
k1=f.getvalue('fname')
k2=f.getvalue('dob')
k3=f.getvalue('email')
k4=f.getvalue('pno')
k5=f.getvalue('uname')
k6=f.getvalue('password')


from mysql.connector import connect

db=connect(
        host='localhost',
        user='root',
        password='Gmoule@123',
        database='ssms'
    )
mycursor=db.cursor()
sql=("INSERT INTO ssms.signup (name,dob,email,pno,uname,pword) VALUES (%s,%s,%s,%s,%s,%s)")
data=(str(k1),str(k2),str(k3),str(k4),str(k5),str(k6))
mycursor.execute(sql,data)
db.commit()
mycursor.close()
db.close()

print(
'''
<div class="overlay">
<!-- LOGN IN FORM by Omar Dsoky -->
<link rel="stylesheet" href="./2.login_style.css">
<form action="3.welcome.py" method="post">
   <!--   con = Container  for items in the form-->
   <div class="con">
   <!--     Start  header Content  -->
   <header class="head-form">
      <h2>Log In</h2>
      <!--     A welcome message or an explanation of the login form -->
      <p>login here using your username and password</p>
   </header>
   <!--     End  header Content  -->
   <br>
   <div class="field-set">
     
      <!--   user name -->
         <span class="input-item">
           <i class="fa fa-user-circle"></i>
         </span>
        <!--   user name Input-->
         <input class="form-input" id="txt-input" name="uname1" type="text" placeholder="UserName" autocomplete='off' required>
     
      <br><br>
     
           <!--   Password -->
     
      <span class="input-item">
        <i class="fa fa-user-circle"></i>
       </span>
      <!--   Password Input-->
      <input class="form-input" type="password" placeholder="Password" id="txt-input"  name="pword1" required>
         
      <br><br>
<!--        buttons -->
<!--      button LogIn -->
      <button class="log-in"> Log In </button>
<br><br>
   </div>
   <form action="signup.html">
      <p>you don't have an account?</p>
   <button class="log-in">Sign Up </button>
</form>
  </div>
  
  <!-- End Form -->
</form>
</div>
''')

    
