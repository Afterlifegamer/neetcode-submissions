class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        profit=0
        for price in prices:
            if(price<low):
                low=price
            else:
                curr_profit=price-low
            if(curr_profit>profit):
                profit=curr_profit
        return(profit)

       

        