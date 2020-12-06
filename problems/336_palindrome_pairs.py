'''
URL: https://leetcode.com/problems/palindrome-pairs
Time complexity: O(k^2 * n) where n is number of words and k is length of word
Space complexity: O(n)
'''

class Solution(object):
    def _is_palindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_to_index = {}
        for i, word in enumerate(words):
            word_to_index[word] = i

        palindrome_pairs = []

        # full word reversals case
        for word, i in word_to_index.iteritems():
            if word[::-1] in word_to_index and word_to_index[word[::-1]] != i:
                    palindrome_pairs.append([i, word_to_index[word[::-1]]])

        # empty string case
        if "" in word_to_index:
            i = word_to_index[""]
            for j, word in enumerate(words):
                if self._is_palindrome(word) and j != i:
                    palindrome_pairs.append([i,j])
                    palindrome_pairs.append([j,i])

        # prefix/suffix case
        for i in range(len(words)):
            curr_word = words[i]

            for j in range(1, len(curr_word)):
                prefix = curr_word[:j]
                suffix = curr_word[j:]
                reversed_suffix = suffix[::-1]
                reversed_prefix = prefix[::-1]

                if self._is_palindrome(prefix):
                    if reversed_suffix in word_to_index and i != word_to_index[reversed_suffix]:
                        palindrome_pairs.append([word_to_index[reversed_suffix], i])

                if self._is_palindrome(suffix):
                    if reversed_prefix in word_to_index and i != word_to_index[reversed_prefix]:
                        palindrome_pairs.append([i, word_to_index[reversed_prefix]])
        return palindrome_pairs
