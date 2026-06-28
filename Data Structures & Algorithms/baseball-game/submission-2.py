class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        summation = 0
        stack = []
        
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 + num2 
                stack.append(num2)
                stack.append(num1)
                stack.append(num3)
            elif op == "D":
                num = int(stack[-1])
                double_num = num * 2
                stack.append(double_num)
            else: 
                stack.append(int(op))
        
            
        summation = sum(stack)

        return summation