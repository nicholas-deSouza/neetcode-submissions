class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairMap = {}

        for i, n in enumerate(nums):
            pair = target - n
            if pair in pairMap:
                return [pairMap[pair], i]
            else:
                pairMap[n] = i
