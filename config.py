from operator import add, sub, mul, truediv

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

error_zero_div = 'Division by zero'
error_undefined = 'Result is undefined'

default_font_size = 16
default_input_font_size = 40