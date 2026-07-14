class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0 is always the sum value we want

        #[-4, -1, -1, 0, 1, 2]

        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            ptr2 = i + 1
            ptr3 = len(nums) - 1
            complement = -nums[i] 
            while ptr2 < ptr3:
                if nums[ptr2] + nums[ptr3] < complement:
                    ptr2 += 1
                elif nums[ptr2] + nums[ptr3] > complement:
                    ptr3 -= 1
                else:
                    res.append([nums[i], nums[ptr2], nums[ptr3]])
                    ptr2 += 1
                    ptr3 -= 1          
                    while nums[ptr2] == nums[ptr2 - 1] and ptr2 < ptr3:
                        ptr2 += 1         
        return res