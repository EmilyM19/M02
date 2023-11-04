"""
Author:  Emily Mullins
Date written: 11/1/2023
File: CaseStudy.py
Short Desc: This program will prompt a user to enter a student's last name, first name
and gpa. The program will then display whether the student has made the Dean's List
or Honor Roll based on GPA. Users will continue entering students until entering
the quit phrase 'ZZZ'.
            
"""

quit = "ZZZ"

while True:
    lName = input("Enter the student's last name, or 'ZZZ' to quit: ")
    if lName == quit:
        print("You have ended the program")
        break
    else:
        fName = input("Enter the student's first name: ")
        GPA = float(input("Enter the student's GPA: "))
        if GPA >= 3.5:
            print(fName + " " + lName + " has made the Dean's List.")
        elif GPA >= 3.25: 
            print(fName + " " + lName + " has made the Honor Roll.")