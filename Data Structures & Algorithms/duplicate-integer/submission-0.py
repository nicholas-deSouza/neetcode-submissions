class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # key:value pair of value:index
        map = {}

        for n in nums:
            if n in map:
                return True
            else:
                map[n] = n
        return False