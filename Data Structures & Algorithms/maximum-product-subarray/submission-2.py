class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxNum, minNum = 1, 1
        for i in nums:
            if i == 0:
                maxNum, minNum = 1, 1
            else:
                temp = maxNum * i
                maxNum = max(temp, minNum * i, i)
                minNum = min(temp, minNum * i, i)
                res = max(res, maxNum)

        return res