class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        # add pairs of value and index to the stack
        # if a larger number comes in compared to the top of the stack, take the difference in index
        # at the index of the smaller number, put the difference
        # while loop to keep checking if incoming is still > stack[-1]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                topIndex = stack[-1][1]
                stack.pop()
                diff = i - topIndex
                res[topIndex] = diff
            stack.append((temp, i))
        return res