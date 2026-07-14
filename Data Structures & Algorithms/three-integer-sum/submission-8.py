class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            compliment = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i]> 0:
                break 
            while left < right:
                if nums[left] + nums[right] < compliment:
                    left += 1
                elif nums[left] + nums[right] > compliment:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res