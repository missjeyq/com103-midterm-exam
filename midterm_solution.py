category_names    = ["Food & Drinks", "Transportation", "Mobile / Internet", "School Supplies", "Entertainment"]
category_examples = ["Lunch, snacks, coffee", "Bus, jeepney, ride-share", "Load, data plan, WiFi top-up", "Notebook, pen, bond paper", "Games, movies, hangout"]
 
valid = False
while valid == False:
    student_name = input("Student Name: ")
    i = 0
    is_valid = True
    if student_name == "":
        is_valid = False
    while i < len(student_name):
        char = student_name[i]
        if char != " ":
            if char < "A" or (char > "Z" and char < "a") or char > "z":
                is_valid = False
        i = i + 1
    if is_valid == True:
        valid = True
    else:
        print("  Invalid, try again.")
 
valid = False
while valid == False:
    weekly_budget_input = input("Weekly Budget: ")
    i = 0
    is_valid = True
    if weekly_budget_input == "":
        is_valid = False
    while i < len(weekly_budget_input):
        char = weekly_budget_input[i]
        if char < "0" or char > "9":
            is_valid = False
        i = i + 1
    if is_valid == True and int(weekly_budget_input) > 0:
        weekly_budget = float(weekly_budget_input)
        valid = True
    else:
        print("  Invalid, try again.")
 
print()
print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
i = 0
while i < 5:
    print(" " + str(i + 1) + ". " + category_names[i].ljust(22) + " [e.g. " + category_examples[i] + "]")
    i = i + 1
print("==========================================")
 
logged_seq          = []
logged_categories   = []
logged_descriptions = []
logged_amounts      = []
logged_is_high      = []
 
high_expense_limit = weekly_budget * 0.25
total_spent        = 0
seq_num            = 0
 
entry = 1
while entry <= 4:
    print()
    print("--- EXPENSE " + str(entry) + " ---")
 

    valid = False
    while valid == False:
        category_input = input("Category (0 to skip): ")
        i = 0
        is_valid = True
        if category_input == "":
            is_valid = False
        while i < len(category_input):
            char = category_input[i]
            if char < "0" or char > "9":
                is_valid = False
            i = i + 1
        if is_valid == True:
            if int(category_input) >= 0 and int(category_input) <= 5:
                category_num = int(category_input)
                valid = True
            else:
                print("  Invalid, try again.")
        else:
            print("  Invalid, try again.")
 
    if category_num == 0:
        entry = entry + 1
        continue
 
    
    valid = False
    while valid == False:
        description = input("Description: ")
        i = 0
        is_all_digits = True
        if description.strip() == "":
            is_all_digits = True
        else:
            while i < len(description.strip()):
                char = description.strip()[i]
                if char < "0" or char > "9":
                    is_all_digits = False
                i = i + 1
        if description.strip() == "" or is_all_digits == True:
            print("  Invalid, try again.")
        else:
            valid = True
 
    
    valid = False
    while valid == False:
        amount_input = input("Amount: ")
        i = 0
        is_valid = True
        if amount_input == "":
            is_valid = False
        while i < len(amount_input):
            char = amount_input[i]
            if char < "0" or char > "9":
                is_valid = False
            i = i + 1
        if is_valid == True and int(amount_input) > 0:
            amount = float(amount_input)
            valid = True
        else:
            print("  Invalid, try again.")
 
    if amount > high_expense_limit:
        is_high = True
    else:
        is_high = False
 
    seq_num = seq_num + 1
 
    logged_seq.append(seq_num)
    logged_categories.append(category_names[category_num - 1])
    logged_descriptions.append(description)
    logged_amounts.append(amount)
    logged_is_high.append(is_high)
 
    total_spent = total_spent + amount
 
    entry = entry + 1
 
remaining = weekly_budget - total_spent
 
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."
 
print()
print("======================================================")
print("     " + student_name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")
print("  Weekly Budget  : P" + format(weekly_budget, ".2f"))
 
i = 0
while i < seq_num:
    if logged_is_high[i] == True:
        flag = "  ! High Expense Alert!"
    else:
        flag = ""
    print("  [" + str(logged_seq[i]) + "] " + logged_categories[i])
    print("      " + logged_descriptions[i].ljust(36) + " P" + format(logged_amounts[i], ".2f") + flag)
    i = i + 1
 
print("------------------------------------------------------")
print("  Total Spent    : P" + format(total_spent, ".2f"))
print("  Remaining      : P" + format(remaining, ".2f"))
print("  Status         : " + status)
print("======================================================")
