'''
URL: https://leetcode.com/problems/pascals-triangle/description/
Time complexity: O(numRows*maxElems in a row)
Space complexity: O(n^2) where n is a single element in the 2D-array
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        rows = [[1]]
        for i in range(1, numRows):
            last_row = rows[-1]
            next_row = []
            for j in range(len(last_row)+1):
                prev_elem = last_row[j-1] if j > 0 else 0
                curr_elem = last_row[j] if j < len(last_row) else 0
                next_row.append(prev_elem+curr_elem)

            rows.append(next_row)


        return rows
