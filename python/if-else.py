# Conditions
# if-else statements

if condition_true:
  do this
else:
  do this

# Example 1
is_raining = True
if is_raining:
    print("Raining outside")
else:
    print("Not raining")

# Example 2
age = int(input("Enter age : "))
if age > 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Example 3
number = int(input("enter a number : "))

if number == 1:
    print("Sunday")
elif number == 2:
    print("Monday")
elif number == 3:
    print("Tuesday")
elif number == 4:
    print("Wednesday")
elif number == 5:
    print("Thursday")
elif number == 6:
    print("Friday")
elif number == 7:
    print("Saturday")
else:
    print("Invalid input")


#  Example 4 : Check if a number is odd or even using if-else statement
n = int(input("Enter a number : "))
if(n % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")




# Example 5 : add a 20% discount to ticket price if age is less than 12 age < 12
age = int(input("Enter age : "))
ticket_price = int(input("Enter a ticket price : "))
if age < 12:
    print("Original ticket price : ", ticket_price)
    print("(Discount of 10%)")
    print("New Ticket price : ", ticket_price - (ticket_price/10))
else:
    print("Original Ticket price : ", ticket_price)
    print("(Discount 0%)")
    print("New Ticket price : ", ticket_price)

# Example 6: Grade user based on input
m = int(input("Enter marks : "))
if m >= 90 and m < 100:
    print("Grade O")
elif m >= 80 and m < 90:
    print("Grade A")
elif m >= 65 and m < 80:
    print("Grade B")
elif m >= 35 and m < 65:
    print("Grade C")
elif m >= 0 and m < 35:
    print("Grade F")
else:
    print("Invalid input")

if m > 100:
    print("invalid")
elif m >=90:
    print("Grade O")
elif m >= 80:
    print("Grade A")
elif m >= 65:
    print("Grade B")
elif m >= 35:
    print("Grade C")
elif m >= 0:
    print("Grade F")
else:
    print("Invalid")

# Example 7 : Check if a number is positive or negative
n = int(input("Enter a number : "))
if n == 0:
    print("Number is zero")
elif n > 0:
    print("Number is positive")
else:
    print("Number is negative")

# Example 8 : Print the biggest of three inputs
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if a == b and a == c:
    print("all three are equal")
elif a > b:
    if a > c:
        # a > b, a > c
        print("a is greatest")
    elif a == c:
        print("a and c are greater than b")
    else:
        # a > b, c > a
        print("c is greatest")
elif b > c:
    #   b > c, b < or == a
    if b == a:
        print("b and a are greater than c")
    else:
        print("b is greatest")
else:
    # b < a, b < or == c
    if b == c:
        print("b and c are greater than a")
    else:
        print("c is greatest")

# Example 8 : calculate if a year is leap year
y = int(input("year : "))

if y % 400 == 0:
    print("leap year")
elif y % 100 == 0:
    print("not leap year")
elif y % 4 == 0:
        print("leap year")
else:
    print("not leap year")
