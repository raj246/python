# elif if else statements

balance = input("What is your bank balance?")
if int(balance) <=0:
    print("would you like to  make a deposit.")
elif int(balance) <=50:
    print("your are not eligible for interest.")
elif int(balance) <100:
    print("Your are eligible for 1% interest.")
else:
    print("your are eligible for 2% interest")

