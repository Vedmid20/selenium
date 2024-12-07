import scripts.XPATH as X
import scripts.CSS_SELECTOR as CSS
from colorama import Fore, Style

if __name__ == '__main__':
    print(Style.BRIGHT + f'\nEnter {Fore.LIGHTYELLOW_EX + "1" + Fore.RESET} for testing XPATH or {Fore.LIGHTYELLOW_EX + "2" + Fore.RESET} for testing CSS_SELECTOR\n\n{Style.RESET_ALL}')
    choice = input(Fore.LIGHTYELLOW_EX + 'Choose: ')
    if choice == '1':
        X.go()
    elif choice == '2':
        CSS.go()
    else:
        raise ValueError('Wrong input, you can choose between 1 and 2. Try again')