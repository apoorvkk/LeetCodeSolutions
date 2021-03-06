'''
URL:https://leetcode.com/problems/spiral-matrix-ii/
Time complexity: O(n^2)
Space complexity: O(n^2)
'''

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0 for i in range(n)] for j in range(n)]

        width_size, height_size = n, n
        direction = 'right'


        matrix[0][0] = 1
        x, y = 0, 0
        next_val = 2
        first_row = True

        while next_val <= n**2:
            if direction == 'right':
                for i in range(1, width_size):
                    matrix[x][y+i] = next_val
                    next_val += 1

                y += width_size - 1
                direction = 'down'
                if not first_row:
                    width_size -= 1
                else:
                    first_row = False

            elif direction == 'down':
                for i in range(1, height_size):
                    matrix[x+i][y] = next_val
                    next_val += 1

                x += height_size - 1
                direction = 'left'
                height_size -= 1

            elif direction == 'left':
                for i in range(1, width_size):
                    matrix[x][y-i] = next_val
                    next_val += 1

                y = y - width_size + 1
                direction = 'up'
                width_size -= 1

            elif direction == 'up':
                for i in range(1, height_size):
                    matrix[x-i][y] = next_val
                    next_val += 1

                x = x - height_size + 1
                direction = 'right'
                height_size -= 1
        return matrix
