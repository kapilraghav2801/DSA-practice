from collections import Counter
import heapq

def sort_char_freq(s):
    freq_map = Counter(s)
    max_heap = []

    for char,count in freq_map.items():
        heapq.heappush(max_heap,(-count,char))

    result = []
    while max_heap:
        count,char = heapq.heappop(max_heap)
        result.append(char * (-count))

    return ''.join(result)
    

s = "tree"  #eert
print(sort_char_freq(s))

