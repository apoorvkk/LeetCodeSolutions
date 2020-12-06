'''
URL: https://leetcode.com/problems/diagonal-traverse
Time complexity: O(mn)
Space complexity: O(1)
'''

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        start = (0,0)
        end = (0,0)
        direction = 'up'

        diag_order = []
        for _ in range(m + n - 1):
            curr_pointer, target = start, end
            if direction == 'down':
                curr_pointer, target = target, curr_pointer

            while 0 <= curr_pointer[0] < m and 0 <= curr_pointer[1] < n:
                x, y = curr_pointer
                diag_order.append(matrix[x][y])

                if direction == 'up':
                    curr_pointer = (x-1, y+1)
                else:
                    curr_pointer = (x+1, y-1)

            start_x, start_y = start
            if start_x + 1 < m:
                start = (start_x+1, start_y)
            else:
                start = (start_x, start_y+1)

            end_x, end_y = end
            if end_y + 1 < n:
                end = (end_x, end_y+1)
            else:
                end = (end_x+1, end_y)

            if direction == 'up':
                direction = 'down'
            else:
                direction = 'up'
        return diag_order
