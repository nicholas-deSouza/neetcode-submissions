class KthLargest:

    # in a group of the k largest values, we want the kth largest. ex. [4,5,8,2] and k = 3, the 3 largest are
    # 4,5,8 and the kth largest is 4

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
