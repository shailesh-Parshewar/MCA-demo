# While loop

# Example 1 : Infinite loop
while True:
    string = input("Input a string : ")
    print(string)

# Example 2 : conditional while
correct_pass = "pass"
loop_condition = True
while loop_condition:
    string = input("Write a password : ")
    if string == correct_pass:
        loop_condition = False
    else:
        print("Wrong password")
print("Password matched")

# Example 3 : print i at the end of a loop
i = 0
while i < 10:
    i += 1 
print("i at end of loop : ", i)

# Example 4 
i = 1
even = 0
up = int(input("upper range : "))
while i < up:
    if i % 2 == 0:
       even += 1
    i += 1
print(even)

# Example 5
n = int(input("enter a number : "))
i = 1
while i <= 10:
    print(n*i)
    i+=1

# Example 6 : print if a number is prime
n = int(input("Enter a number : "))
i = 2
not_prime = False
while i < n:
    if n % i == 0:
        not_prime = True
        break
    i +=1
print("is prime : ", not not_prime)
