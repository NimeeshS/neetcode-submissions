class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr):
            if len(curr) == 0:
                return [[]]
            
            perms = dfs(curr[1:])
            res = []
            for p in perms:
                for i in range(len(p) + 1):
                    pc = p[:]
                    pc.insert(i, curr[0])
                    res.append(pc)
            return res

        return dfs(nums)