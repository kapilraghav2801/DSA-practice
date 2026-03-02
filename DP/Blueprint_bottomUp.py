def knapsack(wt, val, W, n):
    # Base case
    if n == 0 or W == 0:
        return 0

    # If current item fits
    if wt[n-1] <= W:
        take = val[n-1] + knapsack(wt, val, W - wt[n-1], n-1)
        skip = knapsack(wt, val, W, n-1)
        return max(take, skip)

    # If current item doesn't fit
    else:
        return knapsack(wt, val, W, n-1)