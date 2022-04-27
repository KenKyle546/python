# User input
price_child = float(input("What is the price of a child's meal? $"))
price_adult = float(input("What is the price of an adult's meal? $"))
count_child = int(input("How many children are there? "))
count_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

# Variable calculations
subtotal = (price_child * count_child) + (price_adult * count_adult)
sales_tax = (tax_rate / 100) * subtotal
total = subtotal + sales_tax

# Display totals
print(f"""
Subtotal: ${subtotal:.2f}
Sales Tax: ${sales_tax:.2f}
Total: ${total:.2f}
""")

#Tip Calculator
tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.2

print(f"""For your convenience:
15%: ${tip_15:.2f}
18%: ${tip_18:.2f}
20%: ${tip_20:.2f}
""")

tip = float(input("Please enter tip amount: "))
new_total = float(total + tip)
print(f"New Total: ${new_total:.2f}\n")

# Payment
pmt = float(input("What is your payment amount? "))
change = pmt - new_total
print(f"Change: ${change:.2f}")
