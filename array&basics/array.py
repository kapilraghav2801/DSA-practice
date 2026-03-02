nums = [4,3,2,7,8,2,3,1]

# def find_all_disappeared(nums):
#     n = len(nums)
#     seen = set(nums)
#     result = []

#     for num in range (1,n+1):
#         if num not in seen:
#             result.append(num)

#     return result

# print(find_all_disappeared(nums))

# def find_all_disappeared(nums):
#     # Mark seen indices by negating the value at that index
#     for num in nums:
#         index = abs(num) - 1
#         if nums[index] > 0:
#             nums[index] = -nums[index]

#     # Numbers with positive values were never seen
#     return [i + 1 for i, val in enumerate(nums) if val > 0]
# print(find_all_disappeared(nums))

def find_all_disappeared(nums):
    n = len(nums)
    # Use set difference to find numbers from 1..n that are missing in nums
    return list(set(range(1, n + 1)) - set(nums))
print(find_all_disappeared(nums))