import random
#define a math question function
def generate_question():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice(['+' , '-' , '*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return f"{num1} {operator} {num2}",answer
    
# define math quiz function
def math_quiz():
    score=0
    rounds=5

    print("\n---Welcome to the math Quiz!---")     
    print("You will be presented with math problems, and you need to provide the correct answer")

    for i in range(rounds):
        question, correct_answer =generate_question()
        print(f"\nQuestion{i+1}: {question}")
        user_answer= int(input("Your answer: "))

        if user_answer==correct_answer:
            print("Correct")
            score+=1
        else:
            print(f"Wrong ! The correct answer is : {correct_answer} ")

    print("Game Over!")
    print(f"Your final score is {score}/{rounds} ") 

    if score==rounds:
        print("Congratulations! You got all the answer correct")
    elif score >= rounds//2:
        print("Good job! You did well")
    else:
        print("Keep practicing! You can do better next time")

#run the game
math_quiz()            