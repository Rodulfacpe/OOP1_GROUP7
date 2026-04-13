from QuizReader_updated import QuizReader

quiz = QuizReader("Questions.txt", "Answers.txt")
while True:
    print('''Welcome to the Quiz Menu!\nSelect an option:\n1. Add a Question\n2. Remove A question\n3. View Questions\n4. Quiz Mode\n5. Clear all\n6. Exit\n''')
    while True:
        try:
            choice = int(input("Select option:"))
            if choice < 7 and choice > 0:
                break
            else:
                print("Invalid choice")
                continue
        except:
            print("Invalid input try again")
            continue
    if choice == 1:
        quiz.write_add_ques_ans("Questions.txt", "Answers.txt")
    elif choice == 2:
        quiz.remove_question("Questions.txt", "Answers.txt")
    elif choice == 3:
        quiz.read_questions("Questions.txt", "Answers.txt")
    elif choice == 4:
        quiz.quiz_mode("Questions.txt", "Answers.txt")
    elif choice == 5:
        quiz.clear_all("Questions.txt", "Answers.txt")
    elif choice == 6:
        break