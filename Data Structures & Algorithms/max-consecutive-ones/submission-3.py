class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current_longest = 0
        max_longest = 0

        for num in nums:
            if num == 1:
                current_longest += 1
                max_longest = max(max_longest, current_longest)
            else:
                current_longest = 0
        return max_longest