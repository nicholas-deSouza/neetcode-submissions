class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # loop through nums twice and for each num append it to ans
         
        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans