'''
URL: https://leetcode.com/problems/champagne-tower/description/
Time complexity: O(n^2)
Space complexity: O(n^2)
'''

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        cache = [[0 for i in range(101)] for j in range(101)]

        cache[0][0] = poured

        for i in range(100):
            for j in range(i+1):
                if cache[i][j] > 1:
                    cache[i+1][j] += (cache[i][j] - 1) / 2.0
                    cache[i+1][j+1] += (cache[i][j] - 1) / 2.0
                    cache[i][j] = 1

        return cache[query_row][query_glass]
