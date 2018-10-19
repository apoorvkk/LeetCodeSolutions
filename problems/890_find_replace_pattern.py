'''
URL: https://leetcode.com/problems/find-and-replace-pattern/
Time complexity: O(mn)
Space complexity: O(m)
'''

class Solution:
    def _match(self, word, pattern):
        pattern_to_text = {}
        text_to_pattern = {}

        for i in range(len(word)):
            w_letter = word[i]
            p_letter = pattern[i]

            if p_letter in pattern_to_text or w_letter in text_to_pattern:
                if p_letter in pattern_to_text:
                    if pattern_to_text[p_letter] != w_letter:
                        return False

                if w_letter in text_to_pattern:
                    if text_to_pattern[w_letter] != p_letter:
                        return False
            else:
                pattern_to_text[p_letter] = w_letter
                text_to_pattern[w_letter] = p_letter
        return True

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        perms = []
        for word in words:
            if self._match(word, pattern):
                perms.append(word)
        return perms
