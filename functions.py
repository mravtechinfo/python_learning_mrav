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

