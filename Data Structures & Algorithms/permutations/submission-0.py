class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        result=[]
        for i in range(len(nums)):
            res=nums[:i]+nums[i+1:]
            for p in self.permute(res):
                result.append([nums[i]]+p)
        return result



        