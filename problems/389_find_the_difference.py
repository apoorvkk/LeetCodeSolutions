'''
URL: https://leetcode.com/problems/find-the-difference/description/
Time complexity: O(n)
Space complexity: O(n)
'''


from collections import defaultdict

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = defaultdict(int)

        for letter in s:
            letters[letter] += 1

        for letter in t:
            letters[letter] -= 1

        for key, val in letters.items():
            if val != 0:
                return key

