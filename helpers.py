from pip._vendor.colorama import init, Fore
def display_message(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)