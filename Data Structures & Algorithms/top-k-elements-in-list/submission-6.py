class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for val, cnt in counter.items():
            heapq.heappush(heap, (cnt,val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        final_res = []

        for pair in heap:
            final_res.append(pair[1])

        return final_res