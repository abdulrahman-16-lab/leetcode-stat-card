class Solution:
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        def solve(a):
            p = c = 0
            for n in a: p, c = c, max(c, p+n)
            return c
        return max(solve(nums[:-1]), solve(nums[1:]))