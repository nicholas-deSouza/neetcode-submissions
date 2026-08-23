class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # values in window too small, increase size of window
        # too big, decrease size of window
        # right - left + 1

        minLength = float('inf')
        left = 0
        runningSum = 0

        for right in range(len(nums)):
            runningSum += nums[right]
            
            while runningSum >= target:
                minLength = min(minLength, right - left + 1)
                runningSum -= nums[left]
                left += 1

        if minLength == float('inf'):
            return 0
        
        return minLength if minLength > 0 else 0

