"""
Excercise 9-56
Build a simple interactive calculator

3 var input: value A (int), value B (int) & operation (int)
(integers for simplicity sake, remember input() produces a string
maybe use 'q' in any of the 3 inputs to exit?)

Operations
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Integer Division
6 - Modulo

Also errorhandling like dividing by 0 is wanted

Update: Thought up and typed in 1 go (VS Code helps a lot).
I don't like the lots of repititions (due to the q input, but i don't know how yet to circumvent)
Let see how many bugs i've produced
Update 2: Sloppy config (dict wasn't completely filled with menuName) and trouble translating
a string to functionname for the use in map(). Stackoverflow showed me the use of globals()[functionname]()

But all in all i'm not unsatisfied
"""
# Operations
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

#Keys
MENU_INFO_KEY = 'menuName'
FUNCTION_NAME_KEY = 'fnName'
OPERATOR_SYMBOL_KEY = 'symbol'

#Fixed Text Constants
MENU_HEADER = "===      Welcome to you Interactive Python Calculator      ==="
NOTE_HEADER = "-- q = quit the program, otherwise only digits are expected --"
OPERATOR_WELCOME = "Great! Now enter the operation."

operations_dict = {
    ADDITION: {
        'menuName': 'Addition', 
        'fnName': 'addition', 
        'symbol': '+',
    },
    SUBTRACTION: {
        'menuName': 'Subtraction', 
        'fnName': 'subtraction', 
        'symbol': '-',
    },
    MULTIPLICATION: {
        'menuName': 'Multiplication', 
        'fnName': 'multiplication',
        'symbol': '*',
    },
    DIVISION: {
        'menuName': 'Division', 
        'fnName': 'division',
        'symbol': '/',
    },
    INTEGER_DIVISION: {
        'menuName': 'Integer Division', 
        'fnName': 'integer_division',
        'symbol': '//',
    },
    MODULO: {
        'menuName': 'Modulo', 
        'fnName': 'modulo',
        'symbol': '%',
    },
}

def addition(a: int, b: int) -> int:
    return a + b


def subtraction(a: int, b: int) -> int:
    return a - b


def multiplication(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    return a / b


def integer_division(a: int, b: int) -> int:
    return a // b


def modulo(a: int, b: int) -> int:
    return a % b


def print_operator_dict_menu() -> None:
    for key, value_dict in operations_dict.items():
        print(f"{key} - {value_dict[MENU_INFO_KEY]}")


def main() -> None:
    exit_strategy = False
    # never ending loop unless user inputs a q
    while not exit_strategy:
        # fresh start
        value_a = None
        value_b = None
        operation = None
        result = None

        print(MENU_HEADER)
        print(NOTE_HEADER)

        # first value
        while not exit_strategy:
            value_a = input('Please enter the first value: ')
            if value_a == 'q':
                exit_strategy = True
            elif value_a.isdigit():
                value_a = int(value_a)
                break
        
        if exit_strategy:
            print('Quiting the calculator')
            break 

        # second value
        while not exit_strategy:
            value_b = input('Please enter the second value: ')
            if value_b == 'q':
                exit_strategy = True
            elif value_b.isdigit():
                value_b = int(value_b)
                break
        
        if exit_strategy:
            print('Quiting the calculator')
            break 

        # operator part
        print(OPERATOR_WELCOME)
        print_operator_dict_menu()
        while not exit_strategy:
            operation = input('Input the corresponding integer: ')
            if operation == 'q':
                exit_strategy = True
            elif operation.isdigit() and int(operation) in operations_dict:
                operation = int(operation)
                break
            else:
                print("Please choose a valid operation (or q to quit)")
            
        if exit_strategy:
            print('Quiting the calculator')
            break 

        # We have all 3 mandatory ingredients, it's a go
        # one last sanity check
        if operation in {DIVISION, INTEGER_DIVISION, MODULO} and value_b == 0:
            print("No dividing by 0 possible!")
            continue # The calculator starts afresh
            
        function_name = operations_dict[operation][FUNCTION_NAME_KEY]
        operator_symbol = operations_dict[operation][OPERATOR_SYMBOL_KEY]
        # used first map(), but converting name (string) to the function reference
        # I apparently needed globals()
        result = globals()[function_name](value_a, value_b)

        print(f"The result of {value_a} {operator_symbol} {value_b} = {result}")
        print()


if __name__ == "__main__":
    main()
