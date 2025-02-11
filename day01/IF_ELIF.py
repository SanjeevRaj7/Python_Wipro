#real world example
choice=int(input("1.CHECK BALANCE 2.DEPOSIT 3.WITHDRAW:"))
balance=5000
if choice == 1:
    print("balance of your account:",balance)
elif choice == 2:
    amt=int(input("enter amount to deposit:"))
    amt+=balance
    print("Your balance is:",amt)
elif choice == 3:
    amt=int(input("enter amount to withdraw:"))
    amt-=balance
    print("Your balance is:",amt)
else:
    print("exit"+"\n"+"enter correct choice")







