'''
URL: https://leetcode.com/problems/jump-game
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) in (0,1):
            return True

        curr_zero_index = None

        for i in range(len(nums)-2, -1, -1):
            if curr_zero_index:
                jump_needed = curr_zero_index - i + 1
                if nums[i] >= jump_needed:
                    curr_zero_index = None
            elif nums[i] == 0:
                    curr_zero_index = i

        return True if curr_zero_index is None else False

