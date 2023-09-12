"""text = input()

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        while char in text:
            text = text.replace(char, replacement)
        print(text)
    elif command[0] == "Includes":
        substring = command[1]
        print(substring in text)
    elif command[0] == "Start":
        substring = command[1]
        print(text.startswith(substring))
    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        print(text.rfind(char))
    else:
        start_index = int(command[1])
        count = int(command[2])
        txt = []
        for letter in text:
            txt.append(letter)
        for _ in range(count):
            txt.pop(start_index)
        text = "".join(txt)
        print(text)"""


"""import re
pattern = r"\|([A-Z]+)\|:#([A-Z][a-z]+ [A-Za-z]+)#"
for _ in range(int(input())):
    boss = input()
    if re.match(pattern, boss):
        boss_info = re.findall(pattern, boss)
        print(f"{boss_info[0][0]}, The {boss_info[0][1]}")
        print(f">> Strength: {len(boss_info[0][0])}")
        print(f">> Armor: {len(boss_info[0][1])}")
    else:
        print("Access denied!")"""



""""followers = {}
while True:
    command = input().split(": ")
    if command[0] == "Log out":
        break
    elif command[0] == "New follower":
        username = command[1]
        if username not in followers.keys():
            followers[username] = [0, 0]
    elif command[0] == "Like":
        username = command[1]
        count = int(command[2])
        if username in followers.keys():
            followers[username][0] += count
        else:
            followers[username] = [count, 0]
    elif command[0] == "Comment":
        username = command[1]
        if username in followers.keys():
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]
    else:
        username = command[1]
        if username in followers.keys():
            del(followers[username])
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")
for name, value in followers.items():
    print(f"{name}: {value[0] + value[1]}")"""


wrd = "asdsa"
print(wrd.split(""))