logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(logo)

operators = ['+','-','*','/']



while True:
    x = float(input("Please Enter the First Number : "))

    for ope in operators:
        print(ope)

    operator = input("Pick an operation: ")
    y = float(input("Please Enter the Second Number : "))
    if operator not in operators:
        print('{} {} {} = {}'.format(x, "undefined", y, 0.0))
    else:
        if operator == '+':
            print('{} {} {} = {}'.format(x, operator, y,x+y ))
        elif operator == '-':
            print('{} {} {} = {}'.format(x, operator, y,x-y ))
        elif operator == '*':
            print('{} {} {} = {}'.format(x, operator, y,x*y )) 
        elif operator == '/':
            print('{} {} {} = {}'.format(x, operator, y,x/y ))  
    
    do = input("Type 'y' to calculate again or any other key to exit: ").strip().lower()
    if do != 'y':
        break
    continue



