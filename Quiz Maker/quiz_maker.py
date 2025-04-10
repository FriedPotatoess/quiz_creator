#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
#GOALS: √1: Create a program that lets user create a quiz 2: Create a way for that file to be saved in the user folder

def save_file(questions, options, correct_answer, test_name):       
    with open(test_name, "a") as file:
        file.write(f"Question: {questions}\n")
        for option, answer in options.items():
            file.write(f"{option}: {answer}\n")
        file.write(f"Correct Answer: {correct_answer}\n\n")



#Quiz Creator
def quiz_maker():
    test_name = input("What would be the name of this here's quiz?: ")
    if not test_name.endswith(".txt"):
        test_name += ".txt"  
   
    while True:
        questions = input("Enter your Question: ")
        #Stores the answer    
        options = {}
        for option in ['A', 'B', 'C', 'D']:
            options[option] = input(f"{option}: ")
        #Determines the correct answer   
        correct_answer = input("Which letter is the correct answer?(A, B, C, or, D): ").upper()
        #Reiterates your question, the choices and the correct answer
        print(f"Question: {questions}")
        print("Choices: ")
        for option, answer in options.items():
            print(f"{option}: {answer}")
        print(f"Correct Answer: {correct_answer}\n")
        
        #Calls the save_file function to save the text already placed, before asking the user if they want to repeat the process again
        save_file(questions, options, correct_answer, test_name)
        
        #Asks the user if they want to input another set of question
        while True:
            continue_questioning = input("Enter another question? (Yes/No): ").capitalize()
            if continue_questioning == "Yes":
                break
            elif continue_questioning == "No":
                print("Thank you for using the Quiz Maker, now exiting...")
                return
            else:
                print('Please choose between "Yes" or "No"')
        
quiz_maker()
    