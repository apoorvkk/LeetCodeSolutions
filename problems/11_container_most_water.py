'''
URL: https://leetcode.com/problems/container-with-most-water
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        max_area = 0
        while start < end:
            curr_area = (end - start) * min(nums[start], nums[end])
            max_area = max(max_area, curr_area)

            if nums[start] < nums[end]:
                start += 1
            else:
                end -= 1
        return max_area
