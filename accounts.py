user= input("please enter acount number of any length:")
account = user[-4:].rjust(len(user), 'X')
print("your account number is: ",account)


# https://stackoverflow.com/questions/45229343/program-in-python-that-will-prompt-the-user-to-enter-an-account-number-consists
