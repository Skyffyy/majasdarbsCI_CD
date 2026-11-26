import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


OPERATIONS = {"+": add, "-": sub, "*": mul, "/": div}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError("Nezinama darbiba: " + op)
    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        a, op, b = sys.argv[1:]
    else:
        a = input("Pirmais skaitlis: ")
        op = input("Darbiba (+ - * /): ")
        b = input("Otrais skaitlis: ")
    print(calculate(float(a), op, float(b)))