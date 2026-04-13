from BaseQuiz import BaseQuiz

class QuizReader(BaseQuiz):

    def __init__(self,questionfilename,answerfilename):
        open(questionfilename,'a').close()
        open(answerfilename,'a').close()

    def read_questions(self,filepath,answerfilepath): #reads all questions the user added to the file

        with open(filepath,'r') as r:
            print("Questions:")
            for i in r:
                print(i,end='') #reads every line in the file
        print()
        with open(answerfilepath,'r') as t:
            print("Answers:")
            for o,v in enumerate(t):
                print(o + 1,v,end='') #shows answer and question number
        print("\n\n")


    def clear_all(self,filepath,answerfilepath): #clears the questions and answer files; start from scratch
        open(filepath,'w').close()
        open(answerfilepath,'w').close()

    def write_add_ques_ans(self,filepath,answerfilepath):
        while True:
            choice = 0
            question = '' #default
            answer = ''
            holdline = ''
            print("Write your question (Hit Enter without typing anything to once finished):")
            while True: #loops to add as long of questions as they want
                question = input().strip()
                if question =='': #stopper
                    print("Is this question correct? [1/0]") #Confirm question
                    while True:
                        try:
                            choice = int(input("Select confirmation:"))
                            if choice == 1 or choice == 0:
                                break
                            else:
                                print("Invalid choice")
                                continue
                        except:
                            print("Invalid input try again")
                            continue
                    if choice == 1:
                        break
                    else:
                        holdline = ''
                        print("Write your question (Hit Enter without typing anything to once finished):")
                        continue
                else:
                    holdline += question + "\n"
       
            while True:
                print("Enter the answer for the question:")
                answer = input().strip()
                if answer=='':
                    continue #In case of accidents
                print("Is this answer correct? [1/0]") #Confirm answer
                while True:
                    try:
                        choice = int(input("Select confirmation:")) #same as earlier but for answer
                        if choice == 1 or choice == 0:
                            break
                        else:
                            print("Invalid choice")
                            continue
                    except:
                        print("Invalid input try again")
                        continue

                if choice == 1:
                    break
                else:
                    answer = ''
                    continue

                    
            with open(filepath,'a') as f: #'a' for append to avoid overwriting data
                    f.write(holdline + "\n")

            with open(answerfilepath,'a') as a:
                    a.write(answer + "\n")

            while True:
                    print("Add a new question? [1/0]")
                    try:
                        choice = int(input("Select confirmation:")) #same as earlier but for answer
                        if choice == 1 or choice == 0:
                            break
                        else:
                            print("Invalid choice")
                            continue
                    except:
                        print("Invalid input try again")
                        continue
            if choice == 1:
                continue
            else:
                break
            
    def remove_question(self,filepath,answerfilepath):
        questions = []
        answers = []

        #reads all answers into a list
        with open(answerfilepath,'r') as an:
            for i in an:
                answers.append(i.strip())

        #reads all questions into a list
        with open(filepath,'r') as r:
            holdline = "" 
            for line in r:
                if line.strip() == "":
                    if holdline: 
                        questions.append(holdline)
                        holdline = "" #resets
                else:
                    holdline += line
            
            if holdline: #just in case to catch the last question
                questions.append(holdline)

        #stops if files are empty
        if len(questions) == 0:
            print("No questions to remove.")
            return

        print("Here are your current questions:")
        for o,v in enumerate(questions):
            print(f"[{o + 1}]\n{v.strip()}\n") #shows question number and question

        while True:
            print(f"Select a question number to remove (1-{len(questions)}) or 0 to cancel:")
            try:
                choice = int(input())
                if choice == 0:
                    print("Cancelled.")
                    return
                if choice >= 1 and choice <= len(questions):
                    break
                else:
                    print("Invalid choice")
                    continue
            except:
                print("Invalid input try again")
                continue

        #removes the selected index from both lists
        index = choice - 1
        questions.pop(index)
        answers.pop(index) 

        print("Question successfully removed!\n")

        #overwrites the files with the updated

        # rewrite questions file
        with open(filepath, 'w') as f:
            for q in questions:
                f.write(q.strip() + "\n\n")  # keep spacing format

        # rewrite answers file
        with open(answerfilepath, 'w') as a:
            for ans in answers:
                a.write(ans + "\n")

    def quiz_mode(self,filepath,answerfilepath):

        with open(answerfilepath,'r') as an: #answer file

            answer_list = []
            score = 0
            ans_ind = 0

            for i in an:
                answer_list.append(i.strip()) #adds it into a list


        with open(filepath,'r') as r:
            check_line = "" #store/print lines until empty space. (no touchy)
            for line in r:
                if line.strip() == "": #Only until collected all lines
                    if check_line: #Checks if line is not empty or else false
                        print(check_line) #Prints all that is appended
                        ans = input("Enter your answer here: ")
                        print()
                        if ans_ind < len(answer_list) and ans.lower() == answer_list[ans_ind].lower(): #No need to worry about capitalization and avoids IndexError
                            score += 1
                        
                        ans_ind += 1
                        check_line = "" #resets to normal

                else:
                    check_line += line #collects the lines together until empty space bago nya i-print all at once
            
            if check_line: #just in case to avoid not reading the last question and stops extra spaces
                print(check_line)
                ans = input("Enter your answer here: ")
                if ans_ind < len(answer_list) and ans.lower() == answer_list[ans_ind].lower(): #Same as before
                    score += 1
        
        print(f"Your score is: {score}/{len(answer_list)}")


#Remove the tags to run test

#File names can be changed to whatever you want (Remove Tags to test):
#questfile = "Questions.txt"
#ansfile = "Answers.txt"

#Features:

#Parameters are changeable

#test = QuizReader(questfile,ansfile)  #Invokes the class (remove the hastag to begin testing)
#test.write_add_ques_ans(questfile, ansfile) #Adds a question and an answer
#test.remove_question(questfile, ansfile) #Removes a question and an answer
#test.quiz_mode(questfile, ansfile) #Begin Quiz
#test.read_questions(questfile, ansfile) #Shows all questions and answer list
#test.clear_all(questfile, ansfile) #Clears everything in the files, remove the hashtag to test

