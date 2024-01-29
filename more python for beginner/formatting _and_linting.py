x =  54;

def demo():

    return 'hello'
    print('Not allowed')

# Formatting
# Formatting makes code readable and easier to debug.

# Documentation
# PEP 8 is a set of coding conventions for Python code
# Docstring is the standard for documenting a module, function, class or method definition
# Linting
# Linting helps you identify formatting and convention issues in your Python code

# Pylint Pylint is a linter for Python to help enforce coding standards and check for errors in Python code
# Linting Python in Visual Studio Code will show you how to enable litners in VS Code
# Type hints allow some interactive development environments and linters to enforce types
    
 # Good code
    
def print_hello(name: str) -> str:
    """
    Greets the user by name

	Parameters:
		name (str): The name of the user
	Returns:
		str: The greeting
	"""
    print('Hello, ' + name)



# Bad code
x = 12
if x == 24:
 print('Is valid')
else:
    print("Not valid")

def helper(name='sample'):
 pass

def another(name = 'sample'):
         pass