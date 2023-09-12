even_ascii_values = set()
odd_ascii_values = set()
for row in range(int(input())):
    value = 0
    name = input()
    for letter in name:
        value += ord(letter)
    value //= row+1
    if value % 2:
        odd_ascii_values.add(value)
    else:
        even_ascii_values.add(value)
if sum(even_ascii_values) > sum(odd_ascii_values):
    z = list(odd_ascii_values.symmetric_difference(even_ascii_values))
    for val in z:
        print(val, end="")
        if val != z[-1]:
            print(", ", end="")
elif sum(even_ascii_values) < sum(odd_ascii_values):
    z = list(odd_ascii_values.difference(even_ascii_values))
    for val in z:
        print(val, end="")
        if val != z[-1]:
            print(", ", end="")
else:
    z = list(even_ascii_values | odd_ascii_values)
    for val in z:
        print(val, end="")
        if val != z[-1]:
            print(", ", end="")