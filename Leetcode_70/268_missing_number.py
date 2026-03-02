def missing_number(nums):
    nums.sort()
    for i, v in enumerate(nums):
        if i != v:
            return i
    return len(nums)

nums = [2,0,3]
print(missing_number(nums))

def missing_number_xor(nums):
    n = len(nums)           # n = 3
    res = n                 # res = 3
    
    for i, v in enumerate(nums):
        # i ranges: 0, 1, 2 (indices)
        # v are values: 2, 0, 3
        res ^= i ^ v
    
    return res

def missing_number(nums):
    return sum(range(len(nums) + 1)) - sum(nums)

nums = [2,0,3]
print(missing_number(nums))



