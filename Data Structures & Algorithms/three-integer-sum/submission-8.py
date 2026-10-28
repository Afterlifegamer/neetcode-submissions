class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        
        lists=[]
        for indx,val in enumerate(nums):
           
            front=indx+1
            end=len(nums)-1
            if(indx>0)and (val==nums[indx-1]):
                continue
            
            while(front<end):
                
                sums=nums[front]+val+nums[end]
                if(sums>0):
                    end=end-1
                elif(sums<0):
                    front=front+1
                else:
                    lists.append([val,nums[front],nums[end]])
                    
                   

                    front=front+1
                    
                    
                
                    while(front<end)and(nums[front]==nums[front-1]):
                        front=front+1
               

            
        return lists
            