'''
URL: https://leetcode.com/problems/valid-parenthesis-string
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        num_open_brackets_low = 0
        num_open_brackets_high = 0


        for i in range(len(s)):
            curr_char = s[i]

            if curr_char == "(":
                num_open_brackets_low += 1
                num_open_brackets_high += 1
            elif curr_char == "*":
                num_open_brackets_low -= 1
                num_open_brackets_high += 1
            else:
                num_open_brackets_low -= 1
                num_open_brackets_high -= 1

            if num_open_brackets_low < 0 and num_open_brackets_high < 0:
                return False

            if num_open_brackets_low < 0 and num_open_brackets_high >= 0:
                num_open_brackets_low = max(0, num_open_brackets_low)

        return num_open_brackets_low <= 0 <= num_open_brackets_high
