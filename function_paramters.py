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

def error_logger (error_code, error_severity, log_to_db,error_message, source_module):
    print('oh no error: ' + error_message)
# Imagine code here that logs our error to a database or file
first_number = 10
second_number = 5
if first_number > second_number:
    error_logger (45, 1, True,'Second number greater than first','my_math_method')