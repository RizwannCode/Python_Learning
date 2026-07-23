# Q1: write a simple program to determine if a given year is a leap year using user input.

# print("Leap Year Checking Program: ")

# year=int(input("Enter Any Year (eg.2026): "))

# if (year%4 == 0 and year%100 != 0) \
#     or(year%400 == 0):
#     print(f"{year} is a Leap Year. ")
# else:
#     print(f"{year} is not a leap Year. ") 

# Q2: Login Authentication
# Login Authentication using conditional statement. Assume you have a predefined
# username and password.
# Write a program that prompts the user to enter a username and password and
# checks whether they match. Provide appropriate messages for the following
# cases:
# • Both username and password are correct.
# • Username is correct but password is incorrect.
# • Username is incorrect.

# My SOlution
# print("Login Authentication")
# user_name = "Rizwan63"
# password = "Zakir123"

# user_name1 = input("Enter user Name: ")
# password1 = input("Enter Password: ")

# if(user_name == user_name1) and (password == password1):
#     print("Welome Login Succesfully. ")
# elif(user_name==user_name1) and(password!=password1):
#     print("Login Failed! incorrect Password. ")        
# else:
#     print("Username is incorrect. ")    

# # Tutor Solution
# # Predefined username and password
# predefined_username = "Madhav"
# predefined_password = "Pass101"
# # Prompt the user for username and password
# input_username = input("Enter username: ")
# input_password = input("Enter password: ")
# # Check the username and password
# if input_username == predefined_username:
#     if input_password == predefined_password:
#         print("Welcome! Login was successful.")
#     else:
#         print("Login failed: Incorrect password.")
# else:
#     print("Login failed: Incorrect username.")    

# Q3: Admission Eligibility
# A university has the following eligibility criteria for admission:
# • Marks in Mathematics >= 65
# • Marks in Physics >= 55
# • Marks in Chemistry >= 50
# • Total marks in all three subjects >= 180 OR Total marks in Mathematics and
# Physics >= 140
# Write a program that takes marks in three subjects as input and prints whether the
# student is eligible for admission.

print("Admission Eligibility")

Maths_marks=int(input("Enter Your Math Marks: "))
Phy_marks=int(input("Enter Your Physics Marks: "))
Chemistry_marks=int(input("Enter Your Chemistry Marks: "))

if(Maths_marks >= 65 and  Phy_marks>=55 and  Chemistry_marks>=50 and \
 Maths_marks+Phy_marks+Chemistry_marks>= 180) or (Maths_marks + Phy_marks >= 140):
    print("You are Eligible.")
else:
    print("You are Not Eligible.")    