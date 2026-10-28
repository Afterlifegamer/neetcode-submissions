class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def comb(i,curr,total):
            if(total==target):
                res.append(curr.copy())
                return
            if(total>target or i==len(nums)):
                return
            
            curr.append(nums[i])
            comb(i+1,curr,total+nums[i])
            curr.pop()
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            comb(i+1,curr,total)
        comb(0,[],0)
        return res
        