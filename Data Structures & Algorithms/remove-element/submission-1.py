class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # loop through the list and have another pointer behind
        # to update the elements in the list
        # pointer can also be what's tracking the count

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
                