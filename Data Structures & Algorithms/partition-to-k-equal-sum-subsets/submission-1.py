class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums=sum(nums)//k
        res=[]
        curr=[[] for _ in range(k)]
        def dfs(i):
            if(i==len(nums)):
                return True
            for sets in curr:
                if(sum(sets)+nums[i]<=sums):
                    sets.append(nums[i])
                    if(dfs(i+1)):
                        return True
                    sets.pop()
                    
                    if(sum(sets)==0):
                        break
            return False
        return dfs(0)



        