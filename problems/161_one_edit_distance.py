'''
URL: https://leetcode.com/problems/one-edit-distance
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            strikes = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    if strikes == 1:
                        return False
                    strikes += 1
            return strikes == 1

        elif abs(len(s) - len(t)) == 1:
            shorter_str = s
            longer_str = t
            if len(t) < len(s):
                shorter_str = t
                longer_str = s

            strikes = 0
            i = 0
            j = 0
            while j < len(longer_str):
                if i >= len(shorter_str) or shorter_str[i] != longer_str[j]:
                    if strikes == 1:
                        return False
                    strikes += 1
                    j += 1
                else:
                    i += 1
                    j += 1

            return strikes == 1

        return False

