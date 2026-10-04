# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0 
        res = []
        def dfs(root):
            nonlocal count
            if not root:
                return
            
            left = dfs(root.left)
            count += 1
            if count == k:
                res.append(root.val)
            right = dfs(root.right)
            return
        dfs(root)
        return res[0]