from collections import Counter
import heapq

def freq_sort(arr):
    freq_map = Counter(arr)
    max_heap = []

    for num,count in freq_map.items():
        heapq.heappush(max_heap,(-count,num))
    result = []

    while max_heap:
        count,num = heapq.heappop(max_heap)
        result.extend(-count * [num])

    return result

arr = [1,1,1,3,2,2,4]  #op = [1,1,1,2,2,3,4]

print(freq_sort(arr))


