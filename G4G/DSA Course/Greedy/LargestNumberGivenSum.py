def largestNum(n, s):
    if s == 0:
        return "0" * n
    pos = 0
    result = 0
    totnums = 0
    remain = s
    for number in range(9, 0, -1):
        nums = remain // number
        totnums += nums
        if totnums > n:
            return -1
        remain = remain - (nums * number)
        for x in range(nums):
            result = result * 10 + number
    result = result * 10 ** (n - totnums)
    return result


print(largestNum(1, 1))
