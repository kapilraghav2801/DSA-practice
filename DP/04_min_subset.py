def equal_sum_partion(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2

    dp = [[False] * (total + 1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1,n+1):
        for j in range(1,total + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    for j in range(target,-1,-1):
        if dp[n][j]:
            return total - 2 * j

    return total

   

arr = [1,6,11,5]
print(equal_sum_partion(arr))
