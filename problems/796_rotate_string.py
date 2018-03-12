'''
URL: https://leetcode.com/contest/problems/rotate-string/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == "":
            return False
        return B in A*2

