import heapq

def connect_ropes(ropes):
    heapq.heapify(ropes)
    total_cost = 0

    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        cost = first + second
        total_cost += cost

        heapq.heappush(ropes,cost)

    return total_cost

              
ropes = [1,2,3,4,5]
print(connect_ropes(ropes))

