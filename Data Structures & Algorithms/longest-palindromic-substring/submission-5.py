class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen=0
        res=""
        if(len(s)==1):
            return s
        for i in range(len(s)):
            l=i-1
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                print("No this")
                curlen=(r-l)+1
                if(curlen>reslen):
                    reslen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
                
                
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                print("This ran")
                curlen=(r-l)+1
                if(curlen>reslen):
                    reslen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        if(res==""):
            return s[0]
        else:
         return res

            
                

            
            
        