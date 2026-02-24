# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, level):
            nonlocal total
            if not root: 
                return
            bits[level] = root.val
            
            if not (root.left or root.right):
                total += int(''.join(map(str, bits[:level + 1])), 2)
                return
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        if not root: 
            return 0
        
        total = 0
        bits = [0]*32
        dfs(root, 0)
        return total
        
