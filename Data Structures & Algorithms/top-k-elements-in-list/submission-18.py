class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        counter = Counter(nums)

        for val, idx in counter.items():
            heap.append((idx, val))
        
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [pairs[1] for pairs in heap]

        