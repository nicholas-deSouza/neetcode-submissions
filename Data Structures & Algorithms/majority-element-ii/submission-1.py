class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counter = Counter(nums)

        length = len(nums) / 3

        for val in counter:
            if counter[val] > length:
                res.append(val)
        return res

        