'''
URL: https://leetcode.com/problems/single-number-ii
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x1 = 0
        x2 = 0
        mask = 0

        for num in nums:
            x2 = x2 ^ (x1 & num)
            x1 = x1 ^ num

            mask = ~(x1 & x2)

            x2 = x2 & mask
            x1 = x1 & mask

        return x1

