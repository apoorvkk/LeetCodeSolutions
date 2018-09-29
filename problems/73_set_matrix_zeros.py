'''
URL: https://leetcode.com/problems/set-matrix-zeroes
Time complexity: O(n^2)
Space complexity: O(1)
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_zero = False
        column_zero = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_zero = True

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                column_zero = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if column_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

