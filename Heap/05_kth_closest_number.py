import heapq
def kth_closest(arr,k,x):
    max_heap = []
    for num in arr:
        diff = abs(num - x)
        heapq.heappush(max_heap,(-diff, -num))

        if len(max_heap) > k:
            heapq.heappop(max_heap)
    result = []
    while max_heap:
        result.append(-heapq.heappop(max_heap)[1])

    return result

arr = [5,6,7,8,9]
k = 3
x = 7

print(kth_closest(arr,k,x))