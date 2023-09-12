rc = list(map(int, input().split()))
rows = rc[0]
columns = rc[1]
matrix = []
for i in range(rows):
    for j in range(columns):
        print(f"{chr(97+i)}{chr(97+i+j)}{chr(97+i)}", end=" ")
    print()