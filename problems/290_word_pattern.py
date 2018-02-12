'''
URL: https://leetcode.com/problems/word-pattern/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def wordPattern(self, pattern, text):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        pattern_dict = {}
        word_dict = {}

        words = text.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter not in pattern_dict:
                pattern_dict[letter] = word
            else:
                if pattern_dict[letter] != word:
                    return False

            if word not in word_dict:
                word_dict[word] = letter
            else:
                if word_dict[word] != letter:
                    return False

        return True

