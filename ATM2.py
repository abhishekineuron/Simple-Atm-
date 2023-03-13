def display_balance(balance):
    print("Your balance is: ${:.2f}".format(balance))

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds!")
    elif amount < 0:
        print("Invalid amount!")
    else:
        balance -= amount
        print("Withdrawal successful. New balance: ${:.2f}".format(balance))
    return balance
1
def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    if amount < 0:
        print("Invalid amount!")
    else:
        balance += amount
        print("Deposit successful. New balance: ${:.2f}".format(balance))
    return balance

def main():
    balance = 10000
    while True:
        print("  ATM  ")
        print("1. Check balance")
        print("2. Withdraw funds")
        print("3. Deposit funds")
        print("4. Quit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        if choice == 1:
            display_balance(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            balance = deposit(balance)
        elif choice == 4:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
