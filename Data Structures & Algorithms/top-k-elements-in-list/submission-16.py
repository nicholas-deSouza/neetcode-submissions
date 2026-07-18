class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        final_res = []

        counter = Counter(nums)

        for value, count in counter.items():
            res.append([count,value])      
        
        reverse_sorted_res = sorted(res)

        while len(final_res) < k:
            final_res.append(reverse_sorted_res.pop()[1])
        return final_res