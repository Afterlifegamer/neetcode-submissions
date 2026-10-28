# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        maxs=root.val
        def helper(node,count,maxs):
            if not node:
                return count
            if node.val>=maxs:
                maxs=node.val
                count+=1
            
            count=helper(node.left,count,maxs)
            count=helper(node.right,count,maxs)
            return count
        count=helper(root,count,maxs)
        return(count)
           
            

            
        