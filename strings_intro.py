#String basic done

#first_name = 'Anubhav'
#last_name = 'Miller'
first_name=input('Enter your first name: ')
last_name=input('Enter your last name: ')

#print the name with space between
print (first_name + ' ' + last_name)

#lower method 
print('hello lowercase'+' ' + first_name.lower()+' '+ last_name.lower())

# upper method
print('hello uppercase'+' ' + first_name.upper()+' '+ last_name.upper())
#String Formatting

# combine string with +
# custom String formatting



# output = 'Hello, '  + first_name + ' ' + last_name
#lets do the same task with other ways ie printing the output varible

# output = 'Hello, {} {}'.format(first_name,last_name)
# output = 'Hello, {0} {1}'.format(first_name,last_name)
output = f'Hello, {first_name}{last_name}'  # This can only be done in python3 specifically
print(output)