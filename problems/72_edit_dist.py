'''
URL: https://leetcode.com/problems/edit-distance/description/
Time complexity: O(m*n)
Space complexity: O(m*n)
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

        for i in range(len(word1)+1):
            memo[i][0] = i

        for j in range(len(word2)+1):
            memo[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])

                add_both_chars = memo[i-1][j-1]

                if word1[i-1] != word2[j-1]:
                    add_both_chars += 1
                memo[i][j] = min(add_both_chars, memo[i][j])


        return memo[-1][-1]
