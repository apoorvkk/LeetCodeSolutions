'''
URL: https://leetcode.com/problems/number-of-matching-subsequences/
Time complexity: O(mnlog(s)) where m is number of words, n is length of word and s is length of elems in letters_s
Space complexity: O(s)
'''

from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        letters_s = defaultdict(list)

        for i in range(len(s)):
            curr_letter = s[i]
            letters_s[curr_letter].append(i)

        total = 0

        for word in words:
            start = 0
            used = 0
            for i in range(len(word)):
                elems = letters_s[word[i]]
                target = start

                next_index = self.binary_search(target, elems)

                if next_index == -1:
                    break
                else:
                    used += 1
                    start = next_index

            if used == len(word):
                total += 1
        return total

    def binary_search(self, target, elems):
        start = 0
        end = len(elems) - 1

        while start <= end:
            mid = (start + end) // 2


            if target < elems[start]:
                return elems[start] + 1

            if target > elems[end]:
                if end < len(elems) - 1:
                    return elems[end+1] + 1
                return -1

            if elems[mid] == target:
                return elems[mid] + 1
            elif elems[mid] > target:
                end = mid - 1
            elif elems[mid] < target:
                start = mid + 1

        return -1
