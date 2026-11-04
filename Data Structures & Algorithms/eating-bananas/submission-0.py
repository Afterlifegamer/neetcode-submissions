from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper=max(piles)
        lower=1
        result=-1
        while(lower<=upper):
            mid=(lower+upper)//2
            sums=0
            for num in piles:
                sums+=ceil(num/mid)
            if(sums>h):
                lower=mid+1
            else:
                result=mid
                upper=mid-1
        return result        

        