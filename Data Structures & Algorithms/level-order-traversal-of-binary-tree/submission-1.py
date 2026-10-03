# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[]]
        def dfs(root, depth):
            nonlocal res
            if not root:
                return

            if len(res) <= depth:
                res.append([])

            res[depth].append(root.val)

            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
        
        dfs(root, 0)

        return res



