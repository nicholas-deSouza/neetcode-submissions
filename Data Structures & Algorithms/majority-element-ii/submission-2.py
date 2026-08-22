class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counter = Counter(nums)

        for val in counter:
            if counter[val] > len(nums) / 3:
                res.append(val)
        return res