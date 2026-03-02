import heapq

def kth_largest(arr,k):
    min_heap = []

    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap,num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)


    return min_heap[0]

arr = [3,4,7,10,15,20]
k = 3
print(kth_largest(arr,k))