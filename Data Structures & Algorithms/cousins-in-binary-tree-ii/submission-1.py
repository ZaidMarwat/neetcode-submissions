# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque([root])
        m = defaultdict(int)
        depth = 0

        # First BFS: calculate sum at each depth
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                m[depth] += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        # Second BFS: replace values
        q = deque([root])
        root.val = 0
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                if node.left:
                    node.left.val = m[depth+1] - sibling_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = m[depth+1] - sibling_sum
                    q.append(node.right)
            depth += 1
        
        return root

                