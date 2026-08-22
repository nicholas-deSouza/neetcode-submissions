class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if stack and char in closed:
                if stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
