from collections import deque

rc = list(map(int, input().split()))
rows = rc[0]
columns = rc[1]
matrix = []
for _ in range(rows):
    r = deque()
    #for _ in range(columns):
        #r.append(0)
    matrix.append(r)

word = input()
word_temp = deque()
diff = len(word) - columns

for i in range(rows):
    for j in range(columns):
        if not word_temp:
            for letter in word:
                word_temp.append(letter)
        if i % 2 == 0:      # Changes the direction of writing depending on the line
            matrix[i].append(word_temp.popleft())
        else:
            matrix[i].appendleft(word_temp.popleft())


for row in matrix:
    print(''.join([str(x) for x in row]))