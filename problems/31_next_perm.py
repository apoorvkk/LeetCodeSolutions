'''
URL: https://leetcode.com/problems/next-permutation/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        smaller_index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                smaller_index = i
                break

        if smaller_index == -1:
            self._reverse(nums, 0, len(nums) - 1)
            return

        for i in range(len(nums) - 1, smaller_index, -1):
            if nums[i] > nums[smaller_index]:
                nums[i], nums[smaller_index] = nums[smaller_index], nums[i]
                break

        self._reverse(nums, smaller_index + 1, len(nums) - 1)

    def _reverse(self, nums, start, end):
        while end > start:
            nums[end], nums[start] = nums[start], nums[end]
            start += 1
            end -= 1

