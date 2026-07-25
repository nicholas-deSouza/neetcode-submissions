class Solution:
    def isValid(self, s: str) -> bool:
        
        # only add open parenthesis to the top of the stack
        # if you see a closed stack and it matches, pop from the stack
        # else it's not the right closing pair

        closedOpen = {")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s:
            if char in closedOpen and stack:
                if stack[-1] == closedOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False