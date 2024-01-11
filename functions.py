# Use functions instead of repeating the code.
# Increase readibility of code chances of bugs reduces clean and clear code can be obtained.
from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
first_name='Anubhav'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print()
print_time('loop completed')

def get_initial_name(name):
    initial=name[0:1]
    return initial


first_name=input('enter your First name: ')
first_name_initial = get_initial_name(first_name)

last_name=input('enter your Last name: ')
last_name_initial=get_initial_name(last_name)


print('Your name initials are: '+first_name_initial+' '+last_name_initial)