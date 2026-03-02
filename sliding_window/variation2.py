from collections import Counter

def blueprint_level2(s, k, p=None):
    """
    Level 2: Sliding Window with Strings & HashMaps
    s = string to search in
    k = window size (or pattern length)
    p = pattern (if needed)
    """
    n = len(s)
    if k <= 0 or k > n:
        return None   
    # --- 1. INITIALIZATION ---
    target_count = Counter(p) if p else None
    window_count = Counter()
    result = []
    
    i = 0
    j = 0
    
    while j < n:
        # --- 2. ADD NEW ELEMENT ---
        window_count[s[j]] += 1
        
        if j - i + 1 < k:
            j += 1
            
        elif j - i + 1 == k:
            
            # --- 3. CALCULATE RESULT (Variation) ---
            # >> LOGIC GOES HERE <<
            
            # --- 4. SLIDE WINDOW (Remove left element) ---
            window_count[s[i]] -= 1
            if window_count[s[i]] == 0:
                del window_count[s[i]]  # CRITICAL!
            i += 1
            j += 1
    
    return result


# Test example
s = "abab"
p = "ab"
k = len(p)
print(blueprint_level2(s, k, p))