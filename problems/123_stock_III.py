'''
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/#/description
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ti20 = 0
        ti21 = -float('inf')
        ti10 = 0
        ti11 = -float('inf')

        for i in range(len(prices)):
            ti20 = max(ti20, ti21 + prices[i])
            ti21 = max(ti21, ti10 - prices[i])

            ti10 = max(ti10, ti11 + prices[i])
            ti11 = max(ti11,  -prices[i])

        return ti20

