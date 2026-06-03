# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if root:
                ldepth = depth(root.left)
                rdepth = depth(root.right)

                return max(ldepth, rdepth) + 1

            return 0

        return depth(root)