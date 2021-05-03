# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def recursion(node):
            if not node: return 0
            left_length = recursion(node.left)
            right_length = recursion(node.right)
            left, right = 0, 0
            if node.left and node.left.val == node.val:
                left = left_length + 1
            if node.right and node.right.val == node.val:
                right = right_length + 1
            self.res = max(self.res, left + right)
            return max(left, right)
        recursion(root)
        return self.res