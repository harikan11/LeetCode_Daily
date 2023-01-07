"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        
        def traversal(node):
            if node is None:
                return
            
            nodes.append(node.val)
            
            for child in node.children:
                traversal(child)
            
        traversal(root)
        return nodes