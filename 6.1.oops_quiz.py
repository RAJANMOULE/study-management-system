#! C:\Users\MOULERAJAN G\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n\r")

import cgi

f=cgi.FieldStorage()
k1=f.getvalue('a1')
k2=f.getvalue('a2')

try:
    from mysql.connector import connect

    db=connect(
        host='localhost',
        user='root',
        password='Gmoule@123',
        database='ssms'
    )
    mycursor=db.cursor()

    sql=("INSERT INTO ssms.time (time,concept) VALUES (%s,%s)")

    data=(str(k1),str(k2))
    mycursor.execute(sql,data)
    db.commit()
    mycursor.close()
    db.close()
    print('''
<!DOCTYPE html>
<html>
<head>
   <heading><center>Python oops Quiz </center></heading>
    <title>Quiz page</title>
   <style>
	.center{margin: auto;
  		  width: 60%;
  		  border: 3px solid black;
  		  padding: 10px;
		  background-color:sand;
		}
	body{ 
		background-image:url('iii.png');
	      	background-repeat:no-reapeat;
	      	background-attachment:fixed;
		background-size:cover;
		font-family: "Lucida Console", "Courier New", monospace;
	    }
	heading{
		color:Indigo;
		font-size:22px;
		font-weight:bold;
		}
	label{
		color:rgb(189, 28, 162);
		font-size:17px
    }
	p{
		color:aqua;
	}
	.time{
			text-align: right;
			font-size: 30px;
			font-weight: 200;
			color: rgb(53, 228, 30);
		}
</style>
</head>
<body>
	<div class="time" id="quiz-time"></div>

<div class='center'>

    <form action="6.2.oops_result.py" method='post'>
    <label for="a1">1.In Python, a class is ___________ for a concrete object.</label><br><br>
    <input type="radio" name="a1" value='1'/> a blueprint <br>
	<input type="radio" name="a1" value='2'/> a nuisance <br>
	<input type="radio" name="a1" value='3'/> an instance <br>
	<input type="radio" name="a1" value='4'/> a distraction <br><br>

    <label for="a2">2.The correct way to instantiate the above Dog class is:
      <br> &emsp;class Dog:
   <br> &emsp;&emsp;def __init__(self, name, age):
      <br> &emsp;&emsp;&emsp; self.name = name
      <br> &emsp;&emsp;&emsp; self.age = age
    </label><br><br>
    <input type="radio" name="a2" value='1'/> Dog("Rufus", 3) <br>
	<input type="radio" name="a2" value='2'/> Dog.create("Rufus", 3) <br>
	<input type="radio" name="a2" value='3'/> Dog() <br>
	<input type="radio" name="a2" value='4'/> Dog.__init__("Rufus", 3) <br><br>

    <label for="a3">3.In Python, a function within a class definition is called a:</label><br><br>
    <input type="radio" name="a3" value='1'/> a method <br>
	<input type="radio" name="a3" value='2'/> an operation<br>
	<input type="radio" name="a3" value='3'/> a class function <br>
	<input type="radio" name="a3" value='4'/> a callable <br><br>

    <label for="a4">4.To create an object ______ is used.</label><br><br>
    <input type="radio" name="a4" value='1'/> class <br>
	<input type="radio" name="a4" value='2'/> constructor <br>
	<input type="radio" name="a4" value='3'/> user-defined function <br>
	<input type="radio" name="a4" value='4'/> in-built functions <br><br>

    <label for="a5">5._____ represents an entity in the real world with its identity and 
	<br>&emsp;	behaviour.</label><br><br>
    <input type="radio" name="a5" value='1'/> an object <br>
	<input type="radio" name="a5" value='2'/> an operator <br>
	<input type="radio" name="a5" value='3'/> a method <br>
	<input type="radio" name="a5" value='4'/> a class <br><br>

    <label for="a6">6.Which of the following statements is true?</label><br><br>
    <input type="radio" name="a6" value='1'/> A class is blueprint for the object. <br>
	<input type="radio" name="a6" value='2'/> You can only make a single object from the given class. <br>
	<input type="radio" name="a6" value='3'/> Both statements are true. <br>
	<input type="radio" name="a6" value='4'/> Neither statement is true. <br><br>

    <label for="a7">7.What does the __init__() the function do in Python?</label><br><br>
    <input type="radio" name="a7" value='1'/> Initializes the class for use. <br>
	<input type="radio" name="a7" value='2'/> This function is called when a new object is instantiated. <br>
	<input type="radio" name="a7" value='3'/> Initializes all the data attributes to zero when called. <br>
	<input type="radio" name="a7" value='4'/> None of the above. <br><br>

    <label for="a8">8.Which of the following code uses the inheritance feature of Python?</label><br><br>
    <input type="radio" name="a8" value='1'/> class Foo: <br>&emsp;&emsp;&emsp; Pass <br>
	<input type="radio" name="a8" value='2'/> class Foo(object): <br>&emsp;&emsp;&emsp; pass <br>&emsp;   class Hoo(object): <br>&emsp;&emsp;&emsp; pass <br>
	<input type="radio" name="a8" value='3'/> class Foo: <br>&emsp;&emsp;&emsp; pass <br>&emsp;    class Hoo(Foo): <br>&emsp;&emsp;&emsp; pass <br>
	<input type="radio" name="a8" value='4'/> None of the above code. <br><br>

    <label for="a9">9.If you a class is derived from two different classes, it's called ______</label><br><br>
    <input type="radio" name="a9" value='1'/> Multilevel Inheritance <br>
	<input type="radio" name="a9" value='2'/> Multiple Inheritance <br>
	<input type="radio" name="a9" value='3'/> Hierarchical Inheritance  <br>
	<input type="radio" name="a9" value='4'/> Python Inheritance <br><br>

    <label for="a10">10.Which of the following statements is true?</label><br><br>
    <input type="radio" name="a10" value='1'/> In Python, same operator may behave differently depending upon operands. <br>
	<input type="radio" name="a10" value='2'/> You can change the way operators behave in Python. <br>
	<input type="radio" name="a10" value='3'/> Special method __add()__ is called when + operator is used. <br>
	<input type="radio" name="a10" value='4'/> All of the above. <br><br>

    <label for="a11">11.What is operator overloading in python?</label><br><br>
    <input type="radio" name="a11" value='1'/> A unique instance of a data structure that's defined by its class. <br>
	<input type="radio" name="a11" value='2'/> The operator is overloaded and explodes <br>
	<input type="radio" name="a11" value='3'/> The assignment of more than one function to a particular operator. <br>
	<input type="radio" name="a11" value='4'/> None of the answers <br><br>

    <label for="a12">12.What are the two main components of inheritance?</label><br><br>
    <input type="radio" name="a12" value='1'/> Any class <br>
	<input type="radio" name="a12" value='2'/> Parent class <br>
	<input type="radio" name="a12" value='3'/> Child class <br>
	<input type="radio" name="a12" value='4'/> None <br><br>

    <label for="a13">13.What is the depth of multilevel inheritance in Python?</label><br><br>
    <input type="radio" name="a13" value='1'/> Two-level<br>
	<input type="radio" name="a13" value='2'/> Three-level  <br>
	<input type="radio" name="a13" value='3'/> Any level of depth <br>
	<input type="radio" name="a13" value='4'/> None of these.  <br><br>

    <label for="a14">14.Which of the following is the super Class of all created classes in Python?</label><br><br>
    <input type="radio" name="a14" value='1'/> Super Class<br>
	<input type="radio" name="a14" value='2'/> Object identifier class <br>
	<input type="radio" name="a14" value='3'/> Craetor class <br>
	<input type="radio" name="a14" value='4'/> Object Class <br><br>

    <label for="a15">15.Which of the following is the base class for exceptions in Python?</label><br><br>
    <input type="radio" name="a15" value='1'/> Exception<br>
	<input type="radio" name="a15" value='2'/> BaseException <br>
	<input type="radio" name="a15" value='3'/> ExceptionClass <br>
	<input type="radio" name="a15" value='4'/> BaseExeptionClass <br><br>
   
   <textarea hidden name="a17" id="quiz-time-left" ></textarea>
<br>        <textarea hidden id="timeInSeconds" name='a16'>0</textarea>
    
   <center><input style='font-size:20px' type="submit" name="submit"/></center>
    </form>
</div>
<script>
	var total_seconds = 300 * 1;
	var c_minutes = parseInt(total_seconds / 60);
	var c_seconds = parseInt(total_seconds % 60);
	var timer;
	
	function CheckTime() {
	  document.getElementById("quiz-time").innerHTML = 'Time Left: ' + c_minutes + ' minutes ' + c_seconds + ' seconds ';
	  document.getElementById("quiz-time-left").innerHTML = 'hours=00'+' , '+'minutes='+c_minutes+' , '+'seconds='+ c_seconds;
	
	  if (total_seconds <= 0) {
		score();
	  } else {
		total_seconds = total_seconds - 1;
		c_minutes = parseInt(total_seconds / 60);
		c_seconds = parseInt(total_seconds % 60);
		timer = setTimeout(CheckTime, 1000);
	  }
	}
	timer = setTimeout(CheckTime, 1000);
	
	function score() {
	  // stop timer
	  clearInterval(timer);
	
	  //Referencing the value of the questions
	  var q1 = document.forms.form.q1.value;
	  var q2 = document.forms.form.q2.value;
	  var q3 = document.forms.form.q3.value;
	
	  // disable form
	  var elements = document.getElementById("questions").elements;
	  for (var i = 0, len = elements.length; i < len; ++i) {
		elements[i].disabled = true;
	  }
	
	  //Array for the questions
	  var questions = [q1, q2, q3];
	
	  //Answers for each question
	  var answers = ["b", "b", "b"];
	
	  //variable to keep track of the points
	  var points = 0;
	  var total = 3;
	  //max score 
	
	  //Making use of a for loop to iterate over the questions and answers arrays
	  for (var i = 0; i < total; i++) {
		if (questions[i] == answers[i]) {
		  points = points + 1; //Increment the score by 2 for every correct answer given
		}
	  }
	
	  //CSS for questions
	  var q = document.getElementById("p");
	
	  q.innerHTML = (29 - Math.floor(total_seconds)) ;
	
	  return false;
	}
	</script>
<div>
    <html lang="en"><head>
        <link rel="canonical" href="https://jasonzissman.github.io//time-me-demo/" />
        <script type="application/ld+json">
        {"@context":"https://schema.org","@type":"WebPage","description":"An exploration of building and maintaining a successful software development organization.","headline":"Time Me Demo","url":"https://jasonzissman.github.io//time-me-demo/"}</script>
        
        <link rel="stylesheet" href="/assets/main.css"><link type="application/atom+xml" rel="alternate" href="https://jasonzissman.github.io//feed.xml" title="Jason Zissman" /></head>
        <body>
        <main class="page-content" aria-label="Content">
              <div class="wrapper">
                <article class="post">
        
          <div class="post-content">
            <div class="top-level-message">
        
        </div>
        
        
        <link rel="stylesheet" type="text/css" href="style1.css" />
        
        <script src="timeme.min.js"></script>
        
        <script type="text/javascript">
            TimeMe.initialize({
                currentPageName: "my-home-page", // current page
                idleTimeoutInSeconds: 50, // stop recording time due to inactivity
                
            });
        
            TimeMe.callAfterTimeElapsedInSeconds(4, function(){
                console.log("The user has been using the page for 4 seconds! Let's prompt them with something.");
            });
        
            TimeMe.callAfterTimeElapsedInSeconds(9, function(){
                console.log("The user has been using the page for 9 seconds! Let's prompt them with something.");
            });
        
        
            window.onload = function(){
                TimeMe.trackTimeOnElement('area-of-interest-1');
                TimeMe.trackTimeOnElement('area-of-interest-2');
                setInterval(function(){
                    var timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
                    document.getElementById('timeInSeconds').textContent = timeSpentOnPage.toFixed(2);
        
                    var timeSpentOnElement = TimeMe.getTimeOnElementInSeconds('area-of-interest-1');
                    document.getElementById('area-of-interest-time-1').textContent = timeSpentOnElement.toFixed(2);
        
                    var timeSpentOnElement = TimeMe.getTimeOnElementInSeconds('area-of-interest-2');
                    document.getElementById('area-of-interest-time-2').textContent = timeSpentOnElement.toFixed(2);
                }, 25);
            }
        </script>
        
        
          </div>
        
        </article>
        
              </div>
            </main><footer class="site-footer h-card">
          <data class="u-url" href="/"></data>
        
          <div class="wrapper">
        
        
            <div class="footer-col-wrapper">
              <div class="footer-col footer-col-1">
                <ul class="contact-list">
              </div>
        
              </div>
        
              
            </div>
        
          </div>
        
        </footer>
        </body>
        
        
</div>

</body>
</html>''')
except:
	print('wrong')