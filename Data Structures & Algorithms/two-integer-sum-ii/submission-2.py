class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        right=n-1
        left=0
        output=[]
        while(left<right):
            if(numbers[left]+numbers[right]>target):
                right-=1
            elif(numbers[left]+numbers[right]<target):
                left+=1
            else:
                output.append(left+1)
                output.append(right+1)
                return output

        

        