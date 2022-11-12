#! C:\Users\MOULERAJAN G\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n\r")

import cgi

f=cgi.FieldStorage()

k1=f.getvalue('a11')
k2=f.getvalue('a22')

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

	print('''
<!DOCTYPE html>
<html>
<head>
   <heading><center>Python Control Statement Quiz </center></heading>
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
		color:rgb(99, 97, 5);
		font-size:22px;
		font-weight:bold;
		}
	label{
		color:rgb(110, 6, 98);
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

    <form action="4.1.cs_result.py" method='post'>
		
    <label for="a1">1. Select which is true for for loop</label><br><br>
    <input type="radio" name="a1" value='1'/> Python's for loop used to iterates over the items of list, tuple, dictionary, <br>&emsp;  set, or string <br>
	<input type="radio" name="a1" value='2'/> else clause of for loop is executed when the loop terminates naturally <br>
	<input type="radio" name="a1" value='3'/> else clause of for loop is executed when the loop terminates abruptly <br>
	<input type="radio" name="a1" value='4'/> We use for loop when we want to perform a task indefinitely until a particular <br>&emsp;  condition is met <br><br>

    <label for="a2">2.What is the value of x after the following nested for loop completes its execution
<br>
       <br> &emsp;x = 0
        <br> &emsp;for i in range(10):
         <br> &emsp;&emsp;for j in range(-1, -10, -1):
          <br>  &emsp;&emsp;&emsp;x += 1
          <br>  &emsp;print(x)</label><br><br>
    <input type="radio" name="a2" value='1'/> 99 <br>
	<input type="radio" name="a2" value='2'/> 90 <br>
	<input type="radio" name="a2" value='3'/> 100 <br><br>

    <label for="a3">3.if -3 will evaluate to True</label><br><br>
	<input type="radio" name="a3" value='3'/> True <br>
	<input type="radio" name="a3" value='4'/> False <br><br>

    <label for="a4">4.What is the output of the following loop
<br>
       <br>&emsp; for l in 'Jhon':
         <br>&emsp;&emsp;  if l == 'o':
          <br>&emsp;&emsp; &emsp;   pass
         <br> &emsp;&emsp; print(l, end=", ")
        </label><br><br>
    <input type="radio" name="a4" value='1'/> j,h,n <br>
	<input type="radio" name="a4" value='2'/> j,h,o,n <br>
	<input type="radio" name="a4" value='3'/> Error <br>
	<input type="radio" name="a4" value='4'/> None <br><br>

    <label for="a5">5.What is the output of the following range() function
<br>
       <br>&emsp;&emsp; for num in range(2,-5,-1):
         <br>&emsp;&emsp;&emsp;   print(num, end=", ")</label><br><br>
    <input type="radio" name="a5" value='1'/> 2, 1, 0, -1, -2, -3, -4, -5 <br>
	<input type="radio" name="a5" value='2'/> 2, 1, 0 <br>
	<input type="radio" name="a5" value='4'/>  2, 1, 0, -1, -2, -3, -4 <br><br>

    <label for="a6">6. What is the value of x
<br>
      <br>&emsp;  x = 0
      <br>&emsp; while (x < 100):
         <br>&emsp;&emsp; x+=2
       <br>&emsp;&emsp; print(x)</label><br><br>
    <input type="radio" name="a6" value='1'/> 101 <br>
	<input type="radio" name="a6" value='2'/> 99 <br>
	<input type="radio" name="a6" value='3'/> 100 <br>
	<input type="radio" name="a6" value='4'/> None of the above <br><br>

    <label for="a7">7.What is the output of the following for loop and  range() function

       <br><br> &emsp;for num in range(-2,-5,-1):
         <br>  &emsp;&emsp; print(num, end=", ")</label><br><br>
    <input type="radio" name="a7" value='1'/> -2, -1, -3, -4<br>
	<input type="radio" name="a7" value='2'/> -2, -1, 0, 1, 2, 3,<br>
	<input type="radio" name="a7" value='3'/> -2, -1, 0 <br>
	<input type="radio" name="a7" value='4'/> -2, -3, -4, <br><br>

    <label for="a8">8.Why do we need loops in programming?</label><br><br>
    <input type="radio" name="a8" value='1'/> For iterations. <br>
	<input type="radio" name="a8" value='2'/> For traversals. <br>
	<input type="radio" name="a8" value='3'/> For avoiding repeated code. <br>
	<input type="radio" name="a8" value='4'/> All are correct. <br><br>

    <label for="a9">9.How do we differentiate the body of the loop from the rest of the code?</label><br><br>
    <input type="radio" name="a9" value='1'/> Writing loop above. <br>
	<input type="radio" name="a9" value='2'/> Writing loop below the whole code. <br>
	<input type="radio" name="a9" value='3'/> Using proper indentation. <br>
	<input type="radio" name="a9" value='4'/> All are correct. <br><br>

    <label for="a10">10.Which of the following is a loop in python?</label><br><br>
    <input type="radio" name="a10" value='1'/>  Do-while <br>
	<input type="radio" name="a10" value='2'/> If-else  <br>
	<input type="radio" name="a10" value='3'/>  Foreach <br>
	<input type="radio" name="a10" value='4'/> While <br><br>

    <label for="a11">11. Which of the following creates iterable elements?</label><br><br>
    <input type="radio" name="a11" value='1'/> If-else <br>
	<input type="radio" name="a11" value='2'/> Range <br>
	<input type="radio" name="a11" value='3'/> Count <br>
	<input type="radio" name="a11" value='4'/> None of these. <br><br>

    <label for="a12">12.Which of the following is used when we want to exit a loop?</label><br><br>
    <input type="radio" name="a12" value='1'/> Continue <br>
	<input type="radio" name="a12" value='2'/> Exit <br>
	<input type="radio" name="a12" value='3'/> Break <br>
	<input type="radio" name="a12" value='4'/> Pass <br><br>

    <label for="a13">13.Which type of loop iterates until instructed otherwise?</label><br><br>
    <input type="radio" name="a13" value='1'/> FOR loop<br>
	<input type="radio" name="a13" value='2'/> A count-controlled loop <br>
	<input type="radio" name="a13" value='3'/> Repeat-once loop <br>
	<input type="radio" name="a13" value='4'/> WHILE loop <br><br>

    <label for="a14">14.To repeat a fixed number of times use a</label><br><br>
    <input type="radio" name="a14" value='1'/> while loop<br>
	<input type="radio" name="a14" value='2'/> for loop <br>
	<input type="radio" name="a14" value='3'/> if loop <br>
	<input type="radio" name="a14" value='4'/> indentation <br><br>

    <label for="a15">15.To repeat until a particular condition is true use</label><br><br>
    <input type="radio" name="a15" value='1'/> while loop<br>
	<input type="radio" name="a15" value='2'/> for loop <br>
	<input type="radio" name="a15" value='3'/> if loop <br>
	<input type="radio" name="a15" value='4'/> indentation <br><br>

    <textarea hidden name="a21" id="quiz-time-left" ></textarea>
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
	print('nope again')