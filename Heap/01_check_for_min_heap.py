arr = [1,3,2,4,5]

def is_min_heap(arr):
    n = len(arr)

    for i in range(n//2):  #it will still works for range(n) but not required as we don't see check who has no child 
        left = 2*i + 1
        right = 2*i + 2

        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
        
    return True

print(is_min_heap(arr)) 