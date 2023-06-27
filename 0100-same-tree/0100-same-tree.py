# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # If one of the trees is empty while the other is not, they are not the same
        if not p or not q:
            return False
        # If the values of the current nodes are different, the trees are not the same
        if p.val != q.val:
            return False
        # Recursively check if the left and right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)