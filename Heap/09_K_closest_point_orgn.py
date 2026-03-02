import heapq

def k_closest_point(points, k):  
    max_heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(max_heap, (-dist, (x, y)))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    result = [[x, y] for (_, (x, y)) in max_heap]
    return result

# points = [[3, 3], [5, -1], [-2, 4]]
# k = 2
# # Output: [[3,3],[-2,4]]


points = [[3,4],[2,2],[1,1],[0,0],[5,5]]
k = 3

#Output:[[2,2],[1,1],[0,0]]

print(k_closest_point(points, k))