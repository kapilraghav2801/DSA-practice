from collections import deque

def first_negative_deque(arr, k):
    n = len(arr)
    result = []
    q = deque() # Stores INDICES of negative numbers

    if n < k: return result

    i = 0
    j = 0

    while j < n:
        # 1. Calculation (Add j)
        if arr[j] < 0:
            q.append(j)

        # 2. Window Growth
        if j - i + 1 < k:
            j += 1
        
        # 3. Window Maintenance (Size hit K)
        elif j - i + 1 == k:
            # a. Capture Result
            if not q:
                result.append(0)
            else:
                result.append(arr[q[0]]) # First negative is at q[0]

            # b. Remove i (Slide logic)
            # If the index at the front is the one we are leaving behind (i), remove it
            if q and q[0] == i:
                q.popleft()

            # c. Slide
            i += 1
            j += 1

    return result

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(first_negative_deque(arr, k)) 
# Output: [-1, -1, -7, -15, -15, 0]