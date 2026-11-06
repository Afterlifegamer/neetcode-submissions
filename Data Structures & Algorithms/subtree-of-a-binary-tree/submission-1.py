# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        output=False
        def same(p,q):
            if(not p and not q):
                return True
            if(not p or not q):
                return False
            left=same(p.left,q.left)
            right=same(p.right,q.right)
            if(left and right and(p.val==q.val)):
                return True
            else:
                return False
        
        def dfs(root):
            nonlocal output
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            if(root.val==subRoot.val):
                check=same(root,subRoot)
                if(check==True):
                    output=True
        dfs(root)
        return output
        
        