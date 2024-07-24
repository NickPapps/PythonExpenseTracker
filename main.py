expenses = [] 
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1) 
expense2 = {'amount': '21.55', 'category': 'groceries'}
expenses.append(expense2) 

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)  

def removeExpense():
    while True:
        listExpense()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove] 
            break
        except:
            print("Invalid input. Please try again.")

def printMenu():
    print("Please choose from one of the options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")
    
def listExpense():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    counter = 0
    for expense in expenses: 
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")


# Main Method
if __name__ == "__main__":
    while True:
        ### Prompt the user
        printMenu()
        optionSelected = input("> ")

        if(optionSelected == "1"):
            print("How much was this expense?")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                    print("Invalid input. Please try again.")    
            
            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("invalid input. Please try again.")
            addExpense(amountToAdd, category)
        elif(optionSelected == "2"):
            removeExpense()
        elif(optionSelected == "3"):
            listExpense()
        else:
            print("Invalid input. Please try again.")
            
                