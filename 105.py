# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            inorder_idx = inorder.index(preorder[pre_start])
            root = TreeNode(preorder[pre_start])
            root.left = helper(pre_start + 1, pre_start + (inorder_idx - in_start), in_start, inorder_idx - 1)
            root.right = helper(pre_start + (inorder_idx - in_start) + 1, pre_end, inorder_idx+1, in_end)
            return root
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
            
        
        