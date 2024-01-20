def get_initial(name, force_uppercase):  
    # here we can make the force_uppercase=True i.e by default we can give it a value
    if force_uppercase:
        initial= name[0:1].upper()
    else:
        initial=name[0:1]
    return initial


first_name=input('Enter your first name: ')

first_name_initial=get_initial(first_name,True)
# pass parameters in same order as you have written in the functions

print('Your name initial is: '+first_name_initial) 