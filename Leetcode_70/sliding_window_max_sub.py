arr = [2,5,1,8,2,9,1]
k = 3

def max_subarray(arr,k):
    n = len(arr)
    current_sum = 0
    max_sum = float('-inf')
    i = 0
    j = 0

    if n < k:
        return -1

    while j < n:
        current_sum += arr[j]

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            max_sum = max(current_sum,max_sum)
            current_sum -= arr[i]

            i += 1
            j += 1

    return max_sum

print(max_subarray(arr,k))


#2 Pythonic method
arr = [2,5,1,8,2,9,1]
k = 3

def max_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1

    current_sum = sum(arr[:k])
    max_sum = current_sum

    i = 0

    for j in range(k, n):
        current_sum += arr[j]
        current_sum -= arr[i]
        i += 1
        max_sum = max(max_sum, current_sum)

    return max_sum
        
print(max_subarray(arr,k))



    
def max_all_subarray(arr,k):
    n = len(arr)
    result = []

    if n < k:
        return result

    i = 0
    j = 0

    current = []
    max_res = []

    while j < n :

        current.append(arr[j])

        if j-i+1 < k:
            current.append(arr[j])

        elif j-i+1 == k:
            max_res = max(max_res,current)
            result.append(max_res)
            
            i += 1
            j += 1

    return result
arr = [1,3,-1,-3,5,3,6,7]  #[3,3,5,5,6,7]
k = 3

print(max_all_subarray(arr,k))


