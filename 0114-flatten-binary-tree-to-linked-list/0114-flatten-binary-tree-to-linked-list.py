# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root): #this function returns the tail 
            if not root:
                return None #cant flatten empty tree
            #recursive case
            #first on left subtree
            leftTail= dfs(root.left)
            
            #recursive dfs on right subtree
            rightTail=dfs(root.right)
            
            #if both the subtrees are empty, no need to do anything since nothing can be added
            #if left subtree is empty, then root and right subtree are already flattened
            #only one condition left where left subtree is not empty
            if root.left:
                leftTail.right=root.right #lefttail will point to the curr right child of root
                root.right=root.left
                root.left=None
            last=rightTail or leftTail or root
            return last
        dfs(root)
                