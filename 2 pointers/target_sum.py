def target_sum(arr,target):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return False
    
arr = [2,5,8,9,11]
target = 17
print(target_sum(arr,target))