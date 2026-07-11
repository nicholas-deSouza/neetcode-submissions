class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                firstVal = stack.pop()
                secondVal = stack.pop()
                summation = firstVal + secondVal
                stack.append(summation)
            elif char == "-":
                firstVal = stack.pop()
                secondVal = stack.pop()
                difference = secondVal - firstVal
                stack.append(difference)
            elif char == "*":
                firstVal = stack.pop()
                secondVal = stack.pop()
                product = firstVal * secondVal
                stack.append(product)
            elif char == "/":
                firstVal = stack.pop()
                secondVal = stack.pop()
                division = int(secondVal / firstVal)
                stack.append(division)
            else:
                stack.append(int(char))
        return stack[-1]