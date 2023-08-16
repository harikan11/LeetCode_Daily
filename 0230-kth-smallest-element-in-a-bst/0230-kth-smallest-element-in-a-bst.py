# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        
        res.sort()
        return res[k - 1]