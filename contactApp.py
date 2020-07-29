
import pickle 
import os 
###############################################################################
class Contact:
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, name, number):
        self.name = name 
        self.number = number 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
    def getName(self):
        return self.name 
   
    def getNumber(self):
        return self.number 
     
    def setName(self, name):
        self.name = name 
    
    def setNumber(self, number):
        self.number = number 

    def createContact(namey, numbery):
        return Contact(namey, numbery)

###############################################################################

###############################################################################
class mobilePhone:

    def __init__(self):
        self.myContacts = []

    def add(self):
        print("What's your contacts name? ")
        contactName = input()
        contactName = contactName.strip()
        print("What is " + contactName + "'s phone number?")
        contactNumber = input()
        contactNumber = contactNumber.strip()
        self.myContacts.append(Contact.createContact(contactName,contactNumber))
        print("Exemplary! " + contactName + " with phone number " + contactNumber + " \n was added to contacts! ")

    def indexOfName(self, aName):
        for i in self.myContacts:
            if(aName == i.getName()):
                return i 

    def indexOfNumber(self, aNum):
        for i in self.myContacts:
            if(aNum == i.getNum()):
                return i 

    def findContactName(self, findMe):
        for i in self.myContacts:
            if(findMe == i.getName()):
                return 1
            else:
                return -1

    def searchContacts(self):
        print("For whom do you search?")
        findMe = input()
        findMe = findMe.strip()
        if(self.findContactName(findMe)==-1):
            print("Sorry, we failed to find " + findMe + " :( ")
        elif(self.findContactName(findMe) == 1 ):
            print(findMe + " was found!")
            print("info => " + findMe + " : " + self.indexOfName(findMe).getNumber())

    def findContactNumber(self, findMe):
        for i in self.myContacts:
            if(findMe == i.getNumber()):
                return 1
            else:
                return -1
        
    def showContacts(self):
        for i in self.myContacts:
            print(str(i.getName()) + " : " + str(i.getNumber()))

    def editContacts(self):
        looper = True 
        while(looper):
            nestedLooper = False 
            print("Do you want to edit a name (enter 0 ) or number (enter 1) ?")
            userChoice = int(input().strip())
            while(nestedLooper==False):
                if(userChoice == 0):
                    self.nameChange()
                    nestedLooper = True 
                    looper = False 
                elif(userChoice == 1):
                    self.numberChange()
                    nestedLooper = True 
                    looper = False 
                else:
                    print("oops")
                    nestedLooper = True

    def nameChange(self):
        print("Who's name do you want to change?")
        changeMe = input().strip()
        if(self.findContactName(changeMe)==1):
            print("What do you want " + changeMe + "'s new name to be?")
            newName = input()
            self.indexOfName(changeMe).setName(newName)
            print("Mission success! What was " + changeMe + " is now " + "newName")
        elif(self.findContactName(changeMe) == -1):
            print("Many Apologies, we couldn't find " + changeMe + "....(*sadFace*)...")

    def numberChange(self):
        print("Who's number do you want to change?")
        changeMe = input().strip()
        if(self.findContactName(changeMe)==1):
            print("What do you want " + changeMe + "'s new number to be?")
            newNum = input()
            self.indexOfName(changeMe).setNumber(newNum)
            print("Exemplary! " + changeMe + "'s number is now " + newNum)
        elif(self.findContactName(changeMe)== -1):
            print("There is no " + changeMe + " :( ")

    def deleteContact(self):
        print("Which contact do you want to be rid of?")
        deleteMe = input().strip()
        if(self.findContactName(deleteMe) == 1):
            self.myContacts.remove(self.indexOfName(deleteMe))
            print("Success! " + deleteMe + " was removed from your contacts")
        elif(self.findContactName(deleteMe)==-1):
            print("Hmmmm... looks like you don't have a " + deleteMe + " in your Contacts :/ ")


    def saveContacts(self):
        with open('outfile', 'wb') as fp:
            pickle.dump(self.myContacts, fp) 

    def load(self):
        if(os.path.isfile("C:/Users/austb/OneDrive/Documents/JUSTCODE/contactApp/outfile")):
            with open('outfile', 'rb') as fp:
                self.myContacts = pickle.load(fp)
        else:
            print("Didn't find ya a file to load")


def printMenu():
    print("**************************************************************************")
    print("OPTIONS \n 0. Show Options \n 1. Add a Contact \n 2. Search Contacts " +
                "\n 3. Show Contacts \n 4. Edit a Contact \n 5. Delete a Contact \n 6. Done ")
    print("***************************************************************************")

   
###############################################################################

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                               PROGRAM ENTRY 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

flag = True 

thisPhone = mobilePhone()
thisPhone.load()
printMenu()

while(flag):
    flag2 = False 
    userChoice = int(input().strip())
    while(flag2 == False):
        if(userChoice == 0):
            printMenu()
            flag2=True 
        elif(userChoice==1):
            thisPhone.add()
            flag2=True
        elif(userChoice==2):
            thisPhone.searchContacts()
            flag2=True 
        elif(userChoice==3):
            thisPhone.showContacts()
            flag2=True
        elif(userChoice==4):
            thisPhone.editContacts()
            flag2=True
        elif(userChoice==5):
            thisPhone.deleteContact()
            flag2=True
        elif(userChoice==6):
            thisPhone.saveContacts()
            print("Later Vader")
            flag = False 
            flag2 = True 
        
