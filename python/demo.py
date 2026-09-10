# a = int(input("Enter a number : "))
# print("your number : ", a)

# b = a + 23
# print(f"your number added to 23 is : {b}")

# Example 1 : Check if a number is odd
# a = int(input("enter a number  : "))
# print("statement : Is your number odd?")
# print(f"answer : {a % 2 == 1} ")
# this is better.
# b = ["even", "odd"]
# print(f"your number is {b[a % 2]}")

# Example 2 : Write a program to print age in days.
# assumption : for this use case i want age to be a floating point number.
# age = float(input("Input your age here : "))
# print("Your age in years is : ", age)
# print("Your age in days : ", int(age * 365))
# print(f"{age} years = {int(age * 365)} days")

# Examlple 3 : Write a program to convert minutes into hours and print it.
# minutes = int(input("enter minutes : "))
# print(f"{minutes} is {minutes // 60} hours and {minutes % 60} minutes")

# Example 4 : Write a program to extract the last digit of a number
# number = int(input("enter a number : "))
# print(f"{number} : last digit is {str(number)[-1]}") this is over-engineered but equally valid
# print(f"{number} : last digit is {number % 10}") this is good enough


# Example 5 : Write a program to check if a person is eligible for discount the criteria is he must be a student and age must be below 21
# age = int(input("Enter age : "))
# role = input("Enter role (student, teacher): ")
# print("Eligible : ", age < 21 and role == "student")


# Example 6 : Write a program to swap two variables without a third variable, using arithmetic operations.
