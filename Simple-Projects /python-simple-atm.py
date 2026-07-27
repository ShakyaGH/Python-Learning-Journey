#Simple ATM Machine Project
choice_list = [1,2,3,4]
balance = 10000
while True:
    print("ATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter : "))
    if choice not in choice_list:
        print("Not Valid input,Try again")
        continue
    else:
        if choice == 1:
            print(f"Your account balance is {balance}")
        elif choice == 2:
            deposit = int(input("Enter how much do you want to deposit: "))
            if deposit <= 0:
                print("Enter a valid value to deposit")
                continue
            balance += deposit
            print("Please wait, Your request is processing: ")
            print(f"Your new account balance is {balance}")
        elif choice == 3:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw > balance :
                print("Insufficient Balance")
            elif withdraw <= 0:
                print("Can't make the process please try again")
                continue            
            else:
                balance -= withdraw
                print(f"Your existing balance is {balance}")            
        else:
            print("Thank you for banking with us,Have a nice day & Come again")
            exit()
