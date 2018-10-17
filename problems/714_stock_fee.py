'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        ti0 = 0
        ti1 = float('-inf')

        for i in range(len(prices)):
            old_ti0 = ti0

            ti0 = max(ti0, ti1 + prices[i])
            ti1 = max(ti1, ti0 - prices[i] - fee)

        return ti0
