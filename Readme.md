## Problem Statement: 
# Develop a program which will Randomly select the questions from database.


**1. @Salman8520 - *Salmanansari9869@gmail.com***
- Created database in sqlite3 in python coz it will be almost same as postgre(just connecting method will be different)
- Created table with question_id,question,option_1,option_2,answer.
- Created solution by using list data type(for ease of work) and one of the team member **@Manjeet12102000** share the part of solution by which we can pull rows randomly from table in database, and also search for if any other different logic available.
- There was very slight chance of rows to be repeated, so for that I extended code to avoid that, whose logic will be based of id of each question.Thus remove the worry of repeatation of questions
- Made the code more flexible so that can be use in many different places without changes
- Tested and analyzed the code using different test cases


**2. @jhasurajj - *jhasuraj0501@gmail.com***
- At the starting obtained the knowledge of python, postgresql,  then started learning basic of each then create a database by using python module sqlite3 called "question.db" which consist a table "result" which have 4 columns("question","option 1", "option 2","ans").
- Then using different SQL command insert the values of the column after display the table value which is persent in the database.
- Then wrote the logic to print random question from database without repetation of any question.

**3. @Manjeet12102000 - *manjeetg701@gmail.com***
- did some  research on  how we can connect the database from backend and how to display random question from database . 
- Created database in postgres sql for questions, options and ans. 
- Connected database to the  backend. 
- created query to print the random question from database . 
- discussed with the whole group about our program and checked the all the test cases whether the question repeating or not.

**4. @mansi0204 - *mansiinchanalkar12@gmail.com***
- Installed postgreSQL on my system. 
- Created table named as question in database test by using postgreSQL.
- Developed a Python program  which randomly select and display questions from database with the help of  random () function. 
- Created 7 columns (Question No., Question, Option1, Option 2 , Option3, Option4, Answer) in Question table. Then with the help of for loop I have displayed fixed number of questions. I have used fetchall function to fetch query result from database.


**5. @VrunaliPanchal - *vrunalipanchal89692@gmail.com***
- Created a ER diagram of question and answer table  
- created a Sequence diagram for better understanding of our problem statement .
- Created database of question and answer table. In this create a random 20 questions and their answers columns. In question table create a four columns (id, questions, correct answer and status ) In status column (YES/NO) Shows whether the question asked previously or not.
- NO status indicates  question is not repeated . 
- YES status indicates question is repeated.  
- Database connection from python to database

**6. @Navina Pandhare - *navinapandhare016@gmail.com***
- First researched about the problem statement and ways through which the Problem Statement can be solved. 
- Created a Database containing question & answer table and python program to randomly select questions from the database and display them.

**7. @Rkrock30 - *guptaranjeet451@gmail.com***
- first  I discussed the topic  with my group members for  better understanding of our problem statement .
- Created database of question and answer table. For this problem i created a random 10 questions and their answers columns.
- In question table I created a four columns (id, questions, correct answer and status ) In status column (YES/NO) Shows whether the question asked previously or not.
- NO status indicates  question is not repeated . 
- YES status indicates question is repeated.
- Database connection from python to database.

**8. @vishalrathee01 - *Vishalrathee0123@gmail.com***
- First obtain the knowledge about python, postgresql and nodejs.
- Then learnt the basic of each. Then Created a database called “test” consisting of table “Question-set” having 5 coloumns(“Qid”,”Question”,”Option1”,”Option2”,”Option3”,”Option4”,”Answer”). 
- Then wrote a code to connect the database with the program. 
- Then wrote the logic to print random questions from database along with storing the Qid in set() so that questions don’t repeat and to keep a track of which question from the database was called.

**9. @Deepakjjha - *deepakjha688@gmail.com***
- Researched and Drawn some ER diagram about the problem statement for better understanding.
- Created a database by using python sqlite3 named "random_questions.db" which consists of question and  answer table which contains multiple columns of exam questions,answer and their options.
- Then using different SQL command insert the values in the columns and display the table value which is present in the database.
- Then build the logic of the program that would print random questions from the database and display them.

**10. @Shrutika Netke - *shrutikanetke2205@gmail.com***
- I first tried to gain more knowledge on the problem statement by learning the basics and then slightly started with the more complicated part.
- Then i created a database with question,answer and user table.
- Then wrote a python program which would enable me to create a  program that would fetch questions randomly from the database and display them

**11. @iamtwinklearora - *aroratweety68@gmail.com***
- Researched about the project at first, gained all the knowledge, cleared up doubts i had with my team. Learned every basic detail in dept. 
- Then started to create database for questions, also created user table. Then wrote a python program to execute the whole idea i.e the whole database. 
- Solved the errors i had and did successfully run the program which was made to select & display random questions from the database

**12. @Prashna Shetty - *prashna220499@gmail.com***
- I first researched about the project and tried to understand the project requirements. 
- Attended the meeting, researched about what the platform should look like, drafted a demo layout of the platform's appearance. 
- Gained the knowledge about the requirements by discussing with the team and clearing my doubts. Checked out the other types of methods available. 
- Checking out similar program/ software and also different types of questionnaires available and are being used.
- Attending meeting and discussions with the team and successfully executed the program which was made to select & display random questions from the database.

**13. @Pratikrane123 - *pratikrane786000@gmail.com***
- First I tried to understand the project, Gain knowledge about the project by doing some research. Finding few other way to implement the project. 
- Then gain some basic concepts of python. Create a database and user table.
- then wrote a code to connect database with the program, got few error but was able execute the program and display random question from the database

**14. @pratik80 - *pratiknikumbe8@gmail.com***
- First I did research on system requirements then installed postgresql on my system then wrote program to display random questions from database using python

---
- **Note: Everyone in team discussed & used their own logic and came up with their different or same solution.In the end we chose one efficient & perfect code to push on gitHub repositary**
