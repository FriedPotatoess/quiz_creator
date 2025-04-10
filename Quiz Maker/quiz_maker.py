#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
#GOALS: 1: Create a program that lets user create a quiz 2: Create a way for that file to be saved in the user folder

#Quiz Creator
def quiz_maker():
    while True:
        questions = input("Enter your Question: ")
    
        options = {}
        for option in ['A', 'B', 'C', 'D']:
            options[option] = input(f"{option}: ")
            
        correct_answer = input("Which letter is the correct answer?(A, B, C, or, D): ").upper()
        print(f"Question: {questions}")
        print("Choices: ")
        for option, answer in options.items():
            print(f"{option}: {answer}")
        print(f"Correct Answer: {correct_answer}\n")
        
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
    