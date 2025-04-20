# Solution 1 using a while loop

def isValidSubsequence(array, sequence):
    # Write your code here.
    idx_a = 0
    idx_s = 0

    while idx_a < len(array) and idx_s < len(sequence):
        if array[idx_a] == sequence[idx_s]:
            idx_s += 1
        idx_a += 1
        if idx_s == len(sequence):
            return True

    return False

# Solution 2 using a for loop
def isValidSubsequence(array, sequence):
    # Write your code here.
    idx_s = 0

    for num in array:
        if num == sequence[idx_s]:
            idx_s += 1

        if idx_s == len(sequence):
            return True
    return False


