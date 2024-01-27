# Decorators

import functools
from colorama import init, Fore
init()

def color(color):
    def wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            print(color + 'changing to blue')
            func(*args, **kwargs)
        return runner
    return wrapper

@color(color=Fore.BLUE)
def greeter():
    print('Hello, world!!')
    print('Just saying hi again')

greeter()


# Imports:
# import functools: Importing the functools module, which provides higher-order functions and operations on callable objects.
# from colorama import init, Fore: Importing init and Fore (Foreground color) from the colorama module.

# Initialization:
# init(): Initializing the colorama module. This is typically done to enable the support for colored terminal text.

# Decorator Function:
# color(color): This is a decorator function that takes a color parameter and returns another function (wrapper) to be used as a decorator.

# Decorator Usage:
# @color(color=Fore.BLUE): Applying the decorator to the greeter function with the color parameter set to blue (Fore.BLUE).

# Decorated Function:
# def greeter(): This is the function that is being decorated.
# @color(color=Fore.BLUE): It means the greeter function is wrapped by the color decorator, and the color for this case is set to blue.

# Decorator Execution:
# When you call greeter(), the decorator runs the decorated function (runner function inside the decorator).
# The decorated function prints the message "changing to blue" in blue color (Fore.BLUE).
# After that, the original function (greeter) is called, which prints "Hello, world!!" and "Just saying hi again."

# So, in summary, this code defines a decorator (color) that can change the color of the text in the terminal. 
# The decorator is applied to the greeter function, and when greeter() is called, it prints a message in blue color before executing the original content of the greeter function.





