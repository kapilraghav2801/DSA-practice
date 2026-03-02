import heapq

def relative_rank(score):
    max_heap = []
    
    for i,val in enumerate(score):
        heapq.heappush(max_heap, (-val,i))
    
    n = len(score)
    result = [""] * n
    rank = 1

    while max_heap:
        val, idx = heapq.heappop(max_heap)

        if rank == 1:
            result[idx] = "Gold Medal"
        elif rank == 2:
            result[idx] = "Silver Medal"
        elif rank == 3:
            result[idx] = "Bronze"
        else:
            result[idx] = str(rank)

        rank += 1
    return result

score = [10,3,8,9,4]
#Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

print(relative_rank(score))