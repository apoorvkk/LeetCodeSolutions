'''
URL: https://leetcode.com/problems/basic-calculator-ii/
Time complexity: O(mn) for initialization and O(1) for computing sum
Space complexity: O(mn) for initialization and O(1) for computer sum
'''

class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        self.memo = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total = matrix[i][j]
                left_added = False
                up_added = False
                if j - 1 >= 0:
                    total += self.memo[i][j-1]
                    left_added = True
                if i - 1 >= 0:
                    total += self.memo[i-1][j]
                    up_added = True

                if left_added and up_added:
                    total -= self.memo[i-1][j-1]

                self.memo[i][j] = total


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = self.memo[row2][col2]
        left_subtracted = False
        up_subtracted = False

        if col1 - 1 >= 0:
            total -= self.memo[row2][col1-1]
            left_subtracted = True
        if row1 - 1 >= 0:
            total -= self.memo[row1-1][col2]
            up_subtracted = True

        if left_subtracted and up_subtracted:
            total += self.memo[row1-1][col1-1]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
