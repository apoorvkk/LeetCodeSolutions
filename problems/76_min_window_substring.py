'''
URL: https://leetcode.com/problems/minimum-window-substring/
Time complexity: O(n)
Space complexity: O(k)
'''

from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        start, end = 0, -1
        min_start, min_end = 0, -1
        visited_letters = defaultdict(int)
        characters = defaultdict(int)
        for char in t:
            characters[char] += 1
        num_characters_left = len(t)

        while end + 1 < len(s):
            next_letter = s[end+1]

            if next_letter in characters:
                visited_letters[next_letter] += 1
                if visited_letters[next_letter] <= characters[next_letter]:
                    num_characters_left -= 1

            while num_characters_left == 0:
                if min_end == -1 or (min_end - min_start >= end+1 - start):
                    min_start = start
                    min_end = end+1

                start_letter = s[start]
                if start_letter in characters:
                    visited_letters[start_letter] -= 1
                    if visited_letters[start_letter] < characters[start_letter]:
                        num_characters_left += 1
                start += 1

            end += 1

        return s[min_start: min_end+1]

