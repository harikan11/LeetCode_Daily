# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        right = self.maxDepth(root.right) #this is for moving to the depth of right tree
        left = self.maxDepth(root.left)  # this is for moving to the depth of left tree
        return 1+max(right,left)