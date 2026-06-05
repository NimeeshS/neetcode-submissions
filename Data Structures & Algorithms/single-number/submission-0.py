class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen, seen_again = set(), set()
        for i in nums:
            if i in seen:
                seen_again.add(i)
            else:
                seen.add(i)

        return list(seen - seen_again)[0]