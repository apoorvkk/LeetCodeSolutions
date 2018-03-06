'''
URL: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def count(b):
            result = 0
            curr = 0

            for elem in A:
                if elem <= b:
                    curr += 1
                else:
                    curr = 0
                result += curr

            return result
        return count(R) - count(L-1)
