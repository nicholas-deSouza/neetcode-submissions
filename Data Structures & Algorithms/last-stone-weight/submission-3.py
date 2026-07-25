class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # [2,2,3,4,6]
        # [2,2,2,3]

        if len(stones) == 1:
            return stones[-1]


        while len(stones) > 1:
            stones.sort()
            left = len(stones) - 2
            right = len(stones) - 1
            if stones[left] == stones[right]:
                stones.pop()
                stones.pop()
            elif stones[left] < stones[right]:
                diff = stones[right] - stones[left]
                stones.pop()
                stones.pop()
                stones.append(diff)
        return stones[0] if stones else 0
        
