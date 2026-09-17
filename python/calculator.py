# Example 9 : create a simple calculator

while True:

    op = input("enter an operation to perform(+,-,*,/,%,!,Exit) : ")
    # checking if user entered Exit command
    if op == "Exit":
        print("Exiting calculator")
        break
    # check if user selected factorial as op
    a = int(input("enter number a : "))
    if op == "!":
        temp = 1
        while a > 1:
            temp *= a
            a -= 1
            
        print(f"Factorial : {temp}")
        continue

    b = int(input("enter number a : "))

    # Basic ops match at last
    match op:
        case "+":
            print("a plus b : ", a + b)
        case "-":
            print("a minus b : ", a - b)
        case "*":
            print("a multiplied by b : ", a * b)
        case "/":
            if b == 0:
                print("error : division by zero")
            else:
                print("a divided by b : ", a / b)
        case "%":
            print("remainder of a divided by b : ", a % b)
        case _:
            print("invalid op")