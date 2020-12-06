'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        ti0 = 0
        ti1 = -float('inf')
        prev_ti0 = 0

        for i in range(len(prices)):
            old_ti0 = ti0
            ti0 = max(ti0, ti1 + prices[i])
            ti1 = max(ti1, prev_ti0 - prices[i])

            prev_ti0 = old_ti0
        return ti0

