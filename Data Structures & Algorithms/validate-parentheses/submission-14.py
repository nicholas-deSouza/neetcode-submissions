class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in closed and stack:
                if stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False