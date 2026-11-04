class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index=-1
        for i in range(len(matrix)):
            if(target<matrix[i][0]):
                index=i-1
                break
        if(i==-1):
            return False
        else:
            low=0
            end=len(matrix[index])-1
            while(low<=end):
                mid=(low+end)//2
                if(matrix[index][mid]>target):
                    end=mid-1
                elif(matrix[index][mid]<target):
                    low=mid+1
                else:
                    return True
            return False

        