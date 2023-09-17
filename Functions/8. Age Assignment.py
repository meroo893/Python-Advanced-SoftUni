def age_assignment(*names, **ages):
    res = ""
    sorted_letters = sorted(ages.keys(), key=lambda x: x)
    for letter in sorted_letters:
        for name in names:
            if letter == name[0]:
                res += f"{name} is {ages[letter]} years old.\n"
    return res


print(age_assignment("Amy", "Bill", "Willy", W=36,

A=22, B=61))