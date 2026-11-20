class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxOnes = 0

        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right] == 1 and nums[left] == 1:
                maxOnes = max(maxOnes, right - left + 1)
            elif nums[right] == 0:
                left = right + 1
        return maxOnes