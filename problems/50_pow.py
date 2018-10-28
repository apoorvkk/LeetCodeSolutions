'''
URL: https://leetcode.com/problems/powx-n
Time complexity: O(logn)
Space complexity: O(logn)
'''

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = self._aux_pow(x, abs(n))
        if n < 0:
            return 1 / res
        return res

    def _aux_pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half_res = self._aux_pow(x, n//2)
        res = half_res * half_res
        if n % 2 == 1:
            return res * x
        return res
