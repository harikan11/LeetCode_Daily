# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter=0 # initialise max
    
    def depth(self,node:TreeNode) -> int:
        left=self.depth(node.left) if node.left else 0
        right=self.depth(node.right) if node.right else 0
        
        #calc the diameter by taking the diameter of each node of left and right sub tree
        if left+right>self.diameter:
            self.diameter=left+right
        return 1+(left if left>right else right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter
        