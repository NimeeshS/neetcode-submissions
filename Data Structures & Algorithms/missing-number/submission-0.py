class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        try:
            return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))[0]
        except:
            return 0