expression = input().split()
nums = []

for char in expression:
    try:
        nums.append(int(char))
    except ValueError:
        operator = char
        if operator == "-":
            res = nums[0]
            for n in nums[1:]:
                res -= n
            nums.clear()
            nums.append(res)
        elif operator == "+":
            res = nums[0]
            for n in nums[1:]:
                res += n
            nums.clear()
            nums.append(res)
        elif operator == "*":
            res = nums[0]
            for n in nums[1:]:
                res *= n
            nums.clear()
            nums.append(res)
        else:
            res = nums[0]
            for n in nums[1:]:
                res //= n
            nums.clear()
            nums.append(res)

print(nums[0])