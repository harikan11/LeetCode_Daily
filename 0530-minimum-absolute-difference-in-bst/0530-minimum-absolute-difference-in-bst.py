# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        res=float('inf') #set the res to a large number to overcome edge cases 
        def dfs(node):
            if not node:
                return
            #to process left sub tree
            dfs(node.left) 
            nonlocal prev, res #have to declare them as global vars since we're using it within the dfs func
            #process the currnode and minimize the difference
            if prev:
                res=min(res,node.val-prev.val)
            prev=node
            
            
            #to process right sub tree
            dfs(node.right)
        dfs(root)
        return res