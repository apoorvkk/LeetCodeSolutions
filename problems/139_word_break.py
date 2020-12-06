'''
URL: https://leetcode.com/problems/word-break
Time complexity: O(n^2)
Space complexity: O(n^2 + m) n is size of string, m is size of word dictionary
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)

        return self.aux_word_break(s, wordDict, set())

    def aux_word_break(self, s, wordDict, memo):
        if s in wordDict:
            return True

        if s in memo:
            return False

        if len(s) == 0:
            return True

        for word in wordDict:
            curr_segment = word

            if s.startswith(curr_segment) and self.aux_word_break(s[len(curr_segment):], wordDict, memo):
                return True
        memo.add(s)
        return False
