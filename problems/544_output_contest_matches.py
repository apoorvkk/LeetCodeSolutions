'''
URL: https://leetcode.com/problems/output-contest-matches/description/
Time complexity: O(nlogn)
Space complexity: O(n)
'''

class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """

        elems = [str(i) for i in range(1, n+1)]

        while n > 1:
            for i in range(n // 2):
                elems[i] = "(" + elems[i] + "," + elems[n-i-1] + ")"
            n = n // 2
        return elems[0]
