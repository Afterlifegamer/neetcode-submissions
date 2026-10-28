from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for s in tokens:
            try:
                num = int(s)  # Try to convert to int (handles negatives too)
                stack.append(num)
            except ValueError:
                # It's an operator
                digit2 = stack.pop()
                digit1 = stack.pop()
                if s == '+':
                    stack.append(digit1 + digit2)
                elif s == '-':
                    stack.append(digit1 - digit2)
                elif s == '*':
                    stack.append(digit1 * digit2)
                elif s == '/':
                    
                    stack.append(int(digit1 / digit2))
        
        return stack[0]
