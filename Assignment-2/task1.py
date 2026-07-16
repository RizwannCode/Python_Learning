# Q.1: Write a program to input student name & marks of 3 subjects. 
# Print name & percentage in output. 

# name=input("Enter your Name: ")
# sub1=int(input("Enter subject 1 Marks: "))
# sub2=int(input("Enter subject 2 Marks: " ))
# sub3=int(input("Enter subject  3 Marks: "))

# percentage=(sub1+sub2+sub3)/300*100

# print(f"Mr. {name} your Exam percentage is {int(percentage)}%")



# Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.
my_dictionary={}
my_dictionary['Name']=input("Enter your Name: ")
my_dictionary['Age']=int(input("Enter your Age: "))
my_dictionary['Height']=float(input("Enter your Height: "))
my_dictionary['city']=input("Enter your city: ")
print(f"The Dictionary: {my_dictionary}")


#Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.

My_Name=input("Enter your Name: ")
Age=int(input("Enter your Age: "))
Height=float(input("Enter your Height: "))
city=input("Enter your city: ")
my_dictionary={'Name':My_Name,'Age':Age, 'Height':Height,'city':city}

print(f"The Dictionary: {my_dictionary}")
