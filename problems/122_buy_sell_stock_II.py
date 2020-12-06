'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
