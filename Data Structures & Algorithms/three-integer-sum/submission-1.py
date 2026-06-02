class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    if [nums[l], nums[r], nums[i]] not in answer:
                        answer.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1 
                else:
                    r -= 1

        return answer