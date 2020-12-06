'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Time complexity: O(n)
Space complexity: O(k)
'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if k > len(prices) // 2:
            ti0 = 0
            ti1 = -float('inf')

            for i in range(len(prices)):
                old_ti0 = ti0
                ti0 = max(ti0, ti1 + prices[i])
                ti1 = max(ti1, old_ti0 - prices[i])

            return ti0

        ti0 = [0 for i in range(k+1)]
        ti1 = [float('-inf') for i in range(k+1)]

        for i in range(len(prices)):
            for j in range(k, 0, -1):
                ti0[j] = max(ti0[j], ti1[j] + prices[i])
                ti1[j] = max(ti1[j], ti0[j-1] - prices[i])
        return ti0[-1]
