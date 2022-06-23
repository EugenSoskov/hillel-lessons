op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y}


def arithmetic(a: int, b: int, operation: str) -> str:
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(operation, str)):
        return "Invalid operation"
    elif operation not in {'+', '-', '*', '/'}:
        return "Invalid operation"
    else:
        return op[operation](a, b)


a = int(input('Введите первое число : '))
b = int(input('Введите второе чиcло : '))
c = input('Введите знак (+, -, *, /) : ')
print(arithmetic(a, b, c))
