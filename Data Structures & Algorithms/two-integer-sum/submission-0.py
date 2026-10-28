class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        res=[]
        for indx,value in enumerate(nums):
            remaining=target-value
            if(remaining in num):
                res.append(num[remaining])
                res.append(indx)
            else:
                num[value]=indx
        return res
