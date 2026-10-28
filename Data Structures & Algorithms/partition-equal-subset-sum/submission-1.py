class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2!=0):
            return False
        target=sum(nums)/2
        sums=0
        
        def dfs(i):
            nonlocal sums
            if(i==len(nums)):
                return False
            if(sums+nums[i]==target):
                return True
            elif(sums+nums[i]>target):
                return dfs(i+1)
            else:
                sums+=nums[i]
                if(dfs(i+1)):
                    return True
                sums-=nums[i]
                if(dfs(i+1)):
                    return True
                return False
        return(dfs(0))



            
                
            
        
        