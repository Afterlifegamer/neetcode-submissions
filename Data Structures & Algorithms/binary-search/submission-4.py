class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        end=len(nums)-1
        while(low<=end):
            mid=(low+end)//2
            if(nums[mid]>target):
                end=mid-1
            elif(nums[mid]<target):
                low=mid+1
            else:
                return mid
        return -1

        