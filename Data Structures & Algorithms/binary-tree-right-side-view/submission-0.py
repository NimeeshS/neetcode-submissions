# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            qlen = len(q)
            m = 0
            for _ in range(qlen):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
                    m = max(m, n.val)
            ans.append(m)

        return ans[:-1]