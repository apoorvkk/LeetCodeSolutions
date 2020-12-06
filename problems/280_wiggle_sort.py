'''
URL: https://leetcode.com/problems/wiggle-sort/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            if i % 2 == 1: # bigger value needed
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]

            else: # smaller value needed
                if nums[i-1] < nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
