arr = [1,2,3,4,5,6,7,8,9]
target = 7

n = len(arr)

def find_target_index(arr,target):
    start = 0
    end = n - 1

    while start <= end:
        mid = start + end - start // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(find_target_index(arr,target))
        