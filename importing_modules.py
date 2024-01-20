# Importing a module

# import module as namepsace 
import helpers
helpers.display_message('Not a warning !')

# import all into current namespace
from helpers import *
display_message('Not a warning !!')

# import specific item into current namespace 

from helpers import display_message

display_message('Not a warning !!!')
