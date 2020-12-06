'''
URL: https://leetcode.com/problems/permutation-in-string
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:

    def _get_counts(self, s):
        counts = [0 for i in range(26)]

        for letter in s:
            counts[ord(letter) - 97] += 1

        return counts

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) == 0:
            return True
        elif len(s2) == 0:
            return False

        start = 0
        end = len(s1)-1
        curr_counts = self._get_counts(s2[start: end+1])
        target_counts = self._get_counts(s1)

        while end+1 < len(s2) and curr_counts != target_counts:
            start_letter = s2[start]
            curr_counts[ord(start_letter) - 97] -= 1
            start += 1

            next_letter = s2[end+1]
            curr_counts[ord(next_letter) - 97] += 1
            end += 1

        return curr_counts == target_counts
