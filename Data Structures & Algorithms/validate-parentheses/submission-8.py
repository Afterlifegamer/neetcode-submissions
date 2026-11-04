class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for brack in s:
            if(brack == ')'):
                if(len(stack)==0):
                    return False
                left=stack.pop()
                if(left!='('):
                    return False
            elif(brack == '}'):
                if(len(stack)==0):
                    return False
                left=stack.pop()
                if(left!='{'):
                    return False
            elif(brack == ']'):
                if(len(stack)==0):
                    return False
                left=stack.pop()
                if(left!='['):
                    return False
            else:
                stack.append(brack)
        if(len(stack)==0):
            return True
        else:
            return False

        