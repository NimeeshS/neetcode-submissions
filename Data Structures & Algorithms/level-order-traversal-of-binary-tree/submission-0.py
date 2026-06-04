# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        def dfs(root, depth):
            if root:
                if len(l) == depth:
                    l.append([])
                l[depth].append(root.val)
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)

        dfs(root, 0)
        return l