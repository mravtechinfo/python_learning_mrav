#Dates
# It is one of the most difficult data type to work in any programming language

# We often need current date and time when logging errors and saving data

# To get current date and time
# we need to use the datetime library
from datetime import datetime
current_date = datetime. now()
# the now function returns a datetime object
print( 'Today is:' + str (current_date))

