import heapq

def k_sorted_arr(arr, k):
    min_heap = []
    result = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:   # maintain heap of size k+1
            result.append(heapq.heappop(min_heap))

    # empty remaining heap
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


arr = [6,5,3,2,8,10,9]
k = 3

print(k_sorted_arr(arr, k))


def sort_k_sorted_bruteforce(arr, k):
    n = len(arr)

    for i in range(n):
        min_index = i
        
        end = min(i + k, n - 1)

        for j in range(i + 1, end + 1):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr