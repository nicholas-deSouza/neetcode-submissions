class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        res = []

        for val, cnt in count.items():
            res.append([cnt,val])
        res.sort()

        final_res = []
        while len(final_res) < k:
            final_res.append(res.pop()[1])
        return final_res