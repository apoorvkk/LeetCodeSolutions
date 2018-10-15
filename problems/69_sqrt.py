'''
URL: https://leetcode.com/problems/sqrtx/
Time complexity: O(logn)
Space complexity: O(1)
'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in (0,1):
            return x

        start = 1
        end = x // 2

        while start <= end:

            mid = (start + end) // 2

            squared_val = mid ** 2
            if squared_val == x:
                return mid
            elif squared_val > x:
                end = mid - 1
            elif squared_val < x:
                start = mid + 1

        return end
