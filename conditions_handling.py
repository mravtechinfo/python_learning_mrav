# Your code needs to have the ability to take different action based on different conditions

price_of_product = int(input('Enter the price of product you bought '))

if price_of_product>=10:
    tax = 0.7
    print('Tax rate is: '+str(tax))
else:
    tax=0
    print('Tax rate is: '+str(tax))
