#Goal: Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
#Milestones:
#1. Create a Program that pull a text file from the folder by asking the name of the test
#2. Probably randomize the question and place a score and correct answer at the start
#3. Beautify

import os
import random

#Loads the quiz
def init_quiz(filename):
    components = []
    try:
        with open(filename, 'r') as file: #Opens the file
            while True:
                question_line=file.readline()
                if not question_line:
                    break
                
                question = question_line.split(":", 1)[1].strip()

                options = {}
                for option in ['A', 'B', 'C', 'D']:
                    option_line = file.readline().strip()
                    options[option] = option_line.split(":", 1)[1].strip()
                    
                correct_answer = file.readline().strip()
                correct_letter = correct_answer.split(":", 1)[1].strip().upper()
                
                #Compile the questions options and answer
                components.append((question, options, correct_letter))
                file.readline()
    
    #Error if file test is not found
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return components

#Quiz Runner
def quiz_runner(questions):
    score = 0
    user_answers = []
    random.shuffle(questions) #Randomize question positions
    
    for test, (question, options, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {test}: {question}")
        for option, answer in options.items():
            print(f" {option}: {answer}")
            
        #Input from the user, also a prevention for an unwarranted answers like numbers
        while True:
            user_answer = input("Your answer: ").upper()
            if user_answer in ['A' , 'B' , 'C' , 'D']:
                break
            print("Please input a valid answer")
        #Scores stuff
        is_correct = (user_answer == correct_answer)
        if is_correct:
            score += 1
        
        user_answers.append((question, options, user_answer, correct_answer, is_correct))
        
    #Final Score
    print(f"\nScore: {score}/{len(questions)}")
    #Reviewer
    print("Review")
    for review, (question, options, user_answer, correct_answer, is_correct) in enumerate(user_answers, 1):
        print(f"\nQuestion {review}: {question}")
        for option, answer in options.items():
            print(f"  {option}: {answer}")
        
        print(f"Your answer: {user_answer} - {'Correct!' if is_correct else f'Incorrect. Correct answer: {correct_answer}'}")

        
    
#Runs the code 
if __name__ == "__main__":
    print("Available quiz files:")
    for file in os.listdir():
        if file.endswith(".txt"):
            print(os.path.splitext(file)[0])#Removes txt in the display

    #Input the quiz name even though without txt
    filename = input("\nEnter the name of the quiz: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    questions = init_quiz(filename)
    if questions:
        quiz_runner(questions)
    else:
        print("No questions found or quiz file is invalid.")        
    
    