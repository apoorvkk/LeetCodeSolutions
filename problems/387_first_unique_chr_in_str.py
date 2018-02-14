'''
URL: https://leetcode.com/problems/first-unique-character-in-a-string/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        occurs = {}

        for i in range(len(s)):
            letter = s[i]
            if letter not in occurs:
                occurs[letter] = [1, i] # (no. of occurrences, first time it happened)
            else:
                occurs[letter][0] += 1

        earliest_non_repeating_chr = float("inf")
        for letter, val in occurs.items():
            if val[0] == 1: # Non -repeating char
                earliest_non_repeating_chr = min(earliest_non_repeating_chr, val[1])

        if earliest_non_repeating_chr == float("inf"):
            return -1

        return earliest_non_repeating_chr
