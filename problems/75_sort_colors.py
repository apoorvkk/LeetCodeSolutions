'''
URL: https://leetcode.com/problems/sort-colors/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        lo = 0
        mid = -1
        hi = len(nums) - 1

        while mid < hi:
            next_unknown = nums[mid+1]

            if next_unknown == 1:
                mid += 1
            elif next_unknown == 0:
                nums[lo], nums[mid+1] = nums[mid+1], nums[lo]
                lo += 1
                mid += 1
            elif next_unknown == 2:
                nums[hi], nums[mid+1] = nums[mid+1], nums[hi]
                hi -= 1

