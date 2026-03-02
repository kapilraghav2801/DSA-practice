def equal_sum(arr):
    n = len(arr)
    total = sum(arr)

    if total % 2!= 0:
        return False


    target = total // 2

    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1,n+1):
        for j in range(1,target + 1):
            if arr[i-1] <= j:
                dp[i][j]  = dp[i-1][j] or dp[i-1][j-arr[i-1]]

            else:
                dp[i][j] = dp[i-1][j]

    if not dp[n][target]:
        return False,[],[]


    subset1 = []
    i = n
    j = target

    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            subset1.append(arr[i-1])
            j -= arr[i-1]
            i -= 1

    subset2 = arr.copy()
    for num in subset1:
        subset2.remove(num)

    return True,subset1,subset2

 
arr = [1,5,11,5]

print(equal_sum(arr))
