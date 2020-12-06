'''
URL: https://leetcode.com/problems/wildcard-matching/
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True

        for i in range(1, len(s)+1):
            dp[0][i] = False

        found_char = False
        for j in range(1, len(p)+1):
            if p[j-1].isalpha() or p[j-1] == '?':
                found_char = True

            dp[j][0] = not found_char

        for j in range(1, len(p)+1):
            for i in range(1, len(s)+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[j][i] = dp[j-1][i-1]
                elif p[j-1] == '*':
                    dp[j][i] = dp[j-1][i] or dp[j][i-1]

        return dp[-1][-1]
