user= input("please enter acount number of any length:")
account = user[-4:].rjust(len(user), 'X')
print("your account number is: ",account)


