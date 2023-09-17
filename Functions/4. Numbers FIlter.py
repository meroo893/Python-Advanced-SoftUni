def even_odd_filter(**kwargs):
    filtered = {}
    for key, nums in kwargs.items():
        if key == "even":
            filtered["even"] = [x for x in nums if x % 2 == 0]
        else:
            filtered["odd"] = [x for x in nums if x % 2 != 0]

    for key, nums in sorted(filtered.items(), key=lambda x: len(x[1])):
        filtered[key] = nums
    return filtered


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))