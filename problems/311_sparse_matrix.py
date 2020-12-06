'''
URL: https://leetcode.com/problems/sparse-matrix-multiplication/
Time complexity: O(a*b*c*d) where a*b is dimension of matrix A and c*d is dimension of matrix B
Space complexity: O(1)
'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []


        answer_matrix = [[0 for j in range(len(B[0]))] for i in range(len(A))]

        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    for j in range(len(B[0])):
                        if B[k][j] != 0:
                            answer_matrix[i][j] += A[i][k] * B[k][j]
        return answer_matrix
