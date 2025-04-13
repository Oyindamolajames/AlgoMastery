# Solution 1
def twoNumberSum(array, targetSum):
    pass
    # Set the lookup object
    nums = {}

    for num in array:
        compliment = targetSum - num
        if compliment in nums:
            return [num, compliment]
        else:
            nums[num] = True

    return []

# Solution 2
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []

# Solution 3
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    l = 0
    r = len(array) - 1
    while l < r:
        currentSum = array[r] + array[l]
        if currentSum == targetSum:
            return [array[l], array[r]]
        elif currentSum < targetSum:
            l += 1
        elif currentSum > targetSum:
            r -= 1

    return []

