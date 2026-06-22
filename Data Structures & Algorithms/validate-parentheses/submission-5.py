class Solution:
    def isValid(self, s: str) -> bool:
        
        # implement a stack to keep track of the most recent parenthesis
        # check values using a map, when the parenthesis is a closed one we check if 
        # the top value is the correct one

        stack = []

        closed_open = {")":"(", "}":"{", "]":"["}

        # short circuit, if odd there can not be matching pairs
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in closed_open:
                if not stack or stack.pop() != closed_open[char]:
                    return False  
            else:
                stack.append(char)
        return True if not stack else False
    
                