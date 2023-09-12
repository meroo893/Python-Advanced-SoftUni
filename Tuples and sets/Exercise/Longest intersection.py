longest_intersection = set()
for _ in range(int(input())):
    cmd = input().split(",")
    first_start = int(cmd[0])
    first_end = int(cmd[1].split("-")[0])
    second_start = int(cmd[1].split("-")[1])
    second_end = int(cmd[2])
    intersection = set(range(first_start, first_end+1)) & set(range(second_start, second_end+1))
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection = list(longest_intersection)
longest_intersection.sort()
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
