'''
Set Lists
Menu
    Student Information Query, 
    Student Information Entry, 
    Query GPA Metrics, Academic Violations, 
    Quit Program
Student Info
    - First Name
    - Last Name
    - Major
    - GPA
    Format nice table
Add Student
    Prompt for about
    input()
    firstname, 
Query GPA
    max GPA
    min GPA
    average GPA
    update each time????
Academic Violations
    List of students to pick from 
    input()
    Violations list
        copying homework
        cheating on exam
        plagiarism
        cheating on quiz
        writing paper for another student
'''
from tabulate import tabulate
# Initialize Lists
first_name = ['Harrison', 'Joel', 'Ashley', 'Justin']
last_name = ['Bartlett', 'Christopherson', 'Hardin', 'Bangtson']
major = ['Business', 'Business', 'Business', 'Underwater Basket Weaving']
gpa = [3.5, 3.2, 3.9, 3.9]
violations =['None', 'None', 'None', 'None']
studentID = list(range(1, len(first_name) + 1))

violationList = ['Copying Homework', 'Cheating on Exam', 'Plagiarism', 'Cheating on Quiz', 'Writing Paper for Another Student']

student_id = int()
vio_idx = int()


# Create Student Entry Table
def student_entry_table():
            data = list(zip(studentID, first_name, last_name, major, gpa, violations))

            # Define headers for the table
            headers = ["Student ID", "First Name", "Last Name", "Major", "GPA", "Violations"]

            # Print the table
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))  
# Welcome
print("\nWelcome to the Grade Entry Program\n")

while True:
    quitProg = False
    print("Please Select from the following\n")
    print(f'1) Student Information Query\n2) Student Information Entry\n3) Query GPA Metrics\n4) Academic Violations\n5) Quit Program')
    #Promt for Menu Selection
    menuSelection = int(input())

    if menuSelection == 1:
    # Student Information Query
        print('Here is the Student Information Table')
        student_entry_table()
        
        #Exit Statement
        input('Press Enter to Go Back to the Main Menu')
        
    elif menuSelection == 2:
    # Enter New Student
        while True:
            print('Welcome to the Student Entry System')
            print("What is the Student's First Name?")
            first_name.append(input())
            print("What is the Student's Last Name?")
            last_name.append(input())
            print("What is the Student's Major?")
            major.append(input())
            print("What is the Student's G.P.A?")
            gpa.append(float(input()))
            violations.append('None')
            studentID.append(len(studentID) + 1) 

            student_entry_table()
        
             # Exit Statement
            choice = input('Press 1 to enter another student, Press 2 to Go Back to the Main Menu: ')
            if choice == '2':
                break
            elif choice != '1':
             print("Hmm, something didn't work right. Please try again.")
           
    elif menuSelection == 3:
    # Query GPAs    
        print('\nWelcome to the GPA Statistics Page\n')
    
        while True:
            # Variables
            GPAmax = max(gpa)
            GPAmin = min(gpa)
            GPAavg = sum(gpa)/len(gpa)
            stat = int(input('\nWhat would you like see?\n1) The Maximum GPA\n2) The Minimum GPA\n3) The Average GPA\n4) Go Back to the Main Menu\n'))

            if stat == 1:
                GPAmax = max(gpa)
                print(f'The maximum  GPA is: {GPAmax}')
            elif stat == 2:
                print(f'The minimum GPA is: {GPAmin}')
            elif stat == 3:
                print(f'The average GPA is: {GPAavg}')
            elif stat == 4:
                break
            else:
                print("Hmm, something didn't work right. Please try again.")
            
    elif menuSelection == 4:
    # Academic Violations
        while True:
            print('\nStudent Violation Page\n')
            student_entry_table()

        #Select Student
            student_id = int(input("Please Select a Student by Student ID from the Student Table above\n"))
            print(f'\nThe student you have selected is {first_name[student_id - 1]} {last_name[student_id - 1]}.\n Violation Type:\n')

        #Print Violation List
            v = 0
            while v < len(violationList):
             print(f"{v+1}) {violationList[v]}")
             v+=1
        
        #Select Violation
            vio_idx = (int(input("Please select from the list of violations above to add to the student's record\n")))
            if 1 <= vio_idx <= len(violationList):
                if 0 <= student_id - 1 < len(violations):
                    violations[student_id-1] = violationList[vio_idx - 1]
                print("Violation added successfully!")
            else:
                print("Invalid entry please try again")
            
            choice = input('Press 1 to enter another violation, Press 2 to Go Back to the Main Menu: ')
            if choice == '2':
                break
            elif choice != '1':
                print("Hmm, something didn't work right. Please try again.")

            student_entry_table()

    elif menuSelection == 5:
        quitProg = True

    else:
        # Output if client selects incorrect option
        print("Oh No! That is not an option. Please try again")

    if quitProg:
        # Quitting the program
        print(f"Thank you have a nice day")
        break


# Query Students
# Student Info Entry
# Query GPA Metrics
# Assigning Violations