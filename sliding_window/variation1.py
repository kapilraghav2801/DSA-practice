def blueprint(arr, k):
    n = len(arr)
    if k <= 0 or k > n:
        return None  # or raise ValueError
    
    # --- 1. INITIALIZATION ---
    current_sum = 0
    result = [] # depends on problem

    i = 0
    j = 0

    while j < n:
        # --- 2. ADD NEW ELEMENT ---
        current_sum += arr[j]

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            result.append(current_sum)
            

            # --- 3. CALCULATE RESULT (Variation) ---
            # >> LOGIC GOES HERE <<

            # --- 4. SLIDE WINDOW ---
            current_sum -= arr[i]
            i += 1
            j += 1

    return result

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(blueprint(arr,k))