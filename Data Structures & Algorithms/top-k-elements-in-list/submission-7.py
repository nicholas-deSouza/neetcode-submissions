class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for val, cnt in counter.items():
            heapq.heappush(heap, (cnt,val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]