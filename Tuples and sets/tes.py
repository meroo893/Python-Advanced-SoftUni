#   zad 1 activation keys
"""txt = input()
text = []
for letter in txt:
    text.append(letter)

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        break
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        for _ in range(end-start):
            text.pop(start)
        print("".join(text))
    elif command[0] == "Flip":
        start = int(command[2])
        end = int(command[3])
        if command[1] == "Upper":
            for index in range(start, end):
                text.insert(index, text.pop(index).upper())
        else:
            for index in range(start, end):
                text.insert(index, text.pop(index).lower())
        print("".join(text))
    elif command[0] == "Contains":
        substring = command[1]
        if substring in ''.join(text):
            print(f"{''.join(text)} contains {substring}")
        else:
            print("Substring not found!")

print(f"Your activation key is: {''.join(text)}")"""

#   zad 2 emoji detector
"""import re
text = input()

pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
emojis = re.findall(pattern, text)
digits = re.findall(r"\d", text)
cool_threshold = 1
for digit in digits:
    cool_threshold *= int(digit)


cool_ones = []
for emoji in emojis:
    coolness = 0
    for index in range(2, len(emoji)-2):
        coolness += ord(emoji[index])
    if coolness >= cool_threshold:
        cool_ones.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_ones:
    print(emoji)"""

#   zad 3 P!rates
class City:
    def __init__(self, name: str, population: int, gold: int):
        self.name = name
        self.population = population
        self.gold = gold

    def plunder(self, victims, loot):
        self.population -= victims
        self.gold -= loot

    def prosper(self, growth):
        if growth >= 0:
            self.gold += growth

    def __repr__(self):
        return f"{self.name} -> Population: {self.population} citizens, Gold: {self.gold} kg"


cities = []
city_names = []
while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    else:
        name = command[0]
        population = int(command[1])
        gold = int(command[2])
        if name not in city_names:
            city_names.append(name)
            cities.append(City(name, population, gold))
        else:
            for city in cities:
                if city.name == name:
                    city.gold += gold
                    city.population += population

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    elif command[0] == "Plunder":
        name = command[1]
        killed = int(command[2])
        grabbed = int(command[3])
        for city in cities:
            if city.name == name:
                city.gold -= grabbed
                city.population -= killed
                print(f"{name} plundered! {grabbed} gold stolen, {killed} citizens killed.")
                if city.population <= 0 or city.gold <= 0:
                    print(f"{city.name} has been wiped off the map!")
                    cities.remove(city)
    else:
        name = command[1]
        prosperity = int(command[2])
        if prosperity >= 0:
            for city in cities:
                if city.name == name:
                    city.gold += prosperity
                    print(f"{prosperity} gold added to the city treasury. {name} now has {city.gold} gold.")
        else:
            print("Gold added cannot be a negative number!")
if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(city)
