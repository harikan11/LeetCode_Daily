# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,currsum):
            if not node:
                return False
            
            currsum+=node.val
            if not node.left and not node.right: #to check if its a leaf node
                return currsum==targetSum #returns True if the condition is true else false
                
            return (dfs(node.left,currsum) or
                    dfs(node.right,currsum))    #this is when it is not a leaf node
                    
        return dfs(root,0)
                    
                
            