# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        idxs = {val:idx for idx,val in enumerate(inorder)}

        count = 0
        def dfs(l, r):
            nonlocal count
            if l > r:
                return
            
            rootval = preorder[count]
            root = TreeNode(rootval)
            m = idxs[rootval]
            count += 1
            root.left = dfs(l, m-1)
            root.right = dfs(m+1, r)
            return root
        
        return dfs(0, len(inorder)-1)