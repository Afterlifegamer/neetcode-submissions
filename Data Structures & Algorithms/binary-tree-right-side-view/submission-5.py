# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        queue=collections.deque()
        queue.append(root)
        if not root:
            return []
        while(queue):
            res.append(queue[-1].val)
            qlen=len(queue)   
            for i in range(qlen):
                node=queue.popleft()
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            
        return(res)
                

        

            
        