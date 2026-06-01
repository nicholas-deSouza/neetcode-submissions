class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        k = 0
        for num in nums:
            if num == 1:
                k += 1
                max_consecutive = max(max_consecutive, k)
            else:
                k = 0
        return max_consecutive