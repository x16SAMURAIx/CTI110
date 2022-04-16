item1 = float(input('\nEnter the price for item 1 $'))
item2 = float(input('\nEnter the price for item 2 $'))
item3 = float(input('\nEnter the price for item 3 $'))
item4 = float(input('\nEnter the price for item 4 $'))
item5 = float(input('\nEnter the price for item 5 $'))

subtotal = float(item1 + item2 + item3 + item4 +item5)

SALES_TAX = 0.07

total_sales_tax = subtotal * SALES_TAX

total = subtotal + total_sales_tax

print('-------Results-------')
print('Subtotal: $', format(subtotal, ',.2f'), sep='', end='\n\n')
print('Sales Tax: $', format(total_sales_tax, ',.2f'), sep='', end='\n\n')
print('Total: $', format(total, ',.2f'), sep='', end='\n\n')
