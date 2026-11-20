class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        noDuplicates = set()

        for num in nums:
            if num in noDuplicates:
                return True
            else:
                noDuplicates.add(num)
        return False