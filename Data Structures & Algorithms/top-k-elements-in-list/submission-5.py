class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for val in nums:
            freq[val] += 1
        
        res = []

        for val, cnt in freq.items():
            res.append([cnt,val])
        sorted_res = sorted(res)

        final_res = []

        while len(final_res) < k:
            final_res.append(sorted_res.pop()[1])
        return final_res