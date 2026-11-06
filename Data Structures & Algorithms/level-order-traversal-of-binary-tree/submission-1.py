# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            queue=deque([root])
            result=[]
            while(queue):
                size=len(queue)
                curr_array=[]
                for _ in range(size):
                    curr=queue.popleft()
                    curr_array.append(curr.val)
                    if(curr.left):
                        queue.append(curr.left)
                    if(curr.right):
                        queue.append(curr.right)
                result.append(curr_array)
            return result
        return(bfs(root))


        