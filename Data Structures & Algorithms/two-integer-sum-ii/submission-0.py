class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num={}
        for (indx,val) in enumerate(numbers):
            if((target-val) in num):
                return[(num[target-val]+1),(indx+1)]
            else:
                num[val]=indx;

        