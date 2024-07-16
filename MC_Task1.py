questions = [
  [
    "Which language was used to create Facebook?",
    "Python","Java",
    "C++","PHP", 4
  ],
  [
  "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf",
    "Guido van Rossum","Niene Stom",3
  ],
  [
    "Which type of Programming does Python support?", " object-oriented programming",
    "structured programming",
    "functional programming","all of the mentioned",4
  ],
  [
    "Is Python case sensitive when dealing with identifiers?" ,"no", "yes","machine dependent",
    "none of the mentioned",2
  ],
  [
    "Which of the following is the correct extension of the Python file?",
    ".python",
    ".pl",
    ".py",
    ".p",
    3
  ],
  [
    "Which of the following character is used to give single-line comments in Python?",
    "//",
    "#",
    "!",
    "/*",
    2
  ],
  [
    "Python supports the creation of anonymous functions at runtime, using a construct called ?",
    "pi",
    "anonymous",
    "lambda",
    "none of the mentioned",
    3
  ],
  [
    "Which of the following is not a core data type in Python programming?","Tuples",
    "Lists",
    "Class","Dictionary",3
  ],
  [
    "Which one of the following is not a keyword in Python language?","pass","eval",
    "assert","nonlocal",2
  ],
  [
    "What will be the output of the following Python expression if x=56.236?",
    "56.236",
    "56.23",
    "56.0000",
    "56.24",
    4
  ]
]

levels = [10,20,30,40,50,60,70,80,90,100]
score =0

print("Welcome to Task 1:Basic Quiz Game at Motion Cut Internship !")
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for score: {levels[i]}")
  print(f"Your Question is {questions[i][0]}")  
  print(f"a. {question[1]}")
  print(f"b. {question[2]}")
  print(f"c. {question[3]}")
  print(f"d. {question[4]}")
  reply= int(input("Enter your answer (1-4):"))
  if (reply == question[-1]):
    print(f"Correct answer, you have scored:{levels[i]}")
    if(i== 1):
      score== 10
    elif(i== 2):
      score== 20
    elif(i== 3):
      score== 30
    elif(i== 4):
      score== 40
    elif(i== 5):
      score== 50
    elif(i== 6):
      score== 60
    elif(i== 7):
      score== 70
    elif(i== 8):
      score== 80
    elif(i== 9):
     score== 90
    elif(i== 10):
     score== 100
     print(f"Congratulations You are a Genius !!!! You have got full score 100")

  else:
    print("Wrong answer!")
    print(f"You have scored: {score}")
    break
