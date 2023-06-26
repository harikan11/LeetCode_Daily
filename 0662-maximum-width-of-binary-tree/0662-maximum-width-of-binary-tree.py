# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 1  # Maximum width of the binary tree
        queue = deque([(root, 0)])  # Stores the nodes and their corresponding positions

        while queue:
             level_width = len(queue)  # Number of nodes in the current level

             # Update the maximum width
             max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)

             for _ in range(level_width):
                node, position = queue.popleft()

                # Calculate the position of the child nodes
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))

        return max_width