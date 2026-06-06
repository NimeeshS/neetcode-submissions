class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = []

        def dfs(i, curr):
            if i >= len(nums) and sorted(curr) not in visited:
                res.append(curr[:])
                visited.append(sorted(curr))
                return
            if i >= len(nums): return

            curr.append(nums[i])
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])
        return res