def kth_grammer(n,k):
    if n == 1:
        return 0
    
    mid = 1 << (n-2)

    if k <= mid:
        return kth_grammer(n-1, k)
    else:
        return 1 - kth_grammer(n-1, k-mid)
    
print(kth_grammer(n=4,k=9))
    