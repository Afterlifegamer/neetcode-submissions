from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        left=0
        length=len(s1)
        while(left<=len(s2)-len(s1)):
            count=0
            window_count=Counter()
            
            if(s2[left] in s1):
                for i in range(left,left+length):
                    if window_count[s2[i]] < s1_count[s2[i]]:
                        window_count[s2[i]] += 1
                        count += 1
                    else:
                        break

            if count == length:
                return True

            left += 1

        return False


        