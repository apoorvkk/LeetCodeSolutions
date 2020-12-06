'''
URL: https://leetcode.com/problems/house-robber-ii/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(self.rob_aux(nums[:-1]), self.rob_aux(nums[1:]))

    def rob_aux(self, nums):
        if len(nums) == 0:
            return 0

        i2 = -float('inf')
        i3 = -float('inf')
        curr_i = nums[0]


        for i in range(1, len(nums)):
            old_curr_i = curr_i
            curr_i = max(nums[i] + max(i2, i3, 0), max(curr_i, 0))
            i2 = old_curr_i
            i3 = i2
        return curr_i
