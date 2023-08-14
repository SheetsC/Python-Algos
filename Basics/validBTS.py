from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def isValidBTS(self, root: Optional[TreeNode])->bool:
        stack = [(root,float('-inf'), float('inf'))]
        while stack:
            node, min_val, max_val = stack.pop()
            if not node:
                continue
            if not (min_val < node.val < max_val):
                return False
            stack.append((node.left, min_val, node.val))
            stack.append((node.right, node.val, max_val))
        return True