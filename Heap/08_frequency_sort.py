import heapq
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        min_heap = []
        
        freq = Counter(nums)

        for num, count in freq.items():
            heapq.heappush(min_heap,(count,-num))

        result = []

        while min_heap:
            count, num = heapq.heappop(min_heap)
            result.extend(count * [-num])

        return result
        
