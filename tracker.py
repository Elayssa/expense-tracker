# Expense Tracker - Installment 2
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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}: \t${amount1}")
print(f"\t- {item2}: \t${amount2}")
print(f"Total spent: \t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print("Made by: ELYSSA NICOLE J. APARICIO | Installment 2")
