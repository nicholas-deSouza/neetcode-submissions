class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # output would be the largest product of (min height of two bars) * distance between bars
        # the smaller bar (height) is the limiting factor
        # the smaller bar side moves each iteration

        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            water = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater



