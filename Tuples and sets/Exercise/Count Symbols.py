symbols = {}
text = input()
t = []
for let in text:
    t.append(let)
t.sort()
for letter in t:
    if letter in symbols.keys():
        symbols[letter] += 1
    else:
        symbols[letter] = 1

for key, value in symbols.items():
    print(f"{key}: {value} time/s")