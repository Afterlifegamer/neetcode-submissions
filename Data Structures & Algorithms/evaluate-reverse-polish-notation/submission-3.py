class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for opr in tokens:
            if(opr not in ("+","-","*","/")):
                stack.append(opr)
            else:
                opr2=int(stack.pop())
                opr1=int(stack.pop())
                if(opr=='+'):
                    stack.append(opr1+opr2)
                elif(opr=='-'):
                    stack.append(opr1-opr2)
                elif(opr=='*'):
                    stack.append(opr1*opr2)
                elif(opr=='/'):
                    stack.append(opr1/opr2)
        return int(stack[-1])