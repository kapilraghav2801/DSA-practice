
# k = 3

# arr.sort()
# print(arr)
# print(arr[2])

# def sort(arr,k):
#     n = len(arr)
#     for i in range(k):
#         for j in range(1,n-i):
#             if arr[j-1] > arr[j]:
#                 arr[j-1],arr[j] = arr[j], arr[j-1]

#     return arr[k-1]

# arr = [7,10,4,3,20,15]  #[3,4,7,10,15,20]
# k = 3

# print(sort(arr,k))

import heapq

def find_kth_smallest(arr, k):
    # Initialize an empty list to use as our max-heap
    max_heap = []
    
    for num in arr:
        # Push the negative of the number to simulate a Max-Heap
        heapq.heappush(max_heap, -num)
        
        # If heap size exceeds k, pop the largest element
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    # The root of the max-heap is the kth smallest element
    # Multiply by -1 to get the original value back
    return -max_heap[0]

# Example from your notes
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = find_kth_smallest(arr, k)

print(f"The {k}rd smallest element is: {result}")


















