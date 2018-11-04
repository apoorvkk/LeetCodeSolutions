'''
URL: https://leetcode.com/problems/divide-two-integers/
Time complexity: O(logn)
Space complexity: O(1)
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INTEGER_MAX = 2**31 - 1
        INTEGER_MIN = -2**31

        if not divisor or (dividend == INTEGER_MIN and divisor == -1):
            return INTEGER_MAX

        sign = -1 if dividend ^ divisor < 0 else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while dividend >= divisor:
            multiple = 1
            curr_num = divisor
            while (curr_num << 1) <= dividend:
                curr_num = curr_num << 1
                multiple = multiple << 1
            dividend -= curr_num
            res += multiple

        if sign == -1:
            return -1 * res
        return res
