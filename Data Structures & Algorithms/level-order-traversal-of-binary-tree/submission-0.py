# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count=0
        queue=collections.deque()
        queue.append(root)
        res=[]
        if not root:
            return []
        while(queue):
            temp=[]
            qlen=len(queue)
            for i in range(qlen):
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            
            
            
            res.append(temp)
        return res

            


        