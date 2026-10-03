# Expense Tracker - Installment 3
# Author: ELYSSA NICOLE J. APARICIO
# A simple landing page for a personal expense tracker.

print("=" * 40)
print ("\tEXPENSE TRACKER")
print ("\tKnow where your money goes.")
print ("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Lets log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total


print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}: \t${amount1}")
print(f"\t- {item2}: \t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print("Made by: ELYSSA NICOLE J. APARICIO | Installment 3")
