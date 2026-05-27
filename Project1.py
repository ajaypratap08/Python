print("Expense Tracker")
expenses = []
while(True):
    print("\n=========== MENU ===============")
    print("Opt 1 -> Add Expense")
    print("Opt 2 -> View Expense")
    print("Opt 3 -> Total Expense")
    print("Opt 4 -> Exit")
    try:
        opt = int(input("Enter your option- "))
    except:
        print("Please enter a valid number!")
        continue
    if(opt == 1):
        print("\nEnter Expense Details")
        category = input("Ab kha karcha kar diye bc- ")
        amount = float(input("Kitna paisa udha diya mc- "))
        date = input("Konse din kiya ye- ")
        expense_data = {
            "category": category,
            "amount": amount,
            "date": date
        }
        expenses.append(expense_data)
        print("Expense add ho gaya bhai!")
    elif(opt == 2):
        if(len(expenses) == 0):
            print("No expenses found!")
        else:
            print("\n======= All Expenses =======")
            for expense in expenses:
                print("----------------------")
                for key, value in expense.items():
                    print(key, ":", value)
    elif(opt == 3):
        if(len(expenses) == 0):
            print("No expenses found!")
        else:
            total = 0
            for expense in expenses:
                total += expense["amount"]
            print("Total Expense =", total)
    elif(opt == 4):
        print("Exiting...")
        break
    else:
        print("Invalid Option!")