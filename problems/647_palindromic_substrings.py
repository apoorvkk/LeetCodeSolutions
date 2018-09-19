'''
URL: https://leetcode.com/problems/palindromic-substrings/description/
Time complexity: O(n^2)
Space complexity: O(n^2)
'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        memo = [[False for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            for j in range(0, i+1):
                memo[i][j] = s[i] == s[j] and ((i - j < 2) or memo[i-1][j+1])

                if memo[i][j]:
                    count += 1

        return count
