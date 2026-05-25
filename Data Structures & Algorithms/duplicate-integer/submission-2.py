class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sets can't contain duplicates

        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False