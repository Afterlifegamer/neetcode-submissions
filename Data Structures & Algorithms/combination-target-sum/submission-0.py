class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subsets=[]
        def comb(start,sums):
             
            if(sums>target):
                return
            if(sums==target):
                res.append(subsets.copy())
            for i in range(start,len(nums)):
                subsets.append(nums[i])
                comb(i,sums+nums[i])
                subsets.pop()
                
        
        comb(0,0)
        return res


        
        


        