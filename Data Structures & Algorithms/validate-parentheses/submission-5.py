class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if(len(s)==1):
                return False
            if(i=='['or i=='{'or i=='('):
                stack.append(i)
                
            else:
                if(len(stack)<=0):
                    return False
                top=stack.pop()
                if(i=="}"):
                    if(top!='{'):
                        return False
                elif(i==")"):
                    if(top!='('):
                        return False
                elif(i=="]"):
                    if(top!='['):
                        return False
        if(len(stack)==0):
            return True
        else:
            return False
                

        