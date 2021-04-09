# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.flipped = []
        n = len(voyage)
        def dfs(node):
            if not node: return
            if node.val != voyage[self.i]:
                self.flipped = [-1]
            self.i += 1
            if self.i < n and node.left and node.left.val != voyage[self.i]:
                self.flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        if self.flipped and self.flipped[0] == -1: return [-1]
        return self.flipped
            