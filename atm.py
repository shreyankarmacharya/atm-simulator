pin = "1234"
balance = '1000'
failed = 0
history = []


def atm():
    global balance
    print("""
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
""")
    while True:
        while True:
            userinput = input("Enter the action you wanna perform: ")

            if userinput.isdigit():
                userinput = int(userinput)
                break
            else:
                print("Invalid action")

        match userinput:

            case 1:
                print(balance)
                history.append("Checked balance")

            case 2:
                depo = input("Enter the amount you wanna deposit: ")
                if depo.isdigit() and int(depo) > 0:
                    balance = str(int(balance) + int(depo))
                    history.append("Deposited " + depo)
                else:
                    print('Invalid amount, make sure the deposit amount is greater than 0')

            case 3:
                withdraw = input('Enter the amount you wanna withdraw: ')
                if withdraw.isdigit():
                    withdraw = int(withdraw)
                    if withdraw > int(balance):
                        print("Insufficient balance")
                    if withdraw < int(balance) and withdraw > 0:
                        balance = str(int(balance) - withdraw)
                        history.append("Withdrew " + str(withdraw))
                    elif withdraw <= 0:
                        print('Invalid amount')
                else:
                    print("Invalid amount")

            case 4:
                for x in range(len(history)):
                    print(history[x])

            case 5:
                print("Are you sure you want to exit?")
                confirm = input("Type 'y' to exit and 'n' to cancel: \n")
                if confirm.lower() == 'y':
                    break

            case _ if userinput > 5:
                print("Invalid action")


input("Enter your account number: ")  # for realism

while True:
    entered_pin = input("Enter your account pin: ")
    if entered_pin == pin:
        atm()
        break
    else:
        failed = failed + 1
        print("Wrong pin entered. Please try again.")
        if failed == 3:
            print('')
            print('Wrong pin entered 3 times.')
            print('')
            print('Exiting system')
            break
