province =  input('From which province are you from ?')
province=province.lower()
# print(province)
if province=='kochi':
    tax=.5
elif province=='bilaspur' or province=='raipur':
    tax=.2
elif province in ('bengaluru','hyderabad','pune'): # in operator to pick one from the list provided act as an 'or' operator from the list
    tax=.7
else:
    tax=.9
print('Tax you have to pay is: '+str(tax))