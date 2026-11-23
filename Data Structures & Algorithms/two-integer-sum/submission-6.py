class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffMap = {}


        for i, val in enumerate(nums):
            diff = target - val
            if diff in diffMap:
                return [diffMap[diff], i]
            else:
                diffMap[val] = i
