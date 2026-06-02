class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        for i in range(len(nums) - k + 1):
            l.append(max(nums[i:i+k]))

        return l