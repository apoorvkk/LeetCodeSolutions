'''
URL: https://leetcode.com/contestproblems/custom-sort-string/
Time complexity: O(tlogt)
Space complexity: O(s)
'''

import functools

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        priority = {}
        for i in range(len(S)):
            letter = S[i]
            priority[letter] = i

        def customsort(letter_one, letter_two):
            letter_one_val, letter_two_val = 0, 0
            if letter_one in priority:
                letter_one_val = priority[letter_one]
            if letter_two in priority:
                letter_two_val = priority[letter_two]

            if letter_one_val == letter_two_val:
                return 0
            elif letter_one_val < letter_two_val:
                return -1
            else:
                return 1

        letters_t = [letter for letter in T]
        letters_t.sort(key=functools.cmp_to_key(customsort))

        final_str = ""
        for letter in letters_t:
            final_str += letter
        return final_str
