'''
URL: https://leetcode.com/problems/trapping-rain-water/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        left_highest = [0 for i in range(len(heights))]
        right_highest = [0 for i in range(len(heights))]

        max_height = 0
        for i in range(len(heights)):
            left_highest[i] = max_height

            max_height = max(max_height, heights[i])

        max_height = 0
        for i in range(len(heights)-1, -1, -1):
            right_highest[i] = max_height

            max_height = max(max_height, heights[i])

        total_volume = 0
        for i in range(len(heights)):
            total_volume += max(min(left_highest[i] - heights[i], right_highest[i] - heights[i]),0)
        return total_volume
