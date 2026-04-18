category_names    = ["Food & Drinks", "Transportation", "Mobile / Internet", "School Supplies", "Entertainment"]
category_examples = ["Lunch, snacks, coffee", "Bus, jeepney, ride-share", "Load, data plan, WiFi top-up", "Notebook, pen, bond paper", "Games, movies, hangout"]
 
student_name  = input("Student Name: ")
weekly_budget = float(input("Weekly Budget: "))
 
print()
print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
i = 0
while i < 5:
    print(" " + str(i + 1) + ". " + category_names[i].ljust(22) + " [e.g. " + category_examples[i] + "]")
    i = i + 1
print("==========================================")
 
logged_seq         = []
logged_categories  = []
logged_descriptions= []
logged_amounts     = []
logged_is_high     = []
 
high_expense_limit = weekly_budget * 0.25
total_spent        = 0
seq_num            = 0
 
entry = 1
while entry <= 4:
    print()
    print("--- EXPENSE " + str(entry) + " ---")
    category_num = int(input("Category (0 to skip): "))
 
    if category_num == 0:
        entry = entry + 1
        continue
 
    if category_num >= 1 and category_num <= 5:
        description = input("Description: ")
        amount      = float(input("Amount: "))
 
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
 