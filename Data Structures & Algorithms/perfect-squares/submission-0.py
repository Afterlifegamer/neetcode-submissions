class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for target in range(1,n+1):
            for s in range(1,target+1):
                if(s*s>target):
                    break
                square=s*s
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]
                