import json
import csv
import random
import os
def menu_list(list):
    x=1
    for i in list:
        print(f"{x}.{i}")
        x+=1   
def json_load(data,filepath ):
 file = open(filepath , "w")
 content = json.dumps( data, indent= 2)
 file.write(content)
 file.close()
def json_read(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        items = json.loads(data)
    return items
def csv_append(filepath, data):
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
def csv_read(filepath):
    csvfile=open(filepath, newline='') 
    reader = csv.DictReader(csvfile)
    return reader         
def display_grades_by_code(user_code):
    with open("grades.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 4 and row[0] == user_code:
                print(f"Subject: {row[2]}, Correct Answers: {row[4]}, Total Questions: {row[5]}")    
def ask_questions(questions, num_questions):
    correct_answers = 0
    asked_questions = set()  
    while len(asked_questions) < num_questions:
        question_number = str(random.randint(1, num_questions))
        if question_number in asked_questions:
            continue  
        asked_questions.add(question_number)
        
        question = questions["questions"][question_number]["question"]
        options = questions["questions"][question_number]["options"]
        print(f"\nQuestion {question_number}: {question}")
        print("Options:")
        for key, value in options.items():
            print(f"{key}: {value}")
        while True:
            user_answer = input("Enter your answer (a, b, c, d): ").strip().lower()
            if user_answer in ("a", "b", "c", "d"):
                break
            else:
                print("Please enter a letter of the options.")
                continue

        correct_answer = questions["questions"][question_number]["answer"]
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
    return correct_answers
def exit_program():
    """Exits the program."""
    print("Exiting program...")
    exit()
user_login_json = json_read("users.json")
 
while True:
 os.system("cls")   
 print("welcume Student!") 
 menu_list(["login","signup","exit"])
 
 while True:
        main_user_input= input("enter your answer: ")
        if main_user_input.isdigit():
            break
        else:
            print("Please enter a valid integer.");continue
 main_user_input = int(main_user_input)
 if main_user_input == 1:
    
    
    while True:
        user_code = input("Enter your code: ")
        user_name = input("Enter your name: ")
    
        for user_code_in_file, user_data in user_login_json.items():
            if user_code == user_code_in_file:
                if user_data["user name"] == user_name:
                    print("Login successful!")
                    print(f"Welcome {user_name}")
                    break
                else:
                    print("Incorrect name!")
                    continue
        else:
            print("Incorrect code! Please try again.")
            continue  
        break 
    menu_list(["grades","exam"])
    while True:
         user_input= input("enter your answer: ")
         if user_input.isdigit():
             break
         else:
             print("Please enter a valid integer.");continue
    user_input = int(user_input)
    if user_input == 1 :
        display_grades_by_code(user_code)
        input("press any key")
    elif user_input == 2:
        menu_list(["Engilsh exam","Math exam"])
        while True:
         user_input= input("enter your answer: ")
         if user_input.isdigit():
             break
         else:
             print("Please enter a valid integer.");continue
        user_input = int(user_input)
        if user_input==1:
            menu_list(["easy","intermediate","hard"])
            while True:
             user_input= input("enter your answer: ")
             if user_input.isdigit():
              break
             else:print("Please enter a valid integer.");continue
            user_input=int(user_input)
             
            if user_input == 1 : 
                questions = json_read("MCQ.English_easy.json")
                print("\nWelcome to the English Exam!")
     
                while True:
                    question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                    if question_amount.isdigit() and 1 <= int(question_amount) <= 20:
                        
                        break
                    else:
                        print("Please enter a correct num number between 1 and 20.")
            
                num_questions = int(question_amount)
                
                print("\nLet's begin the exam!")
                
                correct_answers = ask_questions(questions, num_questions)
                print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
                csv_append("grades.csv", [user_code,user_name,"English", "easy", correct_answers,num_questions])
                input("press any key")
                
            if user_input == 2 :
                questions = json_read("MCQ.English intermediate.json")
                print("\nWelcome to the English Exam!")
     
                while True:
                    question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                    if question_amount.isdigit() and 1 <= int(question_amount) <= 20:
                        
                        break
                    else:
                        print("Please enter a correct num number between 1 and 20.")
            
                num_questions = int(question_amount)
                
                print("\nLet's begin the exam!")
                
                correct_answers = ask_questions(questions, num_questions)
                print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
                csv_append("grades.csv", [user_code,user_name,"English", "intermediate", correct_answers,num_questions])
                input("press any key")
                
            if user_input == 3:
                questions = json_read("MCQ.English_Hard.json")
                print("\nWelcome to the English Exam!")
     
                while True:
                    question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                    if question_amount.isdigit() and 1 <= int(question_amount) <= 100:
                        
                        break
                    else:
                        print("Please enter a correct num number between 1 and 20.")
            
                num_questions = int(question_amount)
                
                print("\nLet's begin the exam!")
                
                correct_answers = ask_questions(questions, num_questions)
                print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
                csv_append("grades.csv", [user_code,user_name,"English", "Hard", correct_answers,num_questions])
                input("press any key")
                
        elif user_input == 2:
            menu_list(["easy","intermediate","hard"])
            while True:
             user_input= input("enter your answer: ")
             if user_input.isdigit():
              break
             else:print("Please enter a valid integer.");continue
            user_input=int(user_input)
            if user_input == 1 : 
               questions = json_read("MCQ.math easy.json")
               print("\nWelcome to the Math Exam!")
    
               while True:
                   question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                   if question_amount.isdigit() and 1 <= int(question_amount) <= 20:
                       
                       break
                   else:
                       print("Please enter a correct num number between 1 and 20.")
        
               num_questions = int(question_amount)
               
               print("\nLet's begin the exam!")
               
               correct_answers = ask_questions(questions, num_questions)
               print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
               csv_append("grades.csv", [user_code,user_name,"Math", "easy", correct_answers,num_questions])
               input("press any key")
                
            if user_input == 2 :
                questions = json_read("MCQ.math intermediate.json")
                print("\nWelcome to the Math Exam!")
     
                while True:
                    question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                    if question_amount.isdigit() and 1 <= int(question_amount) <= 20:
                        
                        break
                    else:
                        print("Please enter a correct num number between 1 and 20.")
            
                num_questions = int(question_amount)
                
                print("\nLet's begin the exam!")
                
                correct_answers = ask_questions(questions, num_questions)
                print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
                csv_append("grades.csv", [user_code,user_name,"Math", "intermediate", correct_answers,num_questions]) 
                input("press any key")
            if user_input == 3:
                questions = json_read("MCQ.math Hard.json")
                print("\nWelcome to the Math Exam!")
     
                while True:
                    question_amount = input("Enter the number of questions you want to answer (maximum is 20): ")
                    if question_amount.isdigit() and 1 <= int(question_amount) <= 100:
                        
                        break
                    else:
                        print("Please enter a correct num number between 1 and 20.")
            
                num_questions = int(question_amount)
                
                print("\nLet's begin the exam!")
                
                correct_answers = ask_questions(questions, num_questions)
                print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
                csv_append("grades.csv", [user_code,user_name,"Math", "Hard", correct_answers,num_questions])
                input("press any key")
                    
            
        
 elif main_user_input == 2 :
    print("Signup")
    while True:
        user_code = input("Enter your code: ")
        user_name = input("Enter your name: ")

        if user_code in user_login_json:
            print("This code is already used. Please choose a different one.")
        else:
            user_login_json[user_code] = {"user code": user_code, "user name": user_name}
            json_load(user_login_json, "users.json")
            print("Signup successful!")
            print(f"Welcome, {user_name}!")
            input("press any key")
            break
 if main_user_input == 3:
    exit_program()

