def sum_neg(args):
    return sum([x for x in args if x < 0])


def sum_pos(args):
    return sum([x for x in args if x > 0])


nums = tuple(map(int, input().split()))

neg = sum_neg(nums)
pos = sum_pos(nums)

print(neg)
print(pos)
if neg + pos > 0:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
