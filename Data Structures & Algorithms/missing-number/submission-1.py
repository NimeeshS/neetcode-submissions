class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0.5 * len(nums) * (len(nums) + 1)
        for i in nums:
            s -= i

        return int(s)