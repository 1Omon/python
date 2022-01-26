from bankingBot import *

def createAccount():
    firstName = str(input("Enter your first name - "))
    middleName = str(input("If any, enter your middle name(s) - "))
    lastName = str(input("Enter your last name - "))
    DoB = input("Enter your date of birth (dd/mm/yyyy)- ")
    while len(DoB) != 10:
        print("date of birth syntax not obeyed \n")
        DoB = input("Enter your date of birth (dd/mm/yyyy)- ")
    if (DoB[2] == '/') and (DoB[5] == '/') and (len(DoB[6:]) == 4):
        if (DoB[0:2] > '31') or (DoB[0:2] <= '0'):
            print("day (dd) not in required range")
        elif (DoB[3:5] <= '0') or (DoB[3:5] > '12'):
            print("month of birth(mm) not in range")
        elif (DoB[6:10] > '2021') or (DoB[6:10] < '1920'):
            print("year(yyyy) is not valid")
    else:
        print("Date format invalid.")
        DoB = input("Enter your date of birth (dd/mm/yyyy)- ")
        
    Id_Type = int(input("Select from below \n 1.National Id card \n 2. Driver's license \n 3. Voter's card \n 4. Passport card \n Your option - "))
    if (Id_Type <= 0) or (Id_Type > 4):
        print("Option not found. Try Again!!")
        Id_Type = int(input("Select from below \n 1.National Id card \n 2. Driver's license \n 3. Voter's card \n 4. Passport card \n Your option - "))

    else:
        if Id_Type == 1:
            Id_Type = 'National Id card'
            Id_Number = input("Enter your card id number. (GHA-XXXXXXXXXX-X)")
            if (len(Id_Number) == 16) and (Id_Number[0:3] == 'GHA') and (Id_Number[3] == '-') and (Id_Number[14] == '-') and (Id_Number[15] > '0' and Id_Number[15] < '10') :
                print("correct. next")
            else: 
                Id_Number = input("Enter your card id number. (GHA-XXXXXXXXXX-X)")
        elif Id_Type == 2:
            Id_Type = "Driver's license"
            Id_Number = str(input("Enter your card id number. (XXXXXXXXXXXX)"))
        elif Id_Type == 3:
            Id_Type = "Voter's card"
            Id_Number = str(input("Enter your card id number. (XXXXXXXXXX)"))
        elif Id_Type == 4:
            Id_Type = "Passport card"
            Id_Number = str(input("Enter your card id number. (GXXXXXXXX)"))
        else:
            print("Couldn't validate inputs")
    occupation = str(input("Your occupation - "))
    verifyOccupation = occupation.split()
    for i in verifyOccupation:
        if type(i) is int:
            print("enter a valid occupation")
    user = accountCreation(firstName, middleName, lastName, DoB, Id_Type, Id_Number, occupation)
    user_details = user.details()
    print(user_details)
        #aing user to check if input details are valid or correct
        #ithey are valid, user has to create a 4-digit pin and confirm that pin to be used as his pin when logging into his account
    confirmation = str(input("Y or N - "))
    if (confirmation == 'Y') or (confirmation == 'y'):
        print(" \n Congratulations!!! Your account has been created successfully. \n")
        create_pin = int(input("enter a 4-digit number as your pin - "))
        confirm_created_pin = int(input("re-enter pin to confirm - "))
        #setting the pin as the user's secret pin 
        if create_pin == confirm_created_pin:
            secret_pin = create_pin
            pin_set_msg = f"PIN SET SUCCESSFULLY"
            print('\n' + pin_set_msg)
            #else making user enter a pin until they can confirm it
        else:
            print("Entered pins do not match, TRY AGAIN")
            while create_pin != confirm_created_pin:
                create_pin = int(input("enter a 4-digit number as your pin - "))
                confirm_created_pin = int(input("re-enter pin to confirm - "))

        
    ######if inputs are not valid, 
    elif (confirmation == 'N') or (confirmation == 'n'):
        print("please start the process again with correct or valid details")
    #####if user enters an option which wasn't included
    else:
        print("Input is not valid!")
        



class accountCreation:
    def __init__(self, firstName, middlieName, lastName, DoB, Id_Type,  Id_Number, occupation, ):
        self.firstName = firstName
        self.middleName = middlieName
        self.lastName = lastName
        self.DoB = DoB
        self.Id_Type = Id_Type
        self.Id_Number = Id_Number
        self.occupation = occupation
    def details(self):
        print('\n')
        print("Name : " + self.firstName + ' ' +self.middleName + ' ' + self.lastName)
        print("Date of Birth : " + self.DoB)
        print("Identification card type : " , self.Id_Type)
        print("Identification card number : " + self.Id_Number)
        print("Occupation : " + self.occupation)
        print("Do you agree that the following details are correct? \n if 'yes', enter 'y' or else enter 'n'")

        