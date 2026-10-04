# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float("-inf")

        def fn(root):
            nonlocal res

            if not root:
                return 0

            maxleft = max(0, fn(root.left))
            maxright = max(0, fn(root.right))

            # Best path where root is the highest point
            curmax = root.val + maxleft + maxright
            res = max(res, curmax)

            # Parent can only take ONE side
            return root.val + max(maxleft, maxright)

        fn(root)
        return res
