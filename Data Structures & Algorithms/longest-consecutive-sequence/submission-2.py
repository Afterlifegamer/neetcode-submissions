class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount=1
        if not nums:
            return 0
        for num in nums:
            count=1
            if (num-1) not in nums:
                val=num
                while((val+1) in nums):
                    count+=1
                    val+=1
                maxcount=max(count,maxcount)
        return maxcount
                


        