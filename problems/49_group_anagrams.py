'''
URL: https://leetcode.com/problems/group-anagrams
Time complexity: O(n*m)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_anagrams = defaultdict(list)

        for word in strs:
            word_encoding = self.get_word_encoding(word)

            grouped_anagrams[word_encoding].append(word)

        grouped_anagrams_lst = []
        for word_encoding, words in grouped_anagrams.iteritems():
            grouped_anagrams_lst.append(words)

        return grouped_anagrams_lst

    def get_word_encoding(self, word):
        char_arr = [0 for i in range(26)]

        for letter in word:
            char_arr[ord(letter) - 97] += 1

        return str(char_arr)
