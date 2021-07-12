def random_questions(n):
  db=con.cursor()                  #con is database connecting instance 
  m=n+(math.floor(n/2))           #n=no. of requested row, m=no. of rows to be pulled from database 
  db.execute("SELECT * FROM questionlist ORDER BY RANDOM() LIMIT (?)",(m,))
  list_of_fatched_tuples=db.fetchall()

#converting list of fetched tuples to nested list
  list_of_all_questions=[]
  for i in list_of_fatched_tuples:
    list_of_all_questions.append(list(i))

#removing questions if any question is repeated 
  existing_ids=[]
  final_question_set=[]
  for i in list_of_all_questions:
    if i[0] not in existing_ids:       #here assuming 1st column of table is question id no.
      existing_ids.append(i[0])
      final_question_set.append(i)
      if len(final_question_set)>=n:    
        break;

  db.close()
  return final_question_set

  #additional module require is 1.math 