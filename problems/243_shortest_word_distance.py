'''
URL: https://leetcode.com/problems/shortest-word-distance/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        prev_word = None
        curr_dist = -1

        min_dist = float("inf")

        for word in words:
            if word in (word1, word2):
                if word != prev_word and curr_dist != -1:
                    min_dist = min(min_dist, curr_dist)
                prev_word = word
                curr_dist = 0

            if prev_word is not None:
                curr_dist += 1
        return min_dist
