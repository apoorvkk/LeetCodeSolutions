'''
URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            val = nums[abs(nums[i]) - 1]
            if val > 0:
                nums[abs(nums[i]) - 1] = -val

        lst = []
        for i in range(len(nums)):
            if nums[i] > 0:
                lst.append(i+1)
        return lst

