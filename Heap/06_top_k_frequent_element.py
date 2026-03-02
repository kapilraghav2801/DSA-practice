import heapq
from collections import Counter

def topKFrequent(arr,k):
    freq_map = Counter(arr)
    min_heap = []

    for num,count in freq_map.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = [num for count, num in min_heap]
    return result

arr = [1,1,1,3,2,2,4]
k = 2

print(topKFrequent(arr,k))



