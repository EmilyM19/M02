quit = "ZZZ"
lName = input("Enter the student's last name, or 'ZZZ' to quit: ")
while lName != quit:
    fName = input("Enter the student's first name: ")
    studentGPA = float(input("Enter the student's GPA: "))
    if studentGPA >= 3.5:
        print(fName + " " + lName + " has made the Dean's List.")
    elif studentGPA >= 3.25:
        print(fName + " " + lName + " has made the Honor Roll.")
    lName = input("Enter the student's last name, or 'ZZZ' to quit: ")
else:
    print("You have ended the program.")
    exit()