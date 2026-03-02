def max_average(arr, k):
    n = len(arr)
    
    # --- 1. INITIALIZATION ---
    current_sum = 0
    result = float('-inf') # (Depends on problem: float('-inf'), 0, or [])
    
    i = 0
    j = 0
    
    while j < n:
        # --- 2. ADD NEW ELEMENT ---
        current_sum += arr[j] 
        
        if j - i + 1 < k:
            j += 1
            
        elif j - i + 1 == k:
            current_avg = current_sum / k
            result = max(result,current_avg)
            
            # --- 3. CALCULATE RESULT (The Variation) ---
            # >> LOGIC GOES HERE <<
            
            # --- 4. SLIDE WINDOW ---
            current_sum -= arr[i] # Remove left element
            i += 1
            j += 1
            
    return result

arr = [1,12,-5,-6,50,3]
k = 4

print(max_average(arr,k))