'''
URL: https://leetcode.com/problems/beautiful-array
Time complexity: O(nlogn)
Space complexity: O(n^2)
'''

class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        dp = {}

        dp[1] = [1]

        for i in range(2, N+1):
            dp[i] = [x*2 for x in dp[i//2]] + [x*2-1 for x in dp[i-i//2]]
        return dp[N]
