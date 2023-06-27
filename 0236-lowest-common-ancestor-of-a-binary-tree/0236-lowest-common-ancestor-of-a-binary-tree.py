# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        if root==None:
            return None 
            
        if root== p:
            return p
        if root == q:
            return q
            
        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)
            
        if l!=None and r!=None:
            return root
        return l or r