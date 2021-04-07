# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        length = len(inorder)
        def helper(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            root = TreeNode(postorder[post_end])
            in_idx = inorder_map[postorder[post_end]]
            right_side_length = in_end - in_idx
            root.left = helper(in_start, in_idx - 1, post_start, post_end - right_side_length - 1)
            root.right = helper(in_idx + 1, in_end, post_end - right_side_length, post_end-1)
            return root
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, length - 1, 0, length - 1)
        