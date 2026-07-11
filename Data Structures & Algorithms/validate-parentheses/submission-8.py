class Solution:
    def isValid(self, s: str) -> bool:
        # the top of the stack has to match brackets

        # create a dictionary of open:close

        if len(s) == 1:
            return False

        closeToOpen = {')':'(', '}': '{', ']':'['}

        stack = []

        for char in s:
            if char in closeToOpen and stack:
                if stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False

            
        