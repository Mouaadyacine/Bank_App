import random
dicAccount_Balance = {}
dicClient_Password = {}
dicClient_AccountNumber = {}

currentClientNumber =0

class clsBankEmp:
    clientsCount = 0
    def addClient():
        clsBankEmp.clientsCount +=1
        clientNumber = str(clsBankEmp.clientsCount )
        
        dicAccount_Balance[clientNumber] = "0"
        
        dicClient_Password[clientNumber] = "1234@"

        accountNumber = int(clientNumber) * 100 + random.randint(0,100)
        dicClient_AccountNumber[clientNumber] = str(accountNumber)
    
    def DeleteClient(clientNumber):
        if clsBankClient.isClientFound(clientNumber) :
            del dicAccount_Balance[clientNumber]
            del dicClient_AccountNumber[clientNumber]
            del dicClient_Password[clientNumber]
            return True
        else:
            return False
    def showClients():
        print("Clients NUMBERS/BALANCES")
        print(dicAccount_Balance)

        print("Clients NUMBERS/ACCOUNT NUMBERS")
        print(dicClient_AccountNumber)

        print("Clients NUMBERS/PASSWORDS")
        print(dicClient_Password)
class clsClientMenu:
   
    def performOption(self,opt):
        if opt == "1":
            newPass = input("enter new password : ")
            clsBankClient.updatePassword(newPass)
            print("password updated successfully")
        elif opt == "2":
            amount = int(input("enter amount to deposit : "))
            clsBankClient.deposit(amount)
            print("amount updated successfully")
        elif opt == "3" :
            amount = int(input("enter amount to withdraw : "))
            if clsBankClient.withDraw(amount):
                print("amount updated successfully")
            else:
                print("you cant enough money")
        else :
            print("wrong input!!")

    def showMenu(self):
        print("     MODIFIER PASSWORD [1]         ")
        print("     DEPOSER AMOUNT    [2]         ")
        print("     RETIRER AMOUNT    [3]         ")
        num = str(input("what is you choice : "))
        self.performOption(num)

class clsEmpMenu:
    def showMenu():
        print("     AJOUTER CLIENT     [1]          ")
        print("     SUPRIMER CLIENT    [2]          ")
        print("     SEE CLIENTS        [3]          ")
        num = input("what is you choice : ")
        clsEmpMenu.choice(num)

    def choice(opt):
        if opt == "1":
            clsBankEmp.addClient()
            print("adding client successfully")
        elif opt == "2":
            clientToDel = input("enter client number to delete : ")

            if clsBankEmp.DeleteClient(clientToDel):
                print("deleted client successfully")
            else:
                print("client nmuber was not found")
        elif opt=="3":
            clsBankEmp.showClients()
        else :
            print("wrong input!!")

class clsBankClient:

    def isClientFound(clientNum):
        for k in dicClient_Password.keys():
            if k == clientNum :
                return True
        
        return False
    def CheckClientInfo(clientNum, password):
        for k,v in dicClient_Password.items():
            if k == clientNum and v == password:
                return True
        return False
     
    
    
    def updatePassword(NewPassword):
        dicClient_Password[str(currentClientNumber)] = NewPassword
    
    def deposit(Amount):
        oldAmount = int(dicAccount_Balance[str(currentClientNumber)]) 
        dicAccount_Balance[str(currentClientNumber)] =str( oldAmount + Amount)

    def withDraw(Amount):
        oldAmount = int(dicAccount_Balance[str(currentClientNumber)] )
        if Amount < oldAmount:
            dicAccount_Balance[str(currentClientNumber)] = str(oldAmount + Amount)
            return True
        else :
            return False

while(True):
    print("are you a Client [1] or Employer [2]..")
    opt =input("enter a choice : ")
    if opt == "1":
        Number =int(input("enter client number: "))
        Password =input("enter client password :")
        if clsBankClient.CheckClientInfo(str(Number),str(Password)):
            currentClientNumber = Number
            menu = clsClientMenu()
            menu.showMenu()   
        else:
            print("Wrong info!!!")
    elif opt =="2":
        clsEmpMenu.showMenu()
    else:
        print("wrong input!!!")