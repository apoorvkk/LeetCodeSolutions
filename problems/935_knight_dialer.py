'''
URL: https://leetcode.com/problems/knight-dialer/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        memo = [1 for i in range(10)]

        for k in range(N-1):
            new_memo = [0 for i in range(10)]

            new_memo[0] = memo[4] + memo[6]
            new_memo[1] = memo[6] + memo[8]
            new_memo[2] = memo[7] + memo[9]
            new_memo[3] = memo[4] + memo[8]
            new_memo[4] = memo[0] + memo[3] + memo[9]
            new_memo[6] = memo[0] + memo[1] + memo[7]
            new_memo[7] = memo[2] + memo[6]
            new_memo[8] = memo[1] + memo[3]
            new_memo[9] = memo[2] + memo[4]

            memo = new_memo


        return sum(memo) % (10**9 + 7)
