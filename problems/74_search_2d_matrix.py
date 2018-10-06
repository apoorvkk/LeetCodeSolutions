'''
URL: https://leetcode.com/problems/search-a-2d-matrix/
Time complexity: O(m + n)
Space complexity: O(1)
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False


