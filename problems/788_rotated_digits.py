'''
URL: https://leetcode.com/contest/problems/rotated-digits/
Time complexity: O(nk) where k is length of number
Space complexity: O(1)
'''

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        total = 0
        for curr_num in range(1, N+1):
            num_text = str(curr_num)
            is_different = False
            is_good = True
            for digit in num_text:
                if int(digit) in (2,5,6,9):
                    is_different = True
                if int(digit) in (3, 4, 7):
                    is_good = False
            if is_good and is_different:
                total += 1

        return total
