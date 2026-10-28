class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=101
        maxprofit=0
        for i in prices:
            if(i<lowest):
                lowest=i
            else:
                profit=i-lowest
                maxprofit=max(maxprofit,profit)
        return maxprofit
            

        