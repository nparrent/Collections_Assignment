[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/pW6Oujv2)
# Collections THA
In this assignment you will practice using collections for a student management system. This system will allow you to add students, view GPA metrics, and assign academic violations.

## Instructions
To submit this assignment, please perform the following:
1. Follow the instructions below.
1. When prompted, name your Python file `firstname_lastname_grading` where `firstname` is your first name and `lastname` is your last name.
1. Push your assignment to GitHub.

## Grade Entry System
You are a recent hire for an application development organization. They primarily develop learning management systems for higher education. They are currently migrating their system from Java to C#. Your supervisor, Koorthi Jarvenpaa, has tasked you with developing a grade entry program.

The program should have the following abilities:

| Function | Description |
|:---:|:---|
| Menu Navigation (1 pt.) | Provide the user the ability to traverse a menu: Student Information Query, Student Information Entry, Query GPA Metrics, Academic Violations, Quit Program |
| Student Information Query (1 pt.) | The user can query the system for a list of all the students in the system. Please display the student information in a nicely formatted manner. |
| Student Information Entry (3 pts.) | Prompt the user to create a new student record. Prompt the user for the first name, then the last name, then major, and GPA last. |
| Query GPA Metrics (2 pt.) | The user can query the data for the following: *max* GPA, *min* GPA, *average* GPA. Display each of these on a separate line. Your program should update *max* GPA, *min* GPA, and *average* GPA each time the `Query GPA Metrics` menu option is selected. |
| Academic Violations (3 pts.) | Provide the user a list of current students. After selecting a student, provide them a list of academic violations which they can select (i.e., copying homework, cheating on exam, plagiarism, cheating on quiz, writing paper for another student). A student may only have one academic violation at a time. |

In addition to the requirements above, you have been asked to rely on arrays and lists. I recommend you do not rely on multidimensional lists for this assignment. Specifically, you will need to use lists for the following:
* Storing student information
* Storing academic violations (see in table above)

In all, you should have 6 lists in your program. Your program should start with the following students in the system:
* Harrison Bartlett
* Joel Christopherson
* Ashley Hardin
* Justin Bangston

After you get your program running, you will need to add two more students, one of which is you. Thus, you will have six total students stored in your program. When the user adds a new student to the system, they will not be prompted to add an academic violation. An academic violation is only added via the Academic Violation system.

Take a screenshot, save the image in `assets`, and link it in [submission.md](/submission.md) for the following:
1.  After updating your system with your two new students, take a screen capture of `Student Information Query`
1. `Query GPA Metrics` before you add the 2 new students and after
1. `Academic Violations`: successfully adding violations to two students.