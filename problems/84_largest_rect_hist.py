'''
URL: https://leetcode.com/problems/largest-rectangle-in-histogram/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0

        stack = [-1]
        max_area = 0
        heights.append(0)
        i = 0
        while i < len(heights):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                max_area = max(max_area, heights[tp] * (i-1 - stack[-1]))

        return max_area
