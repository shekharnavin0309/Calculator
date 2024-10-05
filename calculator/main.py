def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def calculator():
    print('Welcome to the calculator!')
    x = float(input('Enter a number: '))
    y = float(input('Enter another number: '))
    print('What would you like to do?')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    choice = input('Enter your choice: ')
    if choice == '1':
        print(f'{x} + {y} = {add(x, y)}')
    elif choice == '2':
        print(f'{x} - {y} = {subtract(x, y)}')
    elif choice == '3':
        print(f'{x} * {y} = {multiply(x, y)}')
    elif choice == '4':
        print(f'{x} / {y} = {divide(x, y)}')
    else:
        print('Invalid choice!')

if __name__ == '__main__':
    calculator()

