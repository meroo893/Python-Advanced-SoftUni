rows = input().split("|")
matrix = []
for row in rows[::-1]:
    row = row.strip()
    matrix.extend(row.split())

print(*matrix)