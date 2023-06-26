# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If the node is a leaf, return 1
        if not root.left and not root.right:
            return 1
        
        # Calculate the minimum depth of the left and right subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        # If either subtree is empty, return the depth of the non-empty subtree plus 1
        if not root.left or not root.right:
            return left_depth + right_depth + 1
        
        # Return the minimum depth among the left and right subtrees plus 1
        return min(left_depth, right_depth) + 1