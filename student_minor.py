# Print the menu
from ast import Break
from re import U


print("Select option from Menu\n-----------------------")
print("1. Login\n2. Create User")
#prompt and get the option the user selected
while True:
    user_option = input("Would you like to (1) login or (2) Create Account?")
    #ensure the user entered a valid option
    if user_option != "1" and user_option != "2":
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("OMG YOU DID IT :)")
        break
# if the user chose 1 ask for username and password


if user_option == "1":
    while True:
        user_name = input("Please enter your Username:")
        user_pass = input("Please enter your Password:")
        #validate username and password
        #open username file
        user_file = open("users.txt", "r")
        user_found = False
        for line in user_file:
            credentials = line.split(", ")
            if user_name == credentials[0] and user_pass == credentials[1]:
                user_found = True
                
        if user_found:
            print(f"User {user_name} is sucessfully logged in!")
            break
        else:
            print(f"User {user_name} not found")

#   if not valid prompt the user
#    If vcalid move on  to prompt for Studen information
#if user chose 2 ask for username and password
elif user_option == "2":
    while True:
        user_name = input("Please enter your Username (4 to 12 characters):")
        user_pass = input("Please enter your Password (6 to 16 characters):")
        username_length = len(user_name)
        password_length = len(user_pass)
    
        #validate username and passworld langth, if valid write to user.txt file and move on
        if username_length >=4 and username_length <=12 and password_length >=6 and password_length <=16:
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            break
        else:
            print("ERROR: Incorrect password or username length.\n")

print("Ask user for student data")
# Make 3 empty lists for name, score, and letter grade
student_names = []
student_scores = []
student_letter_grade = []

#prompt for number of students
number_of_students = int(input("Enter the number of students to enter grades for:"))
for counter in range(number_of_students):
    #Promt user to enter name and number score
    student_name = input("Enter student name:")
    student_score = float(input("Enter student score:"))

    #Store data in list
    student_names.append(student_name)
    student_scores.append(student_score)

    #Convert to letter grade
    if student_score <=100 and student_score >=90:
        student_letter_grade.append("A")
    elif student_score <90 and student_score >=80:
        student_letter_grade.append("B")
    elif student_score <80 and student_score >=70:
        student_letter_grade.append("C")
    elif student_score <70 and student_score >=60:
        student_letter_grade.append("D")
    else:
        student_letter_grade.append("F")
    #Print student date (name, score, grade)
for index in range (number_of_students):
    print(f"Student name: {student_names[index]},{student_scores[index]}, {student_letter_grade[index]}")
