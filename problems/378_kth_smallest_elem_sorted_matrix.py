'''
URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
Time complexity: O(nlog(k))
Space complexity: O(1)
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            # ... find num of elements (count) below or equal to mid
            j = len(matrix) - 1
            for i in range(len(matrix)):

                while j >= 0 and matrix[i][j] > mid:
                    j -= 1

                count += j + 1

            if count < k:
                lo = mid + 1
            else:
                hi = mid


        return lo

