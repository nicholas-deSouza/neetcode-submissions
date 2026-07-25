class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (value, index)

        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((val, idx))
        return res