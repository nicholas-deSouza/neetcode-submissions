class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get freq of every value in nums
        # sort by the count of it 
        # add to new array

        freq = defaultdict(int)
        res = []
        for val in nums:
            freq[val] += 1
        
        for val, cnt in freq.items():
            res.append([cnt,val])
        # highest count values will be at the end    
        res.sort()

        final_res = []
        while len(final_res) < k:
            final_res.append(res.pop()[1])
        return final_res