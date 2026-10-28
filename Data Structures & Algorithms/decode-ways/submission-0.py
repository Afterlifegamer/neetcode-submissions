class Solution:
    def numDecodings(self, s: str) -> int:
        
        def check(i):
            if(i>=len(s)):
                return 1
            if(s[i]=='0'):
                return 0
            
            count=check(i+1)
                   
            if(i+1<len(s) and 10<=int(s[i:i+2])<=26):
                count+=check(i+2)
            return count
        res=check(0)
        return res
                
            

        
            

            
            
            
        
        