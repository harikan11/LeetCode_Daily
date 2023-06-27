# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return None
        q = deque([root])
        zigzag=True
        while q:
            level_size=len(q)
            curr_level=deque()
            for _ in range(level_size):
                node = q.popleft()
                
                if zigzag:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            result.append(list(curr_level))
            zigzag= not zigzag
        return result