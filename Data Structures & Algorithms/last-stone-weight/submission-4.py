class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # max heap solution

         # [2,2,3,4,6]

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstVal = heapq.heappop(stones)
            secondVal = heapq.heappop(stones)
            if secondVal > firstVal:
                heapq.heappush(stones, firstVal - secondVal)
        return abs(stones[0]) if stones else 0