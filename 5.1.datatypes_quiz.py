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
	<style>
		.center{margin: auto;
				width: 60%;
				border: 3px solid black;
				top: 220px;
				padding: 10px;
			  background-color:sand;
			font-family: "Lucida Console", "Courier New", monospace;
			}
		body{ 
			background-image:url('iii.png');
				  background-repeat:no-reapeat;
				  background-attachment:fixed;
			background-size:cover;
			}
		heading{
			color:rgb(99, 97, 5);
			font-size:25px;
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
   <heading><center>Python datatypes Quiz </center></heading>
    <title>Quiz page</title>
   
</head>
<body>
	
	<div class="time" id="quiz-time"></div>
	
	<div class='center'>

    <form action="5.2.datatypes_result.py" method='post'>
    <label for="a1">1.Which Data Type represents a whole number?</label><br><br>
    <input type="radio" name="a1" value='1'/> string <br>
	<input type="radio" name="a1" value='2'/> integer <br>
	<input type="radio" name="a1" value='3'/> float <br>
	<input type="radio" name="a1" value='4'/> boolean <br><br>
	
	<label for="a2">2. What is the data type of print(type(10))</label><br><br>
    <input type="radio" name="a2" value='1'/> float<br>
	<input type="radio" name="a2" value='2'/> integer<br>
	<input type="radio" name="a2" value='3'/> int <br>
	<input type="radio" name="a2" value='4'/> double<br><br>
	
	<label for="a3">3.This particular Data Type has 2 potential values (typically True or False).</label><br><br>
    <input type="radio" name="a3" value='1'/> string<br>
	<input type="radio" name="a3" value='2'/> integer <br>
	<input type="radio" name="a3" value='3'/> boolen <br>
	<input type="radio" name="a3" value='4'/> float <br><br>

	<label for="a4">4.A price such as £3.65 should be saved as what kind of variable?</label><br><br>
    <input type="radio" name="a4" value='1'/> string <br>
	<input type="radio" name="a4" value='2'/> integer <br>
	<input type="radio" name="a4" value='3'/> boolean <br>
	<input type="radio" name="a4" value='4'/> float <br><br>
	
	<label for="a5">5.Which Data Type would the following be stored as:--- " Biscuit "</label><br><br>
    <input type="radio" name="a5" value='1'/> float <br>
	<input type="radio" name="a5" value='2'/> int <br>
	<input type="radio" name="a5" value='3'/> str <br>
	<input type="radio" name="a5" value='4'/> boolean <br><br>
	
	<label for="a6">6. Which of the following is an integer?</label><br><br>        
    <input type="radio" name="a6" value='1'/> 0.2 <br>
	<input type="radio" name="a6" value='2'/> 2 <br>
	<input type="radio" name="a6" value='3'/> .2 <br>
	<input type="radio" name="a6" value='4'/> pi <br><br>

	<label for="a7">7. What is the type of the following variable x = -5j</label><br><br>
    <input type="radio" name="a7" value='1'/> int <br>
	<input type="radio" name="a7" value='2'/> complex <br>
	<input type="radio" name="a7" value='3'/> real <br>
	<input type="radio" name="a7" value='4'/> imaginary <br><br>
	
	<label for="a8">8. Which of the following is an example of a list of numbers?</label><br><br>
    <input type="radio" name="a8" value='1'/> y=[1,2,3]<br>
	<input type="radio" name="a8" value='2'/> y='1,2,3'<br>
	<input type="radio" name="a8" value='3'/> y=(1,2,3) <br>
	<input type="radio" name="a8" value='4'/> y={1,2,3}<br><br>
	
	<label for="a9">9. Select all the correct options to copy a list aList = ['a', 'b', 'c', 'd']</label><br><br>
    <input type="radio" name="a9" value='1'/>  newList = copy(aList) <br>
	<input type="radio" name="a9" value='2'/>  newList = aList.copy() <br>
	<input type="radio" name="a9" value='3'/>  newList.copy(aList) <br>
	<input type="radio" name="a9" value='4'/>  newList = list(aList) <br><br>
	
	<label for="a10">10. list is mutable</label><br><br>
    <input type="radio" name="a10" value='1'/> True <br>
	<input type="radio" name="a10" value='2'/> False <br><br>

    <label for="a11">11.Python allows you to be able to use Dictionaries to store values using <br>&emsp; keys?</label><br><br>
    <input type="radio" name="a11" value='1'/> True<br>
    <input type="radio" name="a11" value='2'/> False<br><br>

    <label for="a12">12.Which Python statement will see if a is greater than b? </label><br><br>
    <input type="radio" name="a12" value='1'/> if a>b:<br>
	<input type="radio" name="a12" value='2'/> if(a>b)<br>
	<input type="radio" name="a12" value='3'/> is a is greater than b <br>
	<input type="radio" name="a12" value='4'/> if a!=b:<br><br>

    <label for="a13">13.Which of the following function convert a string to a float in python?</label><br><br>
    <input type="radio" name="a13" value='1'/> int(x [,base])<br>
	<input type="radio" name="a13" value='2'/> long(x [,base] )<br>
	<input type="radio" name="a13" value='3'/> float(x) <br>
	<input type="radio" name="a13" value='4'/> string(x)<br><br>

    <label for="a14">14. x="ABC learning Academy"<br>&emsp;&emsp;print(x[2:7])</label><br><br>
    <input type="radio" name="a14" value='1'/> C learnin<br>
	<input type="radio" name="a14" value='2'/> ABC lear<br>
	<input type="radio" name="a14" value='3'/> C lea<br>
	<input type="radio" name="a14" value='4'/> BC lear<br><br>

    <label for="a15">15.tuple1=(1,2,3,4) <br>&emsp;&emsp;x=tuple1.add(5) <br>&emsp;&emsp;print(tuple1) </label><br><br>
    <input type="radio" name="a15" value='1'/> Error<br>
	<input type="radio" name="a15" value='2'/> (1,2,3,4)<br>
	<input type="radio" name="a15" value='3'/> None <br>
	<input type="radio" name="a15" value='4'/> (1,2,3,4,5)<br><br>

    <label for="a16">16.n1={1,2,3,4} <br>&emsp;&emsp;n2={6,7,1,2} <br>&emsp;&emsp;print(n1.^(n2))</label><br><br>
    <input type="radio" name="a16" value='1'/> {6,4,3,2,1,7}<br>
	<input type="radio" name="a16" value='2'/> None<br>
	<input type="radio" name="a16" value='3'/> {4,3} <br>
	<input type="radio" name="a16" value='4'/> {6,7,4,3}<br><br>

    <label for="a17">17.list1=[1,2,3,4] <br>&emsp;&emsp;print(list1.pop())</label><br><br>
    <input type="radio" name="a17" value='1'/> None<br>
	<input type="radio" name="a17" value='2'/> [1,2,3]<br>
	<input type="radio" name="a17" value='3'/> []<br>
	<input type="radio" name="a17" value='4'/> [1,2,3,4]<br><br>
        
    <label for="a18">18. str1="hello" <br>&emsp;&emsp;print(str1.capitalize())</label><br><br>
    <input type="radio" name="a18" value='1'/> HELLO<br>
	<input type="radio" name="a18" value='2'/> hello<br>
	<input type="radio" name="a18" value='3'/> Hello<br><br>

    <label for="a19">19.What is a correct syntax to return the first character in a string?</label><br><br>
	<input type="radio" name="a19" value='1'/> x="hello".sub(0,1)<br>
	<input type="radio" name="a19" value='2'/> x=sub("hello",0,1)<br>
	<input type="radio" name="a19" value='3'/> x="hello"[0]<br><br>
        
    <label for="a20">20.Which method can be used to remove any whitespace from both the beginning<br>&emsp; and the end of a string?</label><br><br>
    <input type="radio" name="a20" value='1'/> len()<br>
	<input type="radio" name="a20" value='2'/> partition()<br>
	<input type="radio" name="a20" value='3'/> split() <br>
	<input type="radio" name="a20" value='4'/> strip()<br><br>

	<textarea hidden name="a21" id="quiz-time-left" ></textarea>
<br>        <textarea hidden id="timeInSeconds" name='a22'>0</textarea>
           

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
</html>

          ''')
    
except:
    print("nope")
