'''
URL: https://leetcode.com/problems/k-th-symbol-in-grammar/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        curr_digit = 0
        N = 2**(N-1)
        while N > 1:
            if K > N // 2:
                K -= N // 2
                curr_digit = int(not curr_digit)
            N = N // 2

        return curr_digit
