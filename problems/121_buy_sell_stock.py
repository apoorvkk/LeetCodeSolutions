'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Time complexity: O(n)
Space complexity: O(1)
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        min_val = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            curr_price = prices[i]

            if curr_price >= min_val:
                max_profit = max(max_profit, curr_price - min_val)
            else:
                min_val = curr_price
        return max_profit

