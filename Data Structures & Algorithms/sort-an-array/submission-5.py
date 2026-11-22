class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        res = []

        while len(nums) > 0:
            minVal = min(nums)
            res.append(minVal)
            nums.remove(minVal)
        return res