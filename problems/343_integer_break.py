'''
URL: https://leetcode.com/problems/integer-break/description/
Time complexity: O(n^2)
Space complexity: O(n)
'''

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = [0, 1, 1]


        for i in range(3, n+1):
            curr_num = 0

            for j in range(1, len(memo)):
                curr_num = max(max(j, memo[j]) * max(i-j, memo[i-j]), curr_num)

            memo.append(curr_num)

        return memo[-1]

