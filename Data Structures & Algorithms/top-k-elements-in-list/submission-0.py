class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = defaultdict(int)
        res = []

        for val in nums:
            hash_map[val] += 1
        
        for num, cnt in hash_map.items():
            res.append([cnt, num])
        # sort will sort lexigraphically, the first item in this case is the count
        res.sort()

        final_res = []
        while len(final_res) < k:
            # grab value at the end of the array 
            final_res.append(res.pop()[1])
        return final_res
