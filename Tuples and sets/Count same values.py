values = list(map(float, input().split()))
unique = tuple(values)
count = {}
for val in unique:
    count.update({val: 0})

for value in values:
    count[value] += 1

for key, value in count.items():
    print(f"{key} - {value} times")