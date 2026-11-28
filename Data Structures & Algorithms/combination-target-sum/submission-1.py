class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        def dfs(i,sums):
            if(i>=len(nums) or sums>target):
                return
            if(sums==target):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            sums+=nums[i]
            dfs(i,sums)
            curr.pop()
            sums-=nums[i]
            dfs(i+1,sums)
        dfs(0,0)
        return res


        
        


        