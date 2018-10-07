'''
URL: https://leetcode.com/problems/maximum-length-of-pair-chain
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) == 0:
            return 0

        pairs.sort(key=lambda x: x[1])

        count = 1
        end = pairs[0][1]

        for i in range(1, len(pairs)):
            pair = pairs[i]

            if pair[0] > end:
                count += 1
                end = pair[1]

        return count
