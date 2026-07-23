# Q2: write a simple program to determine if a given year is a leap year using user input.
print("Leap Year Checking Program: ")

year=int(input("Enter Any Year (eg.2026): "))

if (year%4 == 0 and year%100 != 0) or(year%400 == 0):
    print(f"{year} is a Leap Year. ")
else:
    print(f"{year} is not a leap Year. ") 