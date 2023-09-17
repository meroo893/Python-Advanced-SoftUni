def func_executor(*functions):
    result = []

    for fx, args in functions:
        result.append(f"{fx.__name__} - {fx(*args)}")

    return '\n'.join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
        (sum_numbers, (1, 2)),
        (multiply_numbers, (2, 4))
    ))