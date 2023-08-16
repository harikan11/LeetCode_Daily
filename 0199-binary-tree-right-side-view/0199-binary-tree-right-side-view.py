# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans=[]
        queue=[root]
        while queue:
            ans.append(queue[-1].val)
            queue=[child for node in queue for child in (node.left,node.right) if child]
        return ans
            