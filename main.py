# prompts the user to enter the price for 5 individual items.
item_1 = float(input("Enter the price of the first item: $ "))
item_2 = float(input("Enter the price of the second item: $ "))
item_3 = float(input("Enter the price of the third item: $ "))
item_4 = float(input("Enter the price of the fourth item: $ "))
item_5 = float(input("Enter the price of the fifth item: $ "))

# calculating the subtotal of the  items.
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
print(f"The subtotal for the five items is: $ {subtotal:.2f}")

# calculating the sales tax.
# an assumption is we take each item to have a 6% tax rate.
sales_tax = subtotal * 0.06
print(f"The sales tax is: $ {sales_tax:}")

total_value = subtotal + sales_tax
print(f"The total cost of the items is: $ {total_value:}")
