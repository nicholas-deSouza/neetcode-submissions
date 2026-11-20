class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        max_less_than_k = -1

        i = 0
        j = len(nums) - 1

        nums.sort()

        while i < j:
            summation = nums[i] + nums[j]
            if summation < k:
                max_less_than_k = max(max_less_than_k, summation)
                i += 1
            else:
                j -= 1
    
        return max_less_than_k 