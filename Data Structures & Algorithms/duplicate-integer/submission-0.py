class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=set()
        for index ,val in enumerate(nums):
            if(val not in arr):
                arr.add(val)
            
            else:
                return True
        return False