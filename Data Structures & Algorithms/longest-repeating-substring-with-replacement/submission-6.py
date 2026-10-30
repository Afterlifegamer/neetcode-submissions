
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=0
        for c in set(s):
            l=0
            temp=k
            for right in range(len(s)):
                if(s[right]!=c):
                    temp-=1
                while(temp<0):
                    if(s[l]!=c):
                        temp+=1
                    l+=1
                count=max(count,right-l+1)
        return count
                
                    



