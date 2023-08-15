# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        #postorder is left-right-root and inorder is left-root-right
        root=TreeNode(postorder.pop())
        mid=inorder.index(root.val)
        root.right=self.buildTree(inorder[mid+1:],postorder)
        root.left=self.buildTree(inorder[:mid],postorder)
        return root
        