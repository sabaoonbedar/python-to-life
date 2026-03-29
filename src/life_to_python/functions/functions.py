questions = [{"question":"What is the capital of Afghanistan? ","answer":"kabul"},
             {"question":"who was our first president? ","answer":"dawood khan"}
             ,{"question":"Who was our last king? ","answer":"zahir shah"},
             {"question":"Who was our national hero? ","answer":"zahir shah"}
             ]


def question_addition_helper(q,a):
    question_addition = questions.extend([{"question":q,"answer":a}])
    
    
def add_the_question():
    q = input("question to add: ")
    q = q.strip()
    a = input("answer to add: ")
    a = a.strip()
    question_addition_helper(q,a)
    
add_the_question()    


def run_quiz():
 score = 0

 for i in questions:
  userInput = input(i["question"] + ": ")
  if userInput.lower() == i["answer"]:
   print("Correct")
   score = score + 1
  else:
      print("wrong")
 print("your final score is :", score)
run_quiz()



