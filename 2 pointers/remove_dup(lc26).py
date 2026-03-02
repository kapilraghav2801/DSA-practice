def remove_duplicates(arr):
    n = len(arr)
    j = 1
    result = [arr[0]]

    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            result.append(arr[j])
            j += 1
    return result

arr = [1,1,1,2,2,3] #op [1,2,3]

print(remove_duplicates(arr))