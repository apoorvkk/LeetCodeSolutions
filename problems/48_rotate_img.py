'''
URL: https://leetcode.com/problems/rotate-image/description/
Time complexity: O(n^2)
Space complexity: O(1)
'''

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix_size = len(matrix)

        for j in range(matrix_size // 2):
            for i in range(matrix_size-1):
                top = (j, j+i)
                right = (j+i, j + matrix_size - 1)
                bottom = (j + matrix_size - 1, j + matrix_size - 1 - i)
                left = (j + matrix_size - 1 - i, j)

                first_elem = matrix[top[0]][top[1]]
                matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
                matrix[left[0]][left[1]] = matrix[bottom[0]][bottom[1]]
                matrix[bottom[0]][bottom[1]] = matrix[right[0]][right[1]]
                matrix[right[0]][right[1]] = first_elem

            matrix_size -= 2
