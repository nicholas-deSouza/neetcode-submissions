class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # result is the product of the values at the indices
        # keep track of result in a variable that is compared with itself using max

        # min bar  * (indice right - indice left)
        # 6 * (7 - 1) = 36

        # 1 * (7 - 0) = 7, move smallest pointer inward
        # 6 * (7 - 1) = 36, move smallest pointer inward
        # 3 * (6 - 1) = 15

        left, right = 0 , len(heights) - 1

        res = 0
        while left < right:
            min_bar = min(heights[left], heights[right]) 
            distance = right - left
            res = max(min_bar * distance, res)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res


