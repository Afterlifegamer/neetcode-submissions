class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxsum=min(heights[left],heights[right])*(right-left)
        while(left<right):
            if(heights[left]<heights[right]):
                left+=1
            elif(heights[right]<heights[left]):
                right-=1
            else:
                left+=1
            sums=(min(heights[left],heights[right])*(right-left))
            maxsum=max(maxsum,sums)
        return maxsum

        