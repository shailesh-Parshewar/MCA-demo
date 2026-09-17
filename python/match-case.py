# Match case statement
n = int(input("Enter a number : "))
match n:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid choice")



# Example 10 : Traffic signal
 a = input("Enter a signal(Red, Yellow, Green) : ")
 match a:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Get ready")
    case "Green":
        print("Go")
    case _:
        print("Invalid color")

# Example 11: ATM Menu
balance = int(input("Enter your balance : "))

while True:
    action = input("Enter an action(Withdraw, Deposit, Check Balance, Exit) : ")
    match action:
        case "Withdraw":
            amt = int(input("Enter amount to withdraw : "))
            if amt > balance:
                print("Amt is invalid: (Code : Amt is bigger than remaining balance)")
            else:
                balance = balance - amt
                print("Remaining balance : ", balance)
        case "Deposit":
            amt = int(input("Enter amt to deposit : "))
            balance =+ amt
            print("New Balance is : ", balance)
        case "Check Balance":
            print("Your Balance is : ", balance)
        case "Exit":
            break
        case _:
            print("Invalid action : (Code : Action not recognized)")