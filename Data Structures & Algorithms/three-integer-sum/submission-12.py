class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res