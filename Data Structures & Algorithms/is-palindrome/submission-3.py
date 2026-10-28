class Solution:
    def isPalindrome(self, s: str) -> bool:
        word= s.lower()
        
        start=0
        end=len(s)-1
        while(start<=end):
            if(not word[start].isalnum()):
                start+=1
                continue
            if(not word[end].isalnum()):
                end-=1
                continue
            print("This ran")
            if(word[start]!=word[end]):
                print(word[start],word[end])
                return False
            else:
                start+=1
                end-=1
            print(start,end)
        return True
