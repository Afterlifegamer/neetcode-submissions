class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def subs(num,curr):
            nonlocal output
            if num==len(nums):
                output.append(curr.copy())
                return
            curr.append(nums[num])
            subs(num+1,curr)
            curr.pop()
            subs(num+1,curr)
        curr=[]
        subs(0,curr)
        return output


        