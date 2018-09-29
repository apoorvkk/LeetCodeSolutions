'''
URL: https://leetcode.com/problems/online-stock-span
Time complexity: O(n)
Space complexity: O(n)
'''

class StockSpanner(object):

    def __init__(self):
        self.prev_results = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count = 1

        while len(self.prev_results) > 0 and price >= self.prev_results[-1][0]:
            count += self.prev_results.pop()[1]

        self.prev_results.append((price, count))

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
