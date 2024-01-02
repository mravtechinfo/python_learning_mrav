# Error Handling - Error handling is when I have a problem with my code that's running, and it's not something that I'm going to be able to predict when I pushed my code out to production. The most common example of this would be a permissions issue, a database changing, a server being down, etc.

# Debugging - Debugging is when I know that there's a problem with my code.That it's potentially giving me a wrong answer, it's potentially crashing, and I know that there's something that I've done incorrectly that's causing my code to go sideways. That's debugging.



x=10
y=0
#print(x/y)  #ZeroDivisionError: division by zero
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our clean up code')
print()

