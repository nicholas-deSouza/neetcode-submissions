class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # it will always be double the original

        output = []

        for i in range(2):
            for num in nums:
                output.append(num)
        return output