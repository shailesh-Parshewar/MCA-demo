# Functions 
# Syntax
# # Non-parameterized function
# def function_name():
#     Statements to execute upon calling this function

# # Parameterized function
# def function_name(param):
#     Statements to execute upon 

# # Example 1: function to add two numbers and print it.
# def add(param1, param2):
#     print(f"sum ting wong : {param1 + param2}")

# add(3,4)
# add(90,4)

# # Example 2 : return the sum of two numbers
# def add(n1, n2):
#     return n1 + n2

# add(34,3)
# print(add(34,3))

# # Example 3 : Default parameter values
# def name(name="student"):
#     print(f"hello {name}")

# name("shailesh")
# name()

# # Example 4 : Calculator function
# def calc(n1 = 1, op = "", n2 = 1):
#     match op:
#         case "+":
#             print(f" {n1} {op} {n2} : {n1+n2}")
#         case "-":
#             print(f" {n1} {op} {n2} : {n1-n2}")
#         case "+":
#             print(f" {n1} {op} {n2} : {n1*n2}")
#         case "+":
#             print(f" {n1} {op} {n2} : {n1/n2}")
#         case "":
#             print("no op provided")
#         case _:
#             print("invalid op")


# calc()
# calc(12,"+",12)

# # Recursion
# def func(n):
#     print("n :: ", n)
#     if n > 0:
#         func(n-1)
    
# func(123)

# # Example 5 : factorial
# def factorial(n):
#     if n > 1:
#         return n * factorial(n-1)
#     else:
#         return 1
# print(factorial(0))

# # lambda functions
# square = lambda n : n*n
# print(square(25))