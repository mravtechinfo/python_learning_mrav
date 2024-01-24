from pip._vendor.colorama import init, Fore
def display_message(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message + Fore.RESET)

# Fore.RESET to reset the color of terminal other wise it uses the last color for the whole terminal for the rest of the work you do 