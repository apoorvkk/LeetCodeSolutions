'''
URL: https://leetcode.com/problems/longest-palindromic-subsequence/description/
Time complexity: O(n^2)
Space complexity: O(n^2)
'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) in (0,1):
            return len(s)

        memo = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            memo[i][i] = 1

        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j: continue
                if j - i == 1:
                    memo[i][j] = 1 if s[i] != s[j] else 2


                elif s[i] == s[j]:
                    memo[i][j] = 2 + memo[i+1][j-1]
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j-1])

        return memo[0][-1]


