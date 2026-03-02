nums = [4,3,2,2,3,1,8]     #op [5,6,7]]

def missing_numbers(nums):
    n = len(nums)
    seen = set(nums)
    result = []

    for i in range(1,n):
        if i not in seen:
            result.append(i)

    return result
print(missing_numbers(nums))


def missing_numbers(nums):
    n = len(nums)
    seen = set(nums)

    return [i for i in range(1,n+1) if i not in seen]

nums = [4,3,2,2,3,1,8]     #op [5,6,7]]
print(missing_numbers(nums))


def missing_numbers(nums):
    n = len(nums)
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]

    return [i+1 for i in range(n) if nums[i] > 0 ]

nums = [4,3,2,2,3,1,8,7]     #op [5,6,7]]
print(missing_numbers(nums))

