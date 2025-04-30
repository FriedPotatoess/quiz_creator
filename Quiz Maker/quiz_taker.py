#Goal: Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
#Milestones:
#1. Create a Program that pull a text file from the folder by asking the name of the test
#2. Probably randomize the question and place a score and correct answer at the start
#3. Beautify


def init_quiz(filename):
    questions = []
    try:
        with open(filename, r) as file:
            while True:
                question_line=file.readline()
                if not question_line:
                    break
                
                question = question_line.split(":", 1)[1].strip()

                options = {}
                for option in ['A', 'B', 'C', 'D']:
                    option_line = file.readline().strip()
                    options[option] = option_line.split(":", 1)[1].strip()