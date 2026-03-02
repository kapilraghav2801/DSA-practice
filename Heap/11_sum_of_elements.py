import heapq

def sum_elements(arr, k1, k2):
    min_heap = arr[:]
    heapq.heapify(min_heap)

    # Remove first k1 smallest elements
    for _ in range(k1):
        heapq.heappop(min_heap)

    # Sum next (k2 - k1 - 1) elements
    total = 0
    for _ in range(k2 - k1 - 1):
        total += heapq.heappop(min_heap)

    return total

arr = [1, 3, 12, 5, 15, 11]
k1 = 3
k2 = 6
print(sum_elements(arr, k1, k2))  # Output: 23 (5 + 11 + 7? -> actual: between 3rd and 6th: 5,11 => 16)

