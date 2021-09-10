arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10


def twosum(arr, target):
    nums = {}
    for num in arr:
        if target - num in nums:
            return print([target-num, num])
        else:
            nums[num] = True
    return []


twosum(arr, target)
