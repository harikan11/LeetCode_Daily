# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0

        def calHeight(root, height):
            
            if root is None:
                return height

            lheight = calHeight(root.left, height+1)
            rheight = calHeight(root.right, height+1)
            return max(lheight, rheight)

        height = calHeight(root, height)
        return height