def quiz_game():
    questions=("Which data structure is used for implementing recursion?:",
               "The data structure required to check whether an expression contains a balanced parenthesis is?:",
               "Who developed Python Programming Language?",
               "Which of the following is the correct extension of the Python file?",
               "A non-metal used to preserve food material is:")
    
    options=(("A. Stack","B. Queue","C. List","D. Array"),
             ("A. Queue","B. Stack","C. Tree","D. Array"),
             ("A.Wick van Rossum","B.Rasmus Lerdorf","C.Guido van Rossum","D.Niene Stom"),
             ("A. .python","B. .pl","C. .py","D. .p"),
             ("A. Carbon","B. Phosphorus","C. Sulphur","D. Nitrogen"))
    
    answers=("A","B","C","C","D")
    guesses=[]
    score=0
    question_no=0

    for question_no, question in enumerate(questions):
        print("--------------------")
        print(question)
        for option in options[question_no]:
            print(option)

        guess=input("Enter (A,B,C,D):").upper()
        guesses.append(guess)
        if guess==answers[question_no]:
            score+=1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_no]} is the correct answer.")
    print("--------------------")
    print("        RESULTS         ")
    print("--------------------")

    print("answers:",end=" ")
    for answer in answers:
        print(answer,end=" ")
    print()

    print("guesses:",end=" ")
    for guess in guesses:
        print(guess,end=" ")
    print()
    score=int(score/len(questions)*100)
    print(f"Your Score is:{score}% ")
quiz_game()