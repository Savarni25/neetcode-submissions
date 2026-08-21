from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        freq_map = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of the top k frequent elements
        # heapq in Python is a min-heap by default. We store tuples of (frequency, num)
        min_heap = []
        
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # Step 3: Extract the elements from the heap
        return [num for freq, num in min_heap]      