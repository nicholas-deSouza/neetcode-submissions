class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        counter = Counter(nums)

        for number, count in counter.items():
            heapq.heappush(heap, (count, number))
            while len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]