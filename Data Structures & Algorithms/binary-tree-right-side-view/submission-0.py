# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = [root.val]
        
        def dfs(root, depth):
            nonlocal res
            if not root:
                return
            
            if len(res) == depth+1:
                if root.right:
                    res.append(root.right.val)
                elif root.left:
                    res.append(root.left.val)

            right = dfs(root.right, depth+1)
            left = dfs(root.left, depth+1)
            
        dfs(root, 0)
        return res
