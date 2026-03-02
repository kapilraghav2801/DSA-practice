arr = [9,8,7,6,5,4,3,2,1]
target = 8

n = len(arr)

def find_target_index(arr,target):
    start = 0
    end = n - 1

    while start <= end:
        mid = start + end - start // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(find_target_index(arr,target))
        