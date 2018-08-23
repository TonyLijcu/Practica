Number_of_items = int(input("Number of items:"))
total = 0
while Number_of_items < 0:
    print("Invalid number of items!")
    Number_of_items = int(input("Number of items:"))
for i in range(Number_of_items):
    price = float(input("Price of item:"))
    total += price

if total > 100:
    total = total * 0.9

print("Total price for", Number_of_items, "items is", total, "$")
