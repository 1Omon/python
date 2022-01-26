from createAccount import createAccount
from logInAccount import *
# asking for username and sending a welcome message
userName = str(input("Your name - "))

welcomeMsg = f"Hey {userName}"

print(welcomeMsg)

# Options available
createAcc = "Create an Account"
loginAcc = "Log into my account"
aboutBank = "About Bank"
bankServices = "Our Services"
missionStatement = "Our Mission"
changeCredentials = "Change username or password"

print('\n')  # line-breaks
print('Choose the action you want to perform \n')
popUp1 = print('1.'+createAcc + '\n' + '2.'+loginAcc+'\n' + '3.'+aboutBank+'\n' +
               '4.'+bankServices + '\n' + '5.'+missionStatement + '\n' + '6.'+changeCredentials)

print('\n')  # line-breaks
userResponse1 = int(input("Your request - "))
if userResponse1 == 1:
    createAccount()
elif userResponse1 == 2:
    login()
elif userResponse1 == 3:
    print()
elif userResponse1 == 4:
    print()
elif userResponse1 == 5:
    print()
elif userResponse1 == 6:
    print()
else:
    print("Choose one of the above options")