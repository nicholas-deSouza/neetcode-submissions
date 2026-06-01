class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # example of using an array to check for duplicates, does not scale well with larger inputs
        arr = []

        for num in nums:
            if num in arr:
                return True
            else:
                arr.append(num)
        return False