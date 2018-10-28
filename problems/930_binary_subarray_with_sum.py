'''
URL: https://leetcode.com/problems/binary-subarrays-with-sum
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """

        count = 0
        prefix_sums = defaultdict(int)

        prefix_sums[0] = 1

        cumul_sum = 0
        for index, val in enumerate(A):
            cumul_sum += val
            count += prefix_sums[cumul_sum-S]

            prefix_sums[cumul_sum] += 1


        return count


