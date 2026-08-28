def trailing_line(symbol, size):
    return symbol * size

def middle_line(symbol, size):
    return symbol + " " * (size - 2) + symbol

def print_square(symbol, size):
    print(trailing_line(symbol, size), end="")
    print(f"\n{middle_line(symbol, size)}" * (size -2))
    print(trailing_line(symbol, size))

print_square("*", 5)
print_square("|", 10)
print_square("|", 1)