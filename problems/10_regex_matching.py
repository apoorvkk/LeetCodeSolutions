'''
URL: https://leetcode.com/problems/regular-expression-matching/description/
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        is_match = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]

        is_match[0][0] = True

        one_only_match = None
        for j in range(1, len(p)+1):
            if p[j-1] == "." or p[j-1].isalpha():
                is_match[0][j] = False
                if not one_only_match:
                    one_only_match = j
            else:
                if one_only_match == j-1 or not one_only_match:
                    is_match[0][j] = True
                    one_only_match = None
                else:
                    is_match[0][j] = False

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    is_match[i][j] = is_match[i-1][j-1]

                if is_match[i][j]: continue

                if p[j-1] == "*":
                    is_match[i][j] = is_match[i][j-2]
                    if is_match[i][j]: continue

                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        is_match[i][j] = is_match[i-1][j]
        return is_match[-1][-1]

