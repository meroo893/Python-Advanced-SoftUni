record = {}
for _ in range(int(input())):
    datapiece = input().split()
    name = datapiece[0]
    grade = float(datapiece[1])
    if name not in record.keys():
        record[name] = [grade]
    else:
        record[name].append(grade)

for key, value in record.items():
    print(f"{key} ->", end= " ")
    for grade in value: print(f"{grade:.2f}", end=' ')
    print(f"(avg: {sum(value) / len(value):.2f})")