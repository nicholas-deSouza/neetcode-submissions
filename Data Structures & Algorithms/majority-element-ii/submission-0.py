class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        division = len(nums) // 3
        res = []
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for val in freq:
            if freq[val] > division:
                res.append(val)

        return res