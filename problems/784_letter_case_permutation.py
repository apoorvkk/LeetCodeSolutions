'''
URL: https://leetcode.com/problems/letter-case-permutation/
Time complexity: O(2^n)
Space complexity: O(n)
'''

class Solution:
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """

        possible_words = []

        self.find_words(possible_words, s, 0, "")

        return possible_words


    def find_words(self, possible_words, s, index, curr_s):
        if index >= len(s):
            possible_words.append(curr_s)
            return

        curr_letter = s[index]
        if curr_letter.isalpha():
            self.find_words(possible_words, s, index+1, curr_s+curr_letter.lower())
            self.find_words(possible_words, s, index+1, curr_s+curr_letter.upper())
        else:
            self.find_words(possible_words, s, index+1, curr_s+curr_letter)
