#start date:- 16/11/2022   #End date:-13/12/2022
#author:- Rochana Godigamuwa
#To obtain Progression outcomes of students in a university

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: ………w1954113……………..…
# Date: ……13/12/2022………………..…




students=0
trailer=0
progress=0
retriever=0
exclude=0
progress_list=[]
retriever_list=[]
trailer_list=[]
exclude_list=[]
range_check=[0,20,40,60,80,100,120]

print("-----Calculate Student Progression outcome of the academic year-----\n")
print('Enter "Student" if you want access STUDENT VERSION or enter ANY OTHER CHARACTER to access STAFF VERSION\n')
Version=input('Enter the version you want to run in : ').lower()
print('-'*80)


def check_input(Message):
    while True:
            try:
                number=int(input(Message))
            except ValueError:
                print("Integer required")
                continue
            else:
                return number

def print_outcome(Scorelist,Progress_outcome):  
    for x in range(len(Scorelist)):
          print(Progress_outcome,Scorelist[x])




while True:
    while True:
            total=0
            credit_pass=check_input("Please enter your credits at pass: ")
            if credit_pass not in range_check:
                print("Out of range\n")
                continue
            credit_defer=check_input("Please enter your credits at defer: ")
            if credit_defer not in range_check:
                print("Out of range\n")
                continue
            credit_fail=check_input("Please enter your credits at fail: ")
            if credit_fail not in range_check:
                print("Out of range\n")
                continue

            total=credit_pass + credit_defer + credit_fail
            if  total > 120 or total < 120:
                print("Total incorrect\n")
                continue
            elif credit_pass in [120] and credit_defer in [0] and credit_fail in [0]:
                students+=1
                print("Progress\n")
                progress+=1
                progress_list.append((credit_pass,credit_defer,credit_fail))        #Taken from 'Stackflow', appendding 3 variables as one index
                break
            elif credit_pass in [100] and credit_defer in [0,20] or 0 and credit_fail in [0,20]:
                students+=1
                print("Progress(module trailer)\n")
                trailer+=1
                trailer_list.append((credit_pass,credit_defer,credit_fail))
                break
            elif credit_pass in [80,60,40,20,0] and credit_defer in [120,100,80,60,40,20,0] and credit_fail in [60,40,20,0]:
                students+=1
                print("Module retriever\n")
                retriever+=1
                retriever_list.append((credit_pass,credit_defer,credit_fail))
                break
            elif credit_pass in [40,20,0] and credit_defer in [40,20,0] and credit_fail in [120,100,80]:
                students+=1
                print("Exclude\n")
                exclude+=1
                exclude_list.append((credit_pass,credit_defer,credit_fail))
                break
    if Version=='student':
        break
    print("Would you like to enter another set of data?")
    user_response=input("Enter 'y' for yes or 'q' for quit and view results: ").lower()
    print()

    while user_response not in ('y','q'):                   #If anything as than y or q is entered the program would as again and again from the user the correct input
        user_response=input("Please re-enter 'y' for yes or 'q' for quit and view results: ").lower()
        

    if user_response=='q':
           print('-'*50)
           print("Histogram")
           print("Progress",progress," \t: ",'*'*progress)
           print("Trailer",trailer," \t: ",'*'*trailer)
           print("Retriever",retriever," \t: ",'*'*retriever)
           print("Excluded",exclude," \t: ",'*'*exclude,"\n")
           print()
           print(students," outcomes in total.")
           print('-'*50,'\n')
           
    elif user_response=='y':
           print()
           continue

    print_outcome(progress_list,'Progress - ')               #Goes into the 'print_outcome program and executes what's inside it
    print_outcome(trailer_list,'Progress (module trailer) - ')
    print_outcome(retriever_list,'Module retriever - ')
    print_outcome(exclude_list,'Exclude - ')        
    break
