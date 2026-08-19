class Solution:
    def isValid(self, s: str) -> bool:
        
        # use a stack and always check the top of the stack, if it's empty don't do a check
        # check if we can add the char to the stack
        # ( [ {


        closing = {")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s:
            if char in closing and stack:
                if stack[-1] == closing[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False