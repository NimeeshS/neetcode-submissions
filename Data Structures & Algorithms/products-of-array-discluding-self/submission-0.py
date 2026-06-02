class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        p = nums[0]
        for i in range(1, len(nums)):
            l[i] = p
            p *= nums[i]
        p = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            l[i] *= p
            p *= nums[i]

        return l