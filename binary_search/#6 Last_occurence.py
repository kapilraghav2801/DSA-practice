def last_occurence(arr, target):
    n = len(arr)
    start = 0
    end = n -1 
    result = -1

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == target:
            result = mid

            start = mid + 1

        elif arr[mid] <= target:
            start = mid + 1

        else:
            end = mid - 1

    return result

arr = [2,4,10,10,10,28,20]
print(last_occurence(arr, target = 28))

