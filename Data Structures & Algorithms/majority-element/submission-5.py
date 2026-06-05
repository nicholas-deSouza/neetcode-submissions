class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        half = len(nums) / 2

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > half:
                return num

                