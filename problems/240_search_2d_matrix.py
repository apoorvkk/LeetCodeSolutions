'''
URL: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
Time complexity: O(m+n)
Space complexity: O(1)
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        curr_x = 0
        curr_y = len(matrix[0]) - 1

        while curr_x < len(matrix) and curr_y >= 0:
            curr_num = matrix[curr_x][curr_y]

            if curr_num == target:
                return True
            elif curr_num > target:
                curr_y -= 1
            elif curr_num < target:
                curr_x += 1
        return False
