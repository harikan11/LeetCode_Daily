# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root,mx,mi):
            if not root:
                return True
            elif root.val>=mx or root.val<=mi:
                return False
            else:
                return BST(root.left,root.val,mi) and BST(root.right,mx,root.val)
        return BST(root,float('inf'),float('-inf'))