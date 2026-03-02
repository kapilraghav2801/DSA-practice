nums = [1,2,3,1]

print(list(set(nums)))

def brute_remove_duplicate(nums):
    n = len(nums)
    result = []
    for i in range(n):
        duplicate = False
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                duplicate = True
                break
        if not duplicate:
            result.append(nums[i])
    return result
nums = [1,2,3,1]
print(brute_remove_duplicate(nums))

def remove_duplicate(nums):
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

print(remove_duplicate(nums))



nums = [1,2,3,1]
def remove_duplicate(nums):
    if len(set(nums)) == len(nums):
        return True
    else:
        return False
print(remove_duplicate(nums))

