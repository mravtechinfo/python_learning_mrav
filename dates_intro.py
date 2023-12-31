#Dates
# It is one of the most difficult data type to work in any programming language

# We often need current date and time when logging errors and saving data

# To get current date and time
# we need to use the datetime library
from datetime import datetime, timedelta
# the above line means ghet me the datettime function from the datetime library
today = datetime.now()
# the now function returns a datetime object
print( 'Today is:' + str (today))

# timedelta is used to define a period of time

one_day = timedelta(days=1)

yesterday  =  today - one_day

print('Yesterday was: '+ str(yesterday))

print ('Day: '+str(today.day))
print('Month: '+str(today.month))
print('Year: '+str(today.year))

# Sometimes you receive the date as a string and need to convert it to a datetime object

birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: '+str(birthday_date))