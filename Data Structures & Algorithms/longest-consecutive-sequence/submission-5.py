class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
    # put everything in a map and while iterating, check if the next value is in the map?

    # [2,20,4,10,3,4,5]

        longest = 0

        seen = set()

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + 1 in seen:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest
