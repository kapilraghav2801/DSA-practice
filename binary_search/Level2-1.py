def findClosestElements(arr, k, x):
    start = 0
    end = len(arr) - k

    while start < end:
        mid = start + (end - start) // 2

        dist_left = x - arr[mid]
        dist_right = arr[mid + k] - x

        if dist_left > dist_right:
            start = mid + 1      
        else:
            end = mid            

    return arr[start:start + k]
arr = [1,2,3,4,5,6,7,8,9]
k = 4
x = 6
print(findClosestElements(arr,k,x))
def findClosestElements_bruteforce(arr, k, x):
    pairs = []

    for num in arr:
        dist = abs(num - x)
        pairs.append((dist, num))

    pairs.sort()  # sorts by dist, then num (tie-break)

    ans = [num for dist, num in pairs[:k]]
    # ans = []
    # for dist, num in pairs:
    # ans.append(num)
    ans.sort()    # final output must be ascending
    return ans
print(findClosestElements_bruteforce(arr, k, x))  # [1, 2, 3, 4]



