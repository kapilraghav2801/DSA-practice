def moves_0_to_end(nums):
    n = len(nums)
    result = []
    zero_count = 0
    for num in nums:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    result.extend([0] * zero_count)

    return result

nums = [0,1,0,3,1,2]
print(moves_0_to_end(nums))


def moves_0_to_end(nums):
    i = 0
    n = len(nums)

    for j in range(1,n):
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
    return nums
nums = [0,1,0,3,1,2]
print(moves_0_to_end(nums))   
        
