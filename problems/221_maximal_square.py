'''
URL: https://leetcode.com/problems/maximal-square/
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        memo = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        max_area = 0
        for i in range(len(matrix)):
            val = int(matrix[i][0])
            memo[i][0] = val
            if val == 1:
                max_area = val
        for j in range(len(matrix[0])):
            val = int(matrix[0][j])
            memo[0][j] = val
            if val == 1:
                max_area = val

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    memo[i][j] = 1 + min(int(memo[i-1][j-1]), int(memo[i-1][j]), int(memo[i][j-1]))
                    max_area = max(max_area, memo[i][j])

        return max_area**2
